import numpy as np
import pytest

from src.game import Action2048, Game2048


@pytest.fixture()
def game():
    return Game2048()


def test_move_up(game):
    game._grid = np.array([
        [0, 0, 0, 2],
        [0, 2, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
    ]).astype(np.uint8)

    np.testing.assert_equal(game.grid, np.array([
        [0, 0, 0, 4],
        [0, 4, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 2, 0],
    ]))

    moved, score = game.move(Action2048.UP)

    np.testing.assert_equal(game.grid, np.array([
        [2, 4, 2, 4],
        [0, 2, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]))

    assert score == 0
    assert moved == 4


def test_move_left():
    game = Game2048()
    game._grid = np.array([
        [0, 0, 0, 2],
        [0, 2, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
    ]).astype(np.uint8)

    np.testing.assert_equal(game.grid, np.array([
        [0, 0, 0, 4],
        [0, 4, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 2, 0],
    ]))

    moved, score = game.move(Action2048.LEFT)

    np.testing.assert_equal(game.grid, np.array([
        [4, 0, 0, 0],
        [4, 0, 0, 0],
        [0, 0, 0, 0],
        [4, 2, 0, 0],
    ]))

    assert score == 4
    assert moved == 4


def test_move_right():
    game = Game2048()
    game._grid = np.array([
        [0, 0, 0, 2],
        [0, 2, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
    ]).astype(np.uint8)

    np.testing.assert_equal(game.grid, np.array([
        [0, 0, 0, 4],
        [0, 4, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 2, 2],
    ]))

    moved, score = game.move(Action2048.RIGHT)

    np.testing.assert_equal(game.grid, np.array([
        [0, 0, 0, 4],
        [0, 0, 0, 4],
        [0, 0, 0, 0],
        [0, 0, 4, 4],
    ]))

    assert score == 8
    assert moved == 4


def test_move_down():
    game = Game2048()
    game._grid = np.array([
        [0, 0, 1, 2],
        [0, 2, 1, 0],
        [0, 0, 2, 0],
        [1, 1, 2, 0],
    ]).astype(np.uint8)

    np.testing.assert_equal(game.grid, np.array([
        [0, 0, 2, 4],
        [0, 4, 2, 0],
        [0, 0, 4, 0],
        [2, 2, 4, 0],
    ]))

    moved, score = game.move(Action2048.DOWN)

    np.testing.assert_equal(game.grid, np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 4, 4, 0],
        [2, 2, 8, 4],
    ]))


    assert score == 12
    assert moved == 5


def test_game_over():
    game = Game2048()
    game._grid = np.array([
        [5, 3, 1, 1],
        [3, 4, 2, 3],
        [1, 6, 4, 1],
        [4, 1, 2, 4],
    ]).astype(np.uint8)

    np.testing.assert_equal(game.grid, np.array([
        [32, 8, 2, 2],
        [8, 16, 4, 8],
        [2, 64, 16, 2],
        [16, 2, 4, 16],
    ]))

    moved, score = game.play(Action2048.DOWN)

    np.testing.assert_equal(game.grid, np.array([
        [32, 8, 2, 2],
        [8, 16, 4, 8],
        [2, 64, 16, 2],
        [16, 2, 4, 16],
    ]))

    assert moved == 0
    assert score == 0
    assert game.game_over == False

    moved, score = game.play(Action2048.RIGHT)

    np.testing.assert_equal(game.grid[1:], np.array([
        [8, 16, 4, 8],
        [2, 64, 16, 2],
        [16, 2, 4, 16],
    ]))

    np.testing.assert_equal(game.grid[0][1:], np.array([32, 8, 4]))

    assert moved == 3
    assert game.grid[0][0] == 2 or game.grid[0][0] == 4
    assert game.game_over == True


def test_is_game_over_when_tile_match_are_available():
    game = Game2048()
    game._grid = np.array([
        [5, 2, 1, 1],
        [3, 4, 3, 5],
        [1, 6, 4, 1],
        [4, 1, 2, 4],
    ]).astype(np.uint8)

    np.testing.assert_equal(game.grid, np.array([
        [32, 4, 2, 2],
        [8, 16, 8, 32],
        [2, 64, 16, 2],
        [16, 2, 4, 16],
    ]))

    moved, score = game.play(Action2048.LEFT)

    np.testing.assert_equal(game.grid[1:], np.array([
        [8, 16, 8, 32],
        [2, 64, 16, 2],
        [16, 2, 4, 16],
    ]))

    first_row = list(game.grid[0])

    assert first_row == [32, 4, 4, 2] or first_row == [32, 4, 4, 4]
    assert game.game_over == False


def test_can_move_any_direction_when_cells_are_available():
    game = Game2048()
    game._grid = np.array([
        [5, 2, 1, 1],
        [3, 4, 0, 5],
        [1, 6, 4, 1],
        [4, 1, 2, 4],
    ]).astype(np.uint8)

    assert game.can_move(Action2048.UP)
    assert game.can_move(Action2048.RIGHT)
    assert game.can_move(Action2048.DOWN)
    assert game.can_move(Action2048.LEFT)


def test_can_move_when_no_cells_available():
    game = Game2048()
    game._grid = np.array([
        [5, 2, 1, 1],
        [3, 4, 2, 5],
        [1, 6, 4, 1],
        [4, 1, 2, 4],
    ]).astype(np.uint8)

    assert not game.can_move(Action2048.UP)
    assert not game.can_move(Action2048.DOWN)
    assert game.can_move(Action2048.RIGHT)
    assert game.can_move(Action2048.LEFT)


def test_can_move_special_case():
    game = Game2048()
    game._grid = np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
    ]).astype(np.uint8)

    assert game.can_move(Action2048.UP)
    assert game.can_move(Action2048.RIGHT)
    assert game.can_move(Action2048.LEFT)
    assert not game.can_move(Action2048.DOWN)
