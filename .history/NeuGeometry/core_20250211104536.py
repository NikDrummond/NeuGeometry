import numpy as np
from jax import jit
import jax.numpy as jnp
from typing import TypeAlias

from .helpers import raise_dim_error

Array: Type
def normalise(arr: Array) -> Array:


    norms = jnp.linalg.norm(arr, axis=-1, keepdims=True)  # Works for both 1D and 2D arrays
    return arr / norms

