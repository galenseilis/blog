# Explanation

## Convexity and the Hessian

A scalar function of several variables is **convex** if the line segment between
any two points on its graph lies on or above the graph. For a twice
continuously differentiable function the standard test is the second-order
condition: the function is convex exactly where its **Hessian** — the matrix of
all second partial derivatives — is positive semi-definite.

Positive semi-definiteness is checked through the eigenvalues: a symmetric
matrix is positive semi-definite when all of its eigenvalues are non-negative.
So the question "is $p(t)$ convex in $k, p_0, r$?" becomes "are the eigenvalues
of this $3 \times 3$ matrix non-negative on the relevant domain?".

## Why the symbolic route gets unwieldy

The Verhulst function is a ratio of exponentials, and its second derivatives are
correspondingly complicated. The blog post derives the Hessian with SymPy and
then asks for its eigenvalues. Even for a $3 \times 3$ matrix the characteristic
polynomial is large, and the algebraic eigenvalues are enormous expressions.
SymPy produces them exactly, but exactness is not the same as legibility: the
closed form is hard to reason about by eye.

## The pragmatic alternative

Because the parameters are constrained to be positive (and the time `t` is a
non-negative real), a symbolic definiteness proof is not the only option.
Substituting representative and corner-case values — zeros, ones, limits, and a
spread of interior points — into the numeric Hessian and checking the signs of
the eigenvalues gives strong evidence for or against convexity. It is not a
proof, but it is often enough to settle a modelling question, and it is what the
post falls back on.

## Trade-offs

- **Exact but opaque.** Symbolic results are exact and general, but can be too
  large to interpret.
- **Numerical but partial.** Substituting values is easy to read, but only
  samples finitely many points and can miss a sign change.
- **Proof versus evidence.** A convexity claim for a model usually needs either a
  symbolic argument or a counterexample; a finite numerical sweep provides
  neither, only a hint about where to look.

## Caveats

The Hessian is taken with respect to the parameters, holding $t$ fixed; convexity
in the parameters is a different statement from the more familiar S-shape of
$p(t)$ as a function of time. Also, "convex" here should be read as convex over
the positive orthant only, since $k$ and $p_0$ are constrained to be positive.
