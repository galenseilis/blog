from notes_process_modelling.example import (
    build_lts1,
    build_lts2,
    synchronous_product_demo,
)
from notes_process_modelling.lts import LTS


def test_product_state_set_is_the_cartesian_product():
    product = synchronous_product_demo()
    assert product.S == ["s1s3", "s1s4", "s2s3", "s2s4"]


def test_product_actions_are_the_shared_actions():
    product = synchronous_product_demo()
    assert product.A == {"a"}


def test_product_transitions_require_a_shared_action():
    product = synchronous_product_demo()
    assert set(product.transitions) == {
        ("s1s3", "a", "s2s4"),
        ("s1s4", "a", "s2s3"),
        ("s2s3", "a", "s1s4"),
        ("s2s4", "a", "s1s3"),
    }


def test_product_initial_and_accepting_states():
    product = synchronous_product_demo()
    assert product.initial_state == "s1s3"
    assert product.accepting_states == ["s2s4"]


def test_product_requires_an_lts_operand():
    import pytest

    with pytest.raises(TypeError, match="Operand must be an LTS"):
        build_lts1() * 3


def test_private_actions_are_absent_from_the_product():
    product = synchronous_product_demo()
    assert "b" not in product.A
    assert "c" not in product.A


def test_builders_return_lts_instances():
    assert isinstance(build_lts1(), LTS)
    assert isinstance(build_lts2(), LTS)
