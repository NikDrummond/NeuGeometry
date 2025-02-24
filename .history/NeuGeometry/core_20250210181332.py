import numpy as np
import math

def normalise(arr):
    """_summary_

    Parameters
    ----------
    arr : np.ndarray
        Either a single vector, or a stacked array of vectors

    Returns
    -------
    _type_
        _description_

    Raises
    ------
    ValueError
        _description_
    """
    if arr.ndim == 1:
        return arr / np.linalg.norm(arr)
    elif arr.ndim == 2:
        return arr / np.linalg.norm(arr, axis = 1)[:, np.newaxis]
    else:
        raise ValueError('arr must be one or two dimensional!')
    
