use moose_ou::{MooseConfig, histogram, simulate, summarise};

fn small_config() -> MooseConfig {
    MooseConfig {
        kappa: 0.5,
        sigma: 1.0,
        dt: 0.01,
        steps: 500,
        moose: 4_000,
        centre: 0.0,
        seed: 12345,
    }
}

#[test]
fn stationary_sd_matches_closed_form() {
    let config = MooseConfig::default();
    // sigma / sqrt(2 kappa) with sigma = 1 and kappa = 0.5 is exactly 1.
    assert!((config.stationary_sd() - 1.0).abs() < 1e-12);
}

#[test]
fn t_end_is_the_product_of_step_size_and_steps() {
    let config = MooseConfig::default();
    assert!((config.t_end() - 20.0).abs() < 1e-12);
}

#[test]
fn simulation_starts_and_ends_with_the_requested_population() {
    let config = small_config();
    let positions = simulate(&config);
    assert_eq!(positions.len(), config.moose);
}

#[test]
fn simulation_is_reproducible_for_a_fixed_seed() {
    let config = small_config();
    assert_eq!(simulate(&config), simulate(&config));
}

#[test]
fn simulated_moments_approach_the_analytic_values() {
    let config = small_config();
    let positions = simulate(&config);
    let summary = summarise(&config, &positions);

    // The ensemble is large, so the sample moments should be close to the
    // analytic stationary values to within a few percent.
    assert!((summary.mean_x - summary.centre).abs() < 0.1);
    assert!((summary.mean_y - summary.centre).abs() < 0.1);
    assert!((summary.sd_x - summary.stationary_sd).abs() < 0.1);
    assert!((summary.sd_y - summary.stationary_sd).abs() < 0.1);
    assert!((summary.mean_radius - summary.mean_radius_analytic).abs() < 0.1);
}

#[test]
fn histogram_counts_only_positions_inside_the_range() {
    let positions = vec![(-10.0, 0.0), (0.0, 0.0), (1.0, 0.0), (10.0, 0.0)];
    let counts = histogram(&positions, -3.0, 3.0, 12);
    assert_eq!(counts.iter().sum::<usize>(), 2);
}

#[test]
fn analytic_mean_radius_is_the_rayleigh_mean() {
    let config = MooseConfig::default();
    let expected = config.stationary_sd() * std::f64::consts::FRAC_PI_2.sqrt();
    assert!((config.mean_radius() - expected).abs() < 1e-12);
}
