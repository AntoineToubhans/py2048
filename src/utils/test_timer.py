from .timer import timeit


def test_time_is_return():
    @timeit
    def f(x, abc=0):
        """My Awesome docstring"""
        return x + abc

    assert f.__doc__ == "My Awesome docstring"

    t, result = f(1, abc=23)
    assert result == 24
