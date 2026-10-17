import math

import numpy as np
import pytest

from moose_ou_fp.fokker_planck import (
    CENTRE,
    KAPPA,
    SIGMA,
    analytic_pdf,
    analytic_variance,
    diagnostics,
    plot_comparison,
    solve_fokker_planck,
    stationary_sd,
)


def test_stationary_sd_matches_closed_form():
    assert stationary_sd() == pytest.approx(SIGMA / math.sqrt(2 * KAPPA))


def test_analytic_variance_starts_at_zero_and_relaxes_to_equilibrium():
    assert analytic_variance(0.0) == pytest.approx(0.0)
    assert analytic_variance(1e6) == pytest.approx(SIGMA**2 / (2 * KAPPA), rel=1e-6)


def test_analytic_variance_follows_the_relaxation_factor():
    t = 0.7
    expected = SIGMA**2 / (2 * KAPPA) * (1 - math.exp(-2 * KAPPA * t))
    assert analytic_variance(t) == pytest.approx(expected)


def test_analytic_pdf_integrates_to_one():
    x = np.linspace(-20, 20, 4001)
    density = analytic_pdf(x, 3.0)
    integral = np.sum(density) * (x[1] - x[0])
    assert integral == pytest.approx(1.0, rel=1e-3)


def test_analytic_pdf_is_centred_and_symmetric():
    x = np.array([-1.0, 0.0, 1.0])
    density = analytic_pdf(x, 5.0)
    assert density[1] == pytest.approx(density.max())
    assert density[0] == pytest.approx(density[2])


def test_solve_conserves_mass_and_stays_nonnegative():
    x, _times, _snapshots, masses, _means, _variances = solve_fokker_planck(
        extent=5.0, dx=0.05, dt=1e-3, t_end=1.0
    )
    del x
    assert masses[0] == pytest.approx(1.0)
    assert masses[-1] == pytest.approx(1.0, abs=1e-9)
    assert np.all(masses > 0.0)


def test_solve_variance_grows_towards_the_analytic_value():
    _x, _times, _snapshots, _masses, _means, variances = solve_fokker_planck(
        extent=5.0, dx=0.05, dt=1e-3, t_end=2.0
    )
    assert variances[0] == pytest.approx(0.0, abs=1e-12)
    assert variances[-1] == pytest.approx(analytic_variance(2.0), rel=0.05)


def test_diagnostics_reports_expected_keys():
    _x, _times, _snapshots, masses, means, variances = solve_fokker_planck(
        extent=5.0, dx=0.05, dt=1e-3, t_end=1.0
    )
    diag = diagnostics(masses, means, variances, t_end=1.0)
    assert set(diag) == {
        "mass",
        "pde_variance",
        "analytic_variance",
        "pde_mean",
        "analytic_mean",
    }
    assert diag["mass"] == pytest.approx(1.0, abs=1e-9)
    assert diag["analytic_mean"] == CENTRE


def test_plot_comparison_writes_a_file(tmp_path):
    rng = np.random.default_rng(0)
    x_positions = rng.normal(0.0, 1.0, 500)
    y_positions = rng.normal(0.0, 1.0, 500)
    t_track = np.linspace(0.0, 2.0, 50)
    x_track = np.zeros(50)
    y_track = np.zeros(50)

    solve = solve_fokker_planck(extent=5.0, dx=0.05, dt=1e-3, t_end=2.0)
    output = tmp_path / "figures" / "moose_fokker_planck.png"
    written = plot_comparison(
        x_positions, y_positions, t_track, x_track, y_track, solve, output
    )
    assert written == output
    assert output.exists()
