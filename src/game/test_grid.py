import numpy as np
import pytest

from src.game import Action
from src.game.exceptions import NoFreeCellError
from src.game.grid import Grid


@pytest.fixture()
def grid():
    grid = Grid()
    grid._grid = np.array(
        [[0, 0, 0, 2], [0, 2, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0],]
    ).astype(np.uint8)

    return grid


def test_grid_return_power_two(grid):
    np.testing.assert_equal(
        grid.values, np.array([[0, 0, 0, 4], [0, 4, 0, 0], [0, 0, 0, 0], [2, 2, 2, 0],])
    )


def test_move_up(grid):
    moved, score = grid.move(Action.UP)

    assert score == 0
    assert moved == 4

    np.testing.assert_equal(
        grid.values, np.array([[2, 4, 2, 4], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],])
    )


def test_move_left(grid):
    moved, score = grid.move(Action.LEFT)

    assert score == 4
    assert moved == 4

    np.testing.assert_equal(
        grid.values, np.array([[4, 0, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0], [4, 2, 0, 0],])
    )


def test_move_right(grid):
    moved, score = grid.move(Action.RIGHT)

    assert score == 4
    assert moved == 4

    np.testing.assert_equal(
        grid.values, np.array([[0, 0, 0, 4], [0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 2, 4],])
    )


def test_move_down(grid):
    moved, score = grid.move(Action.DOWN)

    assert score == 0
    assert moved == 2

    np.testing.assert_equal(
        grid.values, np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 0, 0], [2, 2, 2, 4],])
    )


def test_raise_no_free_cell_error():
    grid = Grid()
    grid._grid = np.array(
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],]
    ).astype(np.uint8)

    with pytest.raises(NoFreeCellError):
        grid.add_random_tile()
