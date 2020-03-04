import pytest
import numpy as np

from src.game import Action
from .modifiable_game_manager import ModifiableGameManager


@pytest.fixture()
def game():
    modifiable_game_manager = ModifiableGameManager(
        initial_state=np.array(
            [[0, 8, 8, 8], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        ),
    )

    return modifiable_game_manager


def test_initial_state(game):
    np.testing.assert_array_equal(
        game._grid._grid,
        np.array([[0, 3, 3, 3], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]).astype(
            np.uint8
        ),
    )


def test_game_is_copied(game):
    copied_game = game.copy()

    assert 0 == game.score
    assert 0 == copied_game.score

    game.play(Action.RIGHT)
    copied_game.play(Action.DOWN)

    assert 16 == game.score
    assert 0 == copied_game.score
