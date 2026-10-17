//! Virtual moose movement from an Ornstein-Uhlenbeck process.
//!
//! Units are kilometres and hours. Each virtual moose has a home-range
//! centre and is pulled back towards it with strength `kappa`, while an
//! exploratory random walk of strength `sigma` pushes it away:
//!
//! ```text
//! dx = -kappa * (x - c) dt + sigma * dW
//! ```
//!
//! The collection of moose is simulated as independent It^o processes with
//! an Euler-Maruyama scheme. The density of the positions then evolves
//! according to the Fokker-Planck equation
//!
//! ```text
//! dp/dt = kappa * d/dx[(x - c) p] + (sigma^2 / 2) * d^2p/dx^2
//! ```
//!
//! which for this drift and diffusion has the closed-form stationary
//! solution `Normal(c, sigma / sqrt(2 * kappa))` per axis. The printed
//! summary compares the simulated final positions against that analytic
//! answer.

use std::fs::File;
use std::io::Write;

use rand::SeedableRng;
use rand::rngs::StdRng;
use rand_distr::{Distribution, Normal};

/// Parameters for the movement model.
#[derive(Clone, Copy, Debug)]
pub struct MooseConfig {
    /// Home-range fidelity, in 1/h.
    pub kappa: f64,
    /// Exploratory jitter, in km/sqrt(h).
    pub sigma: f64,
    /// Time step, in h.
    pub dt: f64,
    /// Number of time steps.
    pub steps: usize,
    /// Number of virtual moose.
    pub moose: usize,
    /// Home-range centre, in km.
    pub centre: f64,
    /// Seed for reproducibility.
    pub seed: u64,
}

impl Default for MooseConfig {
    fn default() -> Self {
        Self {
            kappa: 0.5,       // Strong fidelity: relaxation time 1/kappa = 2 h
            sigma: 1.0,       // Exploratory motion
            dt: 0.01,         // 36 s fixes, finer than a typical GPS schedule
            steps: 2_000,     // 20 h of simulated movement
            moose: 10_000,    // Virtual population size
            centre: 0.0,      // Home-range centre at the origin
            seed: 20_261_016, // Arbitrary fixed seed
        }
    }
}

impl MooseConfig {
    /// Total simulated time, in hours.
    #[must_use]
    pub fn t_end(&self) -> f64 {
        self.dt * self.steps as f64
    }

    /// Analytic stationary standard deviation per axis, in km.
    #[must_use]
    pub fn stationary_sd(&self) -> f64 {
        self.sigma / (2.0 * self.kappa).sqrt()
    }

    /// Analytic mean distance from the centre at stationarity, in km.
    #[must_use]
    pub fn mean_radius(&self) -> f64 {
        self.stationary_sd() * std::f64::consts::FRAC_PI_2.sqrt()
    }
}

/// Simulate the final positions of a population of virtual moose.
///
/// Every moose starts at the home-range centre and is stepped forward with
/// the Euler-Maruyama scheme.
#[must_use]
pub fn simulate(config: &MooseConfig) -> Vec<(f64, f64)> {
    let mut positions = vec![(config.centre, config.centre); config.moose];

    let mut rng = StdRng::seed_from_u64(config.seed);

    // Standard normal draws for the increments of the Wiener process.
    let normal = Normal::new(0.0_f64, 1.0).unwrap();
    let sqrt_dt = config.dt.sqrt();

    // Euler-Maruyama time stepping of the It^o process.
    for _ in 0..config.steps {
        for position in positions.iter_mut() {
            let dw_x = normal.sample(&mut rng) * sqrt_dt;
            let dw_y = normal.sample(&mut rng) * sqrt_dt;

            position.0 += -config.kappa * (position.0 - config.centre) * config.dt
                + config.sigma * dw_x;
            position.1 += -config.kappa * (position.1 - config.centre) * config.dt
                + config.sigma * dw_y;
        }
    }

    positions
}

/// Summary statistics of a simulated population, with analytic references.
#[derive(Clone, Copy, Debug)]
pub struct Summary {
    /// Sample mean of the x coordinate, in km.
    pub mean_x: f64,
    /// Sample mean of the y coordinate, in km.
    pub mean_y: f64,
    /// Sample standard deviation of x, in km.
    pub sd_x: f64,
    /// Sample standard deviation of y, in km.
    pub sd_y: f64,
    /// Sample mean distance from the centre, in km.
    pub mean_radius: f64,
    /// Home-range centre, in km.
    pub centre: f64,
    /// Analytic stationary standard deviation per axis, in km.
    pub stationary_sd: f64,
    /// Analytic mean distance from the centre at stationarity, in km.
    pub mean_radius_analytic: f64,
}

/// Compute summary statistics of a simulated population.
#[must_use]
pub fn summarise(config: &MooseConfig, positions: &[(f64, f64)]) -> Summary {
    let n = positions.len() as f64;

    let mean_x = positions.iter().map(|p| p.0).sum::<f64>() / n;
    let mean_y = positions.iter().map(|p| p.1).sum::<f64>() / n;

    let sd_x = (positions.iter().map(|p| (p.0 - mean_x).powi(2)).sum::<f64>() / n).sqrt();
    let sd_y = (positions.iter().map(|p| (p.1 - mean_y).powi(2)).sum::<f64>() / n).sqrt();

    let mean_radius = positions
        .iter()
        .map(|p| p.0.hypot(p.1))
        .sum::<f64>()
        / n;

    Summary {
        mean_x,
        mean_y,
        sd_x,
        sd_y,
        mean_radius,
        centre: config.centre,
        stationary_sd: config.stationary_sd(),
        mean_radius_analytic: config.mean_radius(),
    }
}

/// Count how many positions fall in each of `bins` equal bins on `[min, max)`.
#[must_use]
pub fn histogram(positions: &[(f64, f64)], min: f64, max: f64, bins: usize) -> Vec<usize> {
    let bin_size = (max - min) / bins as f64;
    let mut counts = vec![0_usize; bins];

    for position in positions {
        if position.0 >= min && position.0 < max {
            let bin = ((position.0 - min) / bin_size) as usize;
            counts[bin] += 1;
        }
    }

    counts
}

fn print_config(config: &MooseConfig) {
    println!("Movement model: dx = -kappa (x - c) dt + sigma dW   (Ornstein-Uhlenbeck)");
    println!(
        "kappa = {:.3} 1/h, sigma = {:.3} km/sqrt(h), dt = {:.4} h, steps = {} (T = {:.1} h)",
        config.kappa,
        config.sigma,
        config.dt,
        config.steps,
        config.t_end()
    );
    println!(
        "{} virtual moose, seed {}, home-range centre at {:.1} km",
        config.moose, config.seed, config.centre
    );
    println!(
        "Analytic stationary sd per axis: sigma / sqrt(2 kappa) = {:.3} km",
        config.stationary_sd()
    );
}

fn print_summary(summary: &Summary) {
    println!("\nFinal positions at t = T:");
    println!("{:<28}{:>10}{:>10}", "quantity", "simulated", "analytic");
    println!(
        "{:<28}{:>10.3}{:>10.3}",
        "mean x (km)", summary.mean_x, summary.centre
    );
    println!(
        "{:<28}{:>10.3}{:>10.3}",
        "mean y (km)", summary.mean_y, summary.centre
    );
    println!(
        "{:<28}{:>10.3}{:>10.3}",
        "sd x (km)", summary.sd_x, summary.stationary_sd
    );
    println!(
        "{:<28}{:>10.3}{:>10.3}",
        "sd y (km)", summary.sd_y, summary.stationary_sd
    );
    println!(
        "{:<28}{:>10.3}{:>10.3}",
        "mean radius from centre (km)", summary.mean_radius, summary.mean_radius_analytic
    );
}

fn print_histogram(positions: &[(f64, f64)]) {
    let bins = 12;
    let min = -3.0;
    let max = 3.0;
    let bin_size = (max - min) / bins as f64;
    let counts = histogram(positions, min, max, bins);

    println!("\nMarginal distribution of x (each * is about 40 moose):");
    for (i, &count) in counts.iter().enumerate() {
        let bin_start = min + i as f64 * bin_size;
        let bar = "*".repeat(count / 40);
        println!(
            "{:>5.2} to {:>5.2} | {} ({})",
            bin_start,
            bin_start + bin_size,
            bar,
            count
        );
    }
}

/// Final positions of every virtual moose, for downstream plotting.
fn write_positions(positions: &[(f64, f64)]) -> std::io::Result<()> {
    let mut file = File::create("data/moose_positions.csv")?;
    writeln!(file, "x,y")?;
    for (x, y) in positions {
        writeln!(file, "{x:.6},{y:.6}")?;
    }
    Ok(())
}

/// One representative trajectory, subsampled for downstream plotting.
fn write_track(config: &MooseConfig) -> std::io::Result<()> {
    let mut rng = StdRng::seed_from_u64(config.seed);
    let normal = Normal::new(0.0_f64, 1.0).unwrap();
    let sqrt_dt = config.dt.sqrt();

    let mut x = config.centre;
    let mut y = config.centre;

    let mut file = File::create("data/moose_track.csv")?;
    writeln!(file, "t,x,y")?;

    let record_every = 10;
    for step in 0..=config.steps {
        if step % record_every == 0 {
            writeln!(file, "{:.3},{x:.6},{y:.6}", step as f64 * config.dt)?;
        }
        if step == config.steps {
            break;
        }
        let dw_x = normal.sample(&mut rng) * sqrt_dt;
        let dw_y = normal.sample(&mut rng) * sqrt_dt;
        x += -config.kappa * (x - config.centre) * config.dt + config.sigma * dw_x;
        y += -config.kappa * (y - config.centre) * config.dt + config.sigma * dw_y;
    }
    Ok(())
}

/// Simulate, print the summary, and write the plotting CSVs for `config`.
///
/// # Errors
///
/// Returns an error if the CSV files under `data/` cannot be written.
pub fn run_with_config(config: &MooseConfig) -> std::io::Result<()> {
    let positions = simulate(config);
    let summary = summarise(config, &positions);

    print_config(config);
    print_summary(&summary);
    print_histogram(&positions);

    write_positions(&positions)?;
    write_track(config)?;
    Ok(())
}

/// Run the model with the default parameters used in the blog post.
///
/// # Errors
///
/// Returns an error if the CSV files under `data/` cannot be written.
pub fn run() -> std::io::Result<()> {
    run_with_config(&MooseConfig::default())
}
