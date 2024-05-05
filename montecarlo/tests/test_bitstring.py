"""
 test for bitstring in the montecarlo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import montecarlo
import numpy as np
from numpy.testing import assert_array_equal


def test_montecarlo_bistring_class():
    """Tests if bitstring class can be initialized and functions work properly"""
    N = 10
    bs = montecarlo.BitString(N)
    assert_array_equal(bs.config, np.array([0,0,0,0,0,0,0,0,0,0]))
    bs.set_int_config(2**8-1)
    assert_array_equal(bs.config, np.array([0,0,1,1,1,1,1,1,1,1]))
    bs.flip_site(2)
    assert_array_equal(bs.config, np.array([0,0,0,1,1,1,1,1,1,1]))
    assert bs.int() == 2**7-1
    assert bs.on() == 7
    assert bs.off() == 3

