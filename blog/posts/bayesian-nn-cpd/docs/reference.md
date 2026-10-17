# Reference

## API

- `simulate_data(size: int = 3) -> tuple[np.ndarray, int]`
- `build_model(size: int = 3, observed: np.ndarray | None = None) -> pm.Model`
- `main(output_path: str | Path = "test.pickle", cores: int = 1) -> int`

## CLI

`bayesian-nn-cpd` — runs a tiny sample and saves `test.pickle`.
