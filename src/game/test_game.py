import numpy as np
import pytest

from src.game import Action, GameManager


@pytest.fixture()
def game():
    return GameManager()


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

    assert not game.is_game_over()

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
    assert game.is_game_over()


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
    assert not game.is_game_over()


def test_available_actions_when_there_are_free_cells(game):
    game._grid._grid = np.array([
        [5, 2, 1, 1],
        [3, 4, 0, 5],
        [1, 6, 4, 1],
        [4, 1, 2, 4],
    ]).astype(np.uint8)

    assert game.get_available_actions() == [
        Action.UP,
        Action.RIGHT,
        Action.DOWN,
        Action.LEFT,
    ]


def test_available_actions_when_there_are_no_free_cells(game):
    game._grid._grid = np.array([
        [5, 2, 1, 1],
        [3, 4, 2, 5],
        [1, 6, 4, 1],
        [4, 1, 2, 4],
    ]).astype(np.uint8)

    assert game.get_available_actions() == [
        Action.RIGHT,
        Action.LEFT,
    ]


def test_available_actions_when_no_bottom_zero(game):
    game._grid._grid = np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
    ]).astype(np.uint8)

    assert game.get_available_actions() == [
        Action.UP,
        Action.RIGHT,
        Action.LEFT,
    ]
