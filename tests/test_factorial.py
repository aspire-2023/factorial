import math
import pytest
from factorial import factorial


def test_factorial():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(79) == math.factorial(79)
    with pytest.raises(ValueError, match=r'number is negative'):
        assert factorial(-1)
    assert factorial(0) == 1

