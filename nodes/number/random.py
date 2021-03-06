import numpy as np

from svrx.typing import Float, Int
from svrx.nodes.node_base import node_func

from svrx.util.function import generator


@node_func(bl_idname="SvRxNodeNumberRandom", multi_label="Random", id=0)
@generator
def random_int(size: Int = 1, low: Int = 0, high: Int = 10, seed: Int = 1) -> [Int]:
    """Return random integers from low (inclusive) to high (inclusive)
    """
    np.random.seed(seed)
    return np.random.random_integers(low, high, size)


@node_func(id=1)
@generator
def randint(size: Int = 1, low: Int = 0, high: Int = 10, seed: Int = 1) -> [Int]:
    """Return random integers from low (inclusive) to high (exclusive)
    """
    np.random.seed(seed)
    return np.random.randint(low, high, size)


@node_func(id=2)
@generator
def random_float(size: Int = 1, low: Float = 0.0, high: Float = 1.0, seed: Int = 1) -> [Float]:
    np.random.seed(seed)
    #  here we could be clever and only scale if needed.
    return (high - low) * np.random.random_sample(size) + low
