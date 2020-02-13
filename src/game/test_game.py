import numpy as np
import pytest

from src.game import Action, GameManager


@pytest.fixture()
def game():
    return GameManager()


def test_grid_return_power_two(game):
    game._grid._grid = np.array([
        [0, 0, 0, 2],
        [0, 2, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
    ]).astype(np.uint8)

    np.testing.assert_equal(game.get_state(), np.array([
        [0, 0, 0, 4],
        [0, 4, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 2, 0],
    ]))


def test_move_up(game):
    game._grid._grid = np.array([
        [0, 0, 0, 2],
        [0, 2, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
    ]).astype(np.uint8)

    moved, score = game.move(Action.UP)

    np.testing.assert_equal(game.get_state(), np.array([
        [2, 4, 2, 4],
        [0, 2, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]))

    assert score == 0
    assert moved == 4


def test_move_left(game):
    game._grid._grid = np.array([
        [0, 0, 0, 2],
        [0, 2, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
    ]).astype(np.uint8)

    moved, score = game.move(Action.LEFT)

    np.testing.assert_equal(game.get_state(), np.array([
        [4, 0, 0, 0],
        [4, 0, 0, 0],
        [0, 0, 0, 0],
        [4, 2, 0, 0],
    ]))

    assert score == 4
    assert moved == 4


def test_move_right(game):
    game._grid._grid = np.array([
        [0, 0, 0, 2],
        [0, 2, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
    ]).astype(np.uint8)

    moved, score = game.move(Action.RIGHT)

    np.testing.assert_equal(game.get_state(), np.array([
        [0, 0, 0, 4],
        [0, 0, 0, 4],
        [0, 0, 0, 0],
        [0, 0, 4, 4],
    ]))

    assert score == 8
    assert moved == 4


def test_move_down(game):
    game._grid._grid= np.array([
        [0, 0, 1, 2],
        [0, 2, 1, 0],
        [0, 0, 2, 0],
        [1, 1, 2, 0],
    ]).astype(np.uint8)

    moved, score = game.move(Action.DOWN)

    np.testing.assert_equal(game.get_state(), np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 4, 4, 0],
        [2, 2, 8, 4],
    ]))

    assert score == 12
    assert moved == 5


def test_game_over(game):
    game._grid._grid = np.array([
        [5, 3, 1, 1],
        [3, 4, 2, 3],
        [1, 6, 4, 1],
        [4, 1, 2, 4],
    ]).astype(np.uint8)

    reward = game.play(Action.DOWN)

    assert reward.score == 0
    assert reward.tiles_moved == 0

    np.testing.assert_equal(game.get_state(), np.array([
        [32, 8, 2, 2],
        [8, 16, 4, 8],
        [2, 64, 16, 2],
        [16, 2, 4, 16],
    ]))

    assert not game.game_over

    reward = game.play(Action.RIGHT)

    assert reward.score == 4
    assert reward.tiles_moved == 3

    state = game.get_state()

    np.testing.assert_equal(state[1:], np.array([
        [8, 16, 4, 8],
        [2, 64, 16, 2],
        [16, 2, 4, 16],
    ]))

    np.testing.assert_equal(state[0][1:], np.array([32, 8, 4]))

    assert state[0][0] == 2 or state[0][0] == 4
    assert game.game_over


def test_is_game_over_when_tile_match_are_available(game):
    game._grid._grid = np.array([
        [5, 2, 1, 1],
        [3, 4, 3, 5],
        [1, 6, 4, 1],
        [4, 1, 2, 4],
    ]).astype(np.uint8)

    game.play(Action.LEFT)

    state = game.get_state()

    np.testing.assert_equal(state[1:], np.array([
        [8, 16, 8, 32],
        [2, 64, 16, 2],
        [16, 2, 4, 16],
    ]))

    first_row = list(state[0])

    assert first_row == [32, 4, 4, 2] or first_row == [32, 4, 4, 4]
    assert not game.game_over


def test_can_move_any_direction_when_cells_are_available(game):
    game._grid._grid = np.array([
        [5, 2, 1, 1],
        [3, 4, 0, 5],
        [1, 6, 4, 1],
        [4, 1, 2, 4],
    ]).astype(np.uint8)

    assert game.can_move(Action.UP)
    assert game.can_move(Action.RIGHT)
    assert game.can_move(Action.DOWN)
    assert game.can_move(Action.LEFT)


def test_can_move_when_no_cells_available(game):
    game._grid._grid = np.array([
        [5, 2, 1, 1],
        [3, 4, 2, 5],
        [1, 6, 4, 1],
        [4, 1, 2, 4],
    ]).astype(np.uint8)

    assert not game.can_move(Action.UP)
    assert not game.can_move(Action.DOWN)
    assert game.can_move(Action.RIGHT)
    assert game.can_move(Action.LEFT)


def test_can_move_special_case(game):
    game._grid._grid = np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
    ]).astype(np.uint8)

    assert game.can_move(Action.UP)
    assert game.can_move(Action.RIGHT)
    assert game.can_move(Action.LEFT)
    assert not game.can_move(Action.DOWN)
