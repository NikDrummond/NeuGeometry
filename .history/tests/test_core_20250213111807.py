import jax.numpy as jnp
import pytest
from NeuGeometry import core

### normalise

def test_normalise_1d_nonzero_array():
    input_arr = jnp.array([1.0, 2.0, 3.0])
    result = core.normalise(input_arr)
    assert jnp.allclose(jnp.linalg.norm(result), 1.0)

def test_normalise_2d_nonzero_array(self):
    input_arr = jnp.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    result = core.normalise(input_arr)
    norms = jnp.linalg.norm(result, axis=1)
    assert jnp.allclose(norms, jnp.ones_like(norms))

# Function rejects 3D or higher dimensional arrays with assertion error
def test_rejects_3d_array(self):
    input_arr = jnp.ones((2, 2, 2))
    try:
        normalise(input_arr)
    except AssertionError as e:
        assert str(e) == "Input arr must be 1D or 2D"