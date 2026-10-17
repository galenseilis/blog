from notes_order_theory.latex_pairs import latex_pairs, main

EXPECTED = r"\\{(a, a), (a, b), (a, c), (a, d), (a, e), (b, a), (b, b), (b, c), (b, d), (b, e), (c, a), (c, b), (c, c), (c, d), (c, e), (d, a), (d, b), (d, c), (d, d), (d, e), (e, a), (e, b), (e, c), (e, d), (e, e)\\}"  # noqa: E501


def test_latex_pairs_matches_the_post():
    assert latex_pairs(("a", "b", "c", "d", "e")) == EXPECTED


def test_latex_pairs_has_every_ordered_pair():
    result = latex_pairs(("x", "y"))
    assert result.count("(") == 4
    assert result.count("(x,") == 2
    assert "(x, x)" in result
    assert "(y, x)" in result


def test_main_prints_the_post_output(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == EXPECTED


def test_latex_pairs_uses_two_sets_of_escaped_braces():
    result = latex_pairs(("a",))
    assert result.startswith(r"\\{")
    assert result.endswith(r"\\}")
