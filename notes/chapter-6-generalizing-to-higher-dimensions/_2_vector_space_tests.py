from _1_generalizing_definition_of_vectors import *
from hypothesis import given, note, strategies as st


@given(
    st.integers(), st.integers(), st.integers(), st.integers()
)
def commutative_vectors(u_x, u_y, v_x, v_y):
    u = Vec2(u_x, u_y)
    v = Vec2(v_x, v_y)
    result = u + v == v + u
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers(), st.integers(), st.integers()
)
def associative_vectors(u_x, u_y, v_x, v_y, w_x, w_y):
    u = Vec2(u_x, u_y)
    v = Vec2(v_x, v_y)
    w = Vec2(w_x, w_y)
    result = (u + v) + w == u + (v + w)
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers()
)
def multiply_several_scalars_multiply_all_scalars(v_x, v_y, scalar_1, scalar_2):
    v = Vec2(v_x, v_y)
    result = scalar_1 * (scalar_2 * v) == (scalar_1 * scalar_2) * v
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers()
)
def multiply_one_unchanged(v_x, v_y):
    v = Vec2(v_x, v_y)
    result = v == v * 1
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers()
)
def test_addition_scalars_compatible_scalar_multiplication(v_x, v_y, scalar_1, scalar_2):
    v = Vec2(v_x, v_y)
    result = scalar_1 * v + scalar_2 * v == (scalar_1 + scalar_2) * v
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers(), st.integers()
)
def test_addition_vectors_compatible_scalar_multiplication(u_x, u_y, v_x, v_y, scalar):
    u = Vec2(u_x, u_y)
    v = Vec2(v_x, v_y)
    result = scalar * (u + v) == scalar * v + scalar * u
    note(f"Result: {result}")
    assert result == True


try:
    commutative_vectors()
    associative_vectors()
    multiply_several_scalars_multiply_all_scalars()
    multiply_one_unchanged()
    test_addition_scalars_compatible_scalar_multiplication()
except AssertionError:
    print("result != True")
