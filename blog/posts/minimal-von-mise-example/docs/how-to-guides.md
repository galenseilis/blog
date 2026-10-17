# How-to Guides

## Run (non-interactive sampling only if display unavailable)

The original post shows plots; the packaged CLI runs a tiny sample and calls
`plt.show()`. In headless environments you may want to call `build_model` and
`pm.sample` directly with `progressbar=False`.
