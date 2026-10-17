"""Find pandigital factorial numbers by checking trailing digits."""

from __future__ import annotations

from math import factorial
from typing import List


def is_pandigital(num: int) -> bool:
    """Check if a number is pandigital (contains each digit 0-9 at least once).

    Note: This implementation as written in the original script checks
    if all digits 0-9 appear in the string representation of the number.
    """
    s = str(num)
    for i in range(10):
        if str(i) not in s:
            return False
    return True


def is_pandigital_last_m(num_str: str, m: int | None = None) -> bool:
    """Check if the last m digits form a pandigital sequence containing all digits 0-9."""
    # For the original case, they check the full string representation
    # of the factorial's trailing digits
    s = num_str
    for i in range(10):
        if str(i) not in s:
            return False
    return True


def search_pandigital_factorials_up_to(k: int = 1001, m: int = 200) -> List[List]:
    """Search for pandigital factorials in factorial values up to n=k-1.

    This reproduces the logic from the original script.
    """
    results = []
    for n in range(k):
        fact_n = factorial(n)
        fact_str = str(fact_n)[::-1][:m][::-1]
        results.append([n, is_pandigital(fact_str), fact_str])
    return results


def format_results(results: List[List]) -> str:
    """Format results as a markdown table."""
    import pandas as pd

    df = pd.DataFrame(results, columns=["n", f"last_{len(results[0][2]) if results else 200}_is_pandigital", "last_m"])
    # But the original used fixed column name based on m
    if results:
        m_len = len(results[0][2])  # actual length used
    else:
        m_len = 200
    df = pd.DataFrame(
        results,
        columns=["n", f"last_{m_len}_is_pandigital", f"last_{m_len}"],
    )
    return df.to_markdown(index=False)


def main() -> None:
    """Run the search and print formatted results."""
    import pandas as pd
    import sys

    sys.set_int_max_str_digits(1_000_000)  # Prevent large string representations

    k = 1000 + 1
    m = 200
    results = []
    for n in range(k):
        fact_n = factorial(n)
        fact_str = str(fact_n)[::-1][:m][::-1]
        results.append([n, is_pandigital(fact_str), fact_str])

    df = pd.DataFrame(
        results,
        columns=["n", f"last_{m}_is_pandigital", f"last_{m}"],
    )
    print(df.to_markdown(index=False))


if __name__ == "__main__":
    main()
