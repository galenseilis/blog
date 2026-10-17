# Explanation

## Points and vectors live in different spaces

A curve `C` sits inside the plane `R^2`, and a point `p` on the curve is a
point of `C`. A tangent vector at `p` is not a point of `C`; it lives in the
tangent space `T_pC`, which is a copy of the plane attached at `p`. The first
two figures make that distinction visible by drawing the curve and its
tangent space together, while the dashed magenta lines show how the point
`p = (a, f(a))` pulls back onto the `x` and `y` axes.

## Coordinates versus differentials

Coordinates `(x, y)` take a point of the curve to a pair of numbers. Their
differentials `(dx, dy)` take a *tangent vector* to a pair of numbers, so
`dx` and `dy` are coordinate functions on the tangent space rather than on the
curve. For a curve given by `y = f(x)`, the tangent vector at `a` is
`(1, f'(a))`, which is why the tangent space is the span of `(1, f'(a))`:

```
T_pC = span{ (1, f'(a)) } = { (c, c f'(a)) | c in R }.
```

The differential-axes figure draws exactly this: a vector `<c, d>` expressed
against the `dx` and `dy` axes.

## From the picture to `dy = f'(a) dx`

On the parabola the tangent vector is `(dx, dy) = (1, 2a)`, so `dy = 2a dx`
and `dy/dx = 2a = f'(a)`. The picture and the calculus agree because the
differential coordinates are a basis of the cotangent space, and evaluating
`dx` and `dy` on the tangent vector recovers the components of the vector in
the ambient coordinates.

## Why package the figures

The post's figures are pure side effects of three standalone scripts. Wrapping
each in a function that takes an output path makes them importable, testable,
and reusable, and gives a single source of truth that the post includes
directly. The drawings themselves are unchanged; only the surrounding I/O was
lifted into functions.
