from sample_linear_random_ode import sample_linear_random_ode


def test_sample_linear_random_ode_creates_file(tmp_path):
    out = tmp_path / "example.png"
    result = sample_linear_random_ode(n_samples=2, n_points=10, t_max=10, output_path=str(out))
    assert result == str(out)
    assert out.exists()
