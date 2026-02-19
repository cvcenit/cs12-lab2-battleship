# pyright: strict

from model import BattleshipModel
from random import Random, seed
import pytest

def test_turn():
    game_one = BattleshipModel(6, (4, 3, 2, 2), Random(seed()), 4)

    # Case for one turn each
    assert game_one.turn == 0
    game_one.go_to_next_turn()
    assert game_one.turn == 1
    game_one.go_to_next_turn()
    assert game_one.turn == 2
    game_one.go_to_next_turn()
    assert game_one.turn == 3
    game_one.go_to_next_turn()
    assert game_one.turn == 4
    game_one.go_to_next_turn()
    assert game_one.turn == 0

    # Case for multiple turns
    assert game_one.turn == 0
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    assert game_one.turn == 2
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    assert game_one.turn == 4
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    assert game_one.turn == 1
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    assert game_one.turn == 3
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    assert game_one.turn == 0

# TESTS FOR shoot()
# test for shoot on different type of grids (in this case, the player loses)
def test_shooting_player_grid_one_horizontal_one_vertical_version_one():
    game_one = BattleshipModel(4, (3, 2), Random(100), 4)

    # player grid
    original_player_grid_game_one = list(game_one.grids()[0])
    
    with pytest.raises(AssertionError):
        game_one.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_one():
        game_one.shoot(0, 0)
        game_one.shoot(0, 1)
        game_one.shoot(1, 0)
        game_one.shoot(1, 1)
        game_one.shoot(1, 2)
        game_one.shoot(2, 0)
        game_one.shoot(2, 1)
        game_one.shoot(2, 2)
        game_one.shoot(3, 0)
        game_one.shoot(3, 1)
        game_one.shoot(3, 2)
    
    shoot_empty_cells_game_one()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_one == game_one.grids()[0]

    # shoot a horizontal ship
    game_one.shoot(0, 2)
    assert game_one.grids()[0] == ['..bb', '...A', '...A', '...A']
    # shooting it again/an empty cell should not make a difference
    game_one.shoot(0, 2)
    game_one.shoot(0, 3)
    shoot_empty_cells_game_one()
    assert game_one.grids()[0] == ['..bb', '...A', '...A', '...A']

    # shoot a vertical ship
    game_one.shoot(2, 3)
    assert game_one.grids()[0] == ['..bb', '...a', '...a', '...a']

    # game is already over since the player has lost
    assert game_one.is_game_over()
    assert game_one.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_one.shoot(1, 3)
    with pytest.raises(AssertionError):
        game_one.shoot(2, 3)
    with pytest.raises(AssertionError):
        game_one.shoot(3, 3)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_one()


    # Same grids, different parts of boat to shoot
    game_two = BattleshipModel(4, (3, 2), Random(100), 4)

    # player grid
    original_player_grid_game_two = list(game_two.grids()[0])
    
    with pytest.raises(AssertionError):
        game_two.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_two():
        game_two.shoot(0, 0)
        game_two.shoot(0, 1)
        game_two.shoot(1, 0)
        game_two.shoot(1, 1)
        game_two.shoot(1, 2)
        game_two.shoot(2, 0)
        game_two.shoot(2, 1)
        game_two.shoot(2, 2)
        game_two.shoot(3, 0)
        game_two.shoot(3, 1)
        game_two.shoot(3, 2)
    
    shoot_empty_cells_game_two()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_two == game_two.grids()[0]

    # shoot a horizontal ship
    game_two.shoot(0, 3)
    assert game_two.grids()[0] == ['..bb', '...A', '...A', '...A']
    # shooting it again/an empty cell should not make a difference
    game_two.shoot(0, 2)
    game_two.shoot(0, 3)
    shoot_empty_cells_game_two()
    assert game_two.grids()[0] == ['..bb', '...A', '...A', '...A']

    # shoot a vertical ship
    game_two.shoot(1, 3)
    assert game_two.grids()[0] == ['..bb', '...a', '...a', '...a']

    # game is already over since the player has lost
    assert game_two.is_game_over()
    assert game_two.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_two.shoot(1, 3)
    with pytest.raises(AssertionError):
        game_two.shoot(2, 3)
    with pytest.raises(AssertionError):
        game_two.shoot(3, 3)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_two()


    # Same grids, different parts of boat to shoot
    game_three = BattleshipModel(4, (3, 2), Random(100), 4)

    # player grid
    original_player_grid_game_three = list(game_three.grids()[0])
    
    with pytest.raises(AssertionError):
        game_three.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_three():
        game_three.shoot(0, 0)
        game_three.shoot(0, 1)
        game_three.shoot(1, 0)
        game_three.shoot(1, 1)
        game_three.shoot(1, 2)
        game_three.shoot(2, 0)
        game_three.shoot(2, 1)
        game_three.shoot(2, 2)
        game_three.shoot(3, 0)
        game_three.shoot(3, 1)
        game_three.shoot(3, 2)
    
    shoot_empty_cells_game_three()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_three == game_three.grids()[0]

    # shoot a horizontal ship
    game_three.shoot(0, 3)
    assert game_three.grids()[0] == ['..bb', '...A', '...A', '...A']
    # shooting it again/an empty cell should not make a difference
    game_three.shoot(0, 2)
    game_three.shoot(0, 3)
    shoot_empty_cells_game_three()
    assert game_three.grids()[0] == ['..bb', '...A', '...A', '...A']

    # shoot a vertical ship
    game_three.shoot(3, 3)
    assert game_three.grids()[0] == ['..bb', '...a', '...a', '...a']

    # game is already over since the player has lost
    assert game_three.is_game_over()
    assert game_three.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_three.shoot(1, 3)
    with pytest.raises(AssertionError):
        game_three.shoot(2, 3)
    with pytest.raises(AssertionError):
        game_three.shoot(3, 3)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_two()

def test_shooting_player_grid_one_horizontal_one_vertical_version_two():
    game_one = BattleshipModel(4, (3, 2), Random(1), 4)

    # player grid
    original_player_grid_game_one = list(game_one.grids()[0])
    
    with pytest.raises(AssertionError):
        game_one.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_one():
        game_one.shoot(0, 0)
        game_one.shoot(1, 0)
        game_one.shoot(1, 2)
        game_one.shoot(1, 3)
        game_one.shoot(2, 0)
        game_one.shoot(2, 2)
        game_one.shoot(2, 3)
        game_one.shoot(3, 0)
        game_one.shoot(3, 1)
        game_one.shoot(3, 2)
        game_one.shoot(3, 3)
    
    shoot_empty_cells_game_one()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_one == game_one.grids()[0]

    # shoot a horizontal ship
    game_one.shoot(0, 2)
    assert game_one.grids()[0] == ['.Abb', '.A..', '.A..', '....']
    # shooting it again/an empty cell should not make a difference
    game_one.shoot(0, 2)
    game_one.shoot(0, 3)
    shoot_empty_cells_game_one()
    assert game_one.grids()[0] == ['.Abb', '.A..', '.A..', '....']

    # shoot a vertical ship
    game_one.shoot(0, 1)
    assert game_one.grids()[0] == ['.abb', '.a..', '.a..', '....']

    # game is already over since the player has lost
    assert game_one.is_game_over()
    assert game_one.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_one.shoot(0, 1)
    with pytest.raises(AssertionError):
        game_one.shoot(1, 1)
    with pytest.raises(AssertionError):
        game_one.shoot(2, 1)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_one()


    game_two = BattleshipModel(4, (3, 2), Random(1), 4)

    # player grid
    original_player_grid_game_two = list(game_two.grids()[0])
    
    with pytest.raises(AssertionError):
        game_two.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_two():
        game_two.shoot(0, 0)
        game_two.shoot(1, 0)
        game_two.shoot(1, 2)
        game_two.shoot(1, 3)
        game_two.shoot(2, 0)
        game_two.shoot(2, 2)
        game_two.shoot(2, 3)
        game_two.shoot(3, 0)
        game_two.shoot(3, 1)
        game_two.shoot(3, 2)
        game_two.shoot(3, 3)
    
    shoot_empty_cells_game_two()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_two == game_two.grids()[0]

    # shoot a horizontal ship
    game_two.shoot(0, 3)
    assert game_two.grids()[0] == ['.Abb', '.A..', '.A..', '....']
    # shooting it again/an empty cell should not make a difference
    game_two.shoot(0, 2)
    game_two.shoot(0, 3)
    shoot_empty_cells_game_two()
    assert game_two.grids()[0] == ['.Abb', '.A..', '.A..', '....']

    # shoot a vertical ship
    game_two.shoot(1, 1)
    assert game_two.grids()[0] == ['.abb', '.a..', '.a..', '....']

    # game is already over since the player has lost
    assert game_two.is_game_over()
    assert game_two.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_two.shoot(0, 1)
    with pytest.raises(AssertionError):
        game_two.shoot(1, 1)
    with pytest.raises(AssertionError):
        game_two.shoot(2, 1)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_one()


    game_three = BattleshipModel(4, (3, 2), Random(1), 4)

    # player grid
    original_player_grid_game_three = list(game_three.grids()[0])
    
    with pytest.raises(AssertionError):
        game_three.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_three():
        game_three.shoot(0, 0)
        game_three.shoot(1, 0)
        game_three.shoot(1, 2)
        game_three.shoot(1, 3)
        game_three.shoot(2, 0)
        game_three.shoot(2, 2)
        game_three.shoot(2, 3)
        game_three.shoot(3, 0)
        game_three.shoot(3, 1)
        game_three.shoot(3, 2)
        game_three.shoot(3, 3)
    
    shoot_empty_cells_game_three()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_three == game_three.grids()[0]

    # shoot a horizontal ship
    game_three.shoot(0, 3)
    assert game_three.grids()[0] == ['.Abb', '.A..', '.A..', '....']
    # shooting it again/an empty cell should not make a difference
    game_three.shoot(0, 2)
    game_three.shoot(0, 3)
    shoot_empty_cells_game_three()
    assert game_three.grids()[0] == ['.Abb', '.A..', '.A..', '....']

    # shoot a vertical ship
    game_three.shoot(2, 1)
    assert game_three.grids()[0] == ['.abb', '.a..', '.a..', '....']

    # game is already over since the player has lost
    assert game_three.is_game_over()
    assert game_three.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_three.shoot(0, 1)
    with pytest.raises(AssertionError):
        game_three.shoot(1, 1)
    with pytest.raises(AssertionError):
        game_three.shoot(2, 1)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_one()

def test_shooting_player_grid_two_vertical():
    # both ships are vertical
    game_one = BattleshipModel(4, (3, 2), Random(15), 4)

    # player grid
    original_player_grid_game_one = list(game_one.grids()[0])
    
    with pytest.raises(AssertionError):
        game_one.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_one():
        game_one.shoot(0, 1)
        game_one.shoot(0, 2)
        game_one.shoot(1, 1)
        game_one.shoot(1, 2)
        game_one.shoot(2, 1)
        game_one.shoot(2, 2)
        game_one.shoot(2, 3)
        game_one.shoot(3, 0)
        game_one.shoot(3, 1)
        game_one.shoot(3, 2)
        game_one.shoot(3, 3)
    
    shoot_empty_cells_game_one()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_one == game_one.grids()[0]

    # shoot one of the ship
    game_one.shoot(0, 0)
    assert game_one.grids()[0] == ['a..B', 'a..B', 'a...', '....']
    # shooting it again/an empty cell should not make a difference
    game_one.shoot(0, 0)
    game_one.shoot(1, 0)
    game_one.shoot(2, 0)
    shoot_empty_cells_game_one()
    assert game_one.grids()[0] == ['a..B', 'a..B', 'a...', '....']

    # shoot the other ship
    game_one.shoot(0, 3)
    assert game_one.grids()[0] == ['a..b', 'a..b', 'a...', '....']

    # game is already over since the player has lost
    assert game_one.is_game_over()
    assert game_one.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_one.shoot(0, 0)
    with pytest.raises(AssertionError):
        game_one.shoot(1, 0)
    with pytest.raises(AssertionError):
        game_one.shoot(2, 0)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_one()

    # same grid, different cell to shoot
    game_two = BattleshipModel(4, (3, 2), Random(15), 4)

    # player grid
    original_player_grid_game_two = list(game_two.grids()[0])
    
    with pytest.raises(AssertionError):
        game_two.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_two():
        game_two.shoot(0, 1)
        game_two.shoot(0, 2)
        game_two.shoot(1, 1)
        game_two.shoot(1, 2)
        game_two.shoot(2, 1)
        game_two.shoot(2, 2)
        game_two.shoot(2, 3)
        game_two.shoot(3, 0)
        game_two.shoot(3, 1)
        game_two.shoot(3, 2)
        game_two.shoot(3, 3)
    
    shoot_empty_cells_game_two()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_two == game_two.grids()[0]

    # shoot one of the ship
    game_two.shoot(1, 0)
    assert game_two.grids()[0] == ['a..B', 'a..B', 'a...', '....']
    # shooting it again/an empty cell should not make a difference
    game_two.shoot(0, 0)
    game_two.shoot(1, 0)
    game_two.shoot(2, 0)
    shoot_empty_cells_game_two()
    assert game_two.grids()[0] == ['a..B', 'a..B', 'a...', '....']

    # shoot the other ship
    game_two.shoot(0, 3)
    assert game_two.grids()[0] == ['a..b', 'a..b', 'a...', '....']

    # game is already over since the player has lost
    assert game_two.is_game_over()
    assert game_two.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_two.shoot(0, 0)
    with pytest.raises(AssertionError):
        game_two.shoot(1, 0)
    with pytest.raises(AssertionError):
        game_two.shoot(2, 0)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_one()


    # same grid, different cell to shoot
    game_three = BattleshipModel(4, (3, 2), Random(15), 4)

    # player grid
    original_player_grid_game_three = list(game_three.grids()[0])
    
    with pytest.raises(AssertionError):
        game_three.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_three():
        game_three.shoot(0, 1)
        game_three.shoot(0, 2)
        game_three.shoot(1, 1)
        game_three.shoot(1, 2)
        game_three.shoot(2, 1)
        game_three.shoot(2, 2)
        game_three.shoot(2, 3)
        game_three.shoot(3, 0)
        game_three.shoot(3, 1)
        game_three.shoot(3, 2)
        game_three.shoot(3, 3)
    
    shoot_empty_cells_game_three()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_three == game_three.grids()[0]

    # shoot one of the ship
    game_three.shoot(2, 0)
    assert game_three.grids()[0] == ['a..B', 'a..B', 'a...', '....']
    # shooting it again/an empty cell should not make a difference
    game_three.shoot(0, 0)
    game_three.shoot(1, 0)
    game_three.shoot(2, 0)
    shoot_empty_cells_game_three()
    assert game_three.grids()[0] == ['a..B', 'a..B', 'a...', '....']

    # shoot the other ship
    game_three.shoot(0, 3)
    assert game_three.grids()[0] == ['a..b', 'a..b', 'a...', '....']

    # game is already over since the player has lost
    assert game_three.is_game_over()
    assert game_three.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_three.shoot(0, 0)
    with pytest.raises(AssertionError):
        game_three.shoot(1, 0)
    with pytest.raises(AssertionError):
        game_three.shoot(2, 0)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_one()

def test_shooting_player_grid_two_horizontal():
    # both ships are horizontal
    game_one = BattleshipModel(4, (3, 2), Random(7), 4)

    # player grid
    original_player_grid_game_one = list(game_one.grids()[0])
    
    with pytest.raises(AssertionError):
        game_one.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_one():
        game_one.shoot(0, 2)
        game_one.shoot(0, 3)
        game_one.shoot(1, 3)
        game_one.shoot(2, 0)
        game_one.shoot(2, 1)
        game_one.shoot(2, 2)
        game_one.shoot(2, 3)
        game_one.shoot(3, 0)
        game_one.shoot(3, 1)
        game_one.shoot(3, 2)
        game_one.shoot(3, 3)
    
    shoot_empty_cells_game_one()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_one == game_one.grids()[0]

    # shoot one of the ship
    game_one.shoot(1, 0)
    assert game_one.grids()[0] == ['BB..', 'aaa.', '....', '....']
    # shooting it again/an empty cell should not make a difference
    game_one.shoot(1, 0)
    game_one.shoot(1, 1)
    game_one.shoot(1, 2)
    shoot_empty_cells_game_one()
    assert game_one.grids()[0] == ['BB..', 'aaa.', '....', '....']

    # shoot the other ship
    game_one.shoot(0, 0)
    assert game_one.grids()[0] == ['bb..', 'aaa.', '....', '....']

    # game is already over since the player has lost
    assert game_one.is_game_over()
    assert game_one.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_one.shoot(1, 0)
    with pytest.raises(AssertionError):
        game_one.shoot(1, 1)
    with pytest.raises(AssertionError):
        game_one.shoot(1, 2)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_one()


    # same grid, different cell to shoot
    game_two = BattleshipModel(4, (3, 2), Random(7), 4)

    # player grid
    original_player_grid_game_two = list(game_two.grids()[0])
    
    with pytest.raises(AssertionError):
        game_two.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_two():
        game_two.shoot(0, 2)
        game_two.shoot(0, 3)
        game_two.shoot(1, 3)
        game_two.shoot(2, 0)
        game_two.shoot(2, 1)
        game_two.shoot(2, 2)
        game_two.shoot(2, 3)
        game_two.shoot(3, 0)
        game_two.shoot(3, 1)
        game_two.shoot(3, 2)
        game_two.shoot(3, 3)
    
    shoot_empty_cells_game_two()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_two == game_two.grids()[0]

    # shoot one of the ship
    game_two.shoot(1, 1)
    assert game_two.grids()[0] == ['BB..', 'aaa.', '....', '....']
    # shooting it again/an empty cell should not make a difference
    game_two.shoot(1, 0)
    game_two.shoot(1, 1)
    game_two.shoot(1, 2)
    shoot_empty_cells_game_two()
    assert game_two.grids()[0] == ['BB..', 'aaa.', '....', '....']

    # shoot the other ship
    game_two.shoot(0, 0)
    assert game_two.grids()[0] == ['bb..', 'aaa.', '....', '....']

    # game is already over since the player has lost
    assert game_two.is_game_over()
    assert game_two.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_two.shoot(1, 0)
    with pytest.raises(AssertionError):
        game_two.shoot(1, 1)
    with pytest.raises(AssertionError):
        game_two.shoot(1, 2)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_one()


    # same grid, different cell to shoot
    game_three = BattleshipModel(4, (3, 2), Random(7), 4)

    # player grid
    original_player_grid_game_three = list(game_three.grids()[0])
    
    with pytest.raises(AssertionError):
        game_three.winner()

    # shoot empty locations with current target grid = 0
    def shoot_empty_cells_game_three():
        game_three.shoot(0, 2)
        game_three.shoot(0, 3)
        game_three.shoot(1, 3)
        game_three.shoot(2, 0)
        game_three.shoot(2, 1)
        game_three.shoot(2, 2)
        game_three.shoot(2, 3)
        game_three.shoot(3, 0)
        game_three.shoot(3, 1)
        game_three.shoot(3, 2)
        game_three.shoot(3, 3)
    
    shoot_empty_cells_game_three()

    # since those locations has no ship, no changes to the player's grid
    assert original_player_grid_game_three == game_three.grids()[0]

    # shoot one of the ship
    game_three.shoot(1, 2)
    assert game_three.grids()[0] == ['BB..', 'aaa.', '....', '....']
    # shooting it again/an empty cell should not make a difference
    game_three.shoot(1, 0)
    game_three.shoot(1, 1)
    game_three.shoot(1, 2)
    shoot_empty_cells_game_three()
    assert game_three.grids()[0] == ['BB..', 'aaa.', '....', '....']

    # shoot the other ship
    game_three.shoot(0, 0)
    assert game_three.grids()[0] == ['bb..', 'aaa.', '....', '....']

    # game is already over since the player has lost
    assert game_three.is_game_over()
    assert game_three.winner() != 0

    # shooting after the game is over will raise an assertion error
    with pytest.raises(AssertionError):
        game_three.shoot(1, 0)
    with pytest.raises(AssertionError):
        game_three.shoot(1, 1)
    with pytest.raises(AssertionError):
        game_three.shoot(1, 2)
    with pytest.raises(AssertionError):
        shoot_empty_cells_game_one()

# test for shoot where the player wins
def test_shooting_player_wins():
    game_one = BattleshipModel(4, (3, 2), Random(0), 4)

    # shoots all of Bot 1 ships
    game_one.target = 1
    assert game_one.grids()[game_one.target] == ['????', '????', '????', '????']
    game_one.shoot(2, 1)
    # shoot empty cell
    game_one.shoot(0, 0)
    assert game_one.grids()[game_one.target] == ['.???', '????', '?b??', '????']
    assert game_one.players()[game_one.target].are_there_ships_remaining()
    game_one.shoot(3, 1)
    assert game_one.grids()[game_one.target] == ['.???', '????', '?b??', '?a??']
    assert not game_one.players()[game_one.target].are_there_ships_remaining()
    assert not game_one.is_game_over()

    # shoots all of Bot 2 ships
    game_one.target = 2
    assert game_one.grids()[game_one.target] == ['????', '????', '????', '????']
    game_one.shoot(1, 1)
    assert game_one.grids()[game_one.target] == ['????', '?a??', '????', '????']
    assert game_one.players()[game_one.target].are_there_ships_remaining()
    game_one.shoot(2, 0)
    assert game_one.grids()[game_one.target] == ['????', '?a??', 'b???', '????']
    assert not game_one.players()[game_one.target].are_there_ships_remaining()
    assert not game_one.is_game_over()

    # shoots all of Bot 3 ships
    game_one.target = 3
    assert game_one.grids()[game_one.target] == ['????', '????', '????', '????']
    game_one.shoot(0, 1)
    assert game_one.grids()[game_one.target] == ['?a??', '????', '????', '????']
    assert game_one.players()[game_one.target].are_there_ships_remaining()
    game_one.shoot(3, 1)
    assert game_one.grids()[game_one.target] == ['?a??', '????', '????', '?b??']
    assert not game_one.players()[game_one.target].are_there_ships_remaining()
    assert not game_one.is_game_over()

    # shoots all of Bot 4 ships
    game_one.target = 4
    assert game_one.grids()[game_one.target] == ['????', '????', '????', '????']
    game_one.shoot(1, 0)
    assert game_one.grids()[game_one.target] == ['????', 'a???', '????', '????']
    assert game_one.players()[game_one.target].are_there_ships_remaining()
    game_one.shoot(0, 2)
    assert game_one.grids()[game_one.target] == ['??b?', 'a???', '????', '????']
    assert not game_one.players()[game_one.target].are_there_ships_remaining()
    
    # game already over (since all of the bot ships are sunken while the player still have at least one ship)
    assert game_one.players()[0].are_there_ships_remaining()
    assert game_one.is_game_over()
    assert game_one.winner() == 0

# TESTS FOR square_scan()
def test_scan():
    game_one = BattleshipModel(10, (3, 2), Random(0), 5)

    # Scan Bot 1 (scan top left corner)
    assert game_one.grids()[1] == ['??????????', '??????????', '??????????', '??????????', '??????????', \
                                    '??????????', '??????????', '??????????', '??????????', '??????????']
    game_one.square_scan(0, 0, 1)
    assert game_one.grids()[1] == ['.....?????', '.....?????', '.....?????', '.....?????', '.....?????', \
                                    '??????????', '??????????', '??????????', '??????????', '??????????']
    assert game_one.players()[0].remaining_square_scan() == 2

    # Scan Bot 1 (scan half left corner)
    game_one.square_scan(5, 0, 1)
    assert game_one.grids()[1] == ['.....?????', '.....?????', '.....?????', '.....?????', '.....?????', \
                                    '.....?????', '...AA?????', '..BB.?????', '.....?????', '.....?????']
    assert game_one.players()[0].remaining_square_scan() == 1

    # Bot 1 moves a ship with a hidden part, revealing the whole ship (A)
    game_one.go_to_next_turn()
    assert game_one.turn == 1
    assert game_one.get_ships_that_can_move() != dict()
    (i, j), _ = game_one.get_random_ship_that_can_move()
    game_one.move_ship(i, j, -1)
    assert game_one.players()[game_one.turn].remaining_move_ship() == 2
    assert game_one.grids()[1] == ['.....?????', '.....?????', '.....?????', '.....?????', '.....?????', \
                                    '.....?????', '..AAA?????', '..BB.?????', '.....?????', '.....?????']

    # Scan Bot 1 (scan at half row, half column)
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    assert game_one.turn == 0
    game_one.square_scan(5, 5, 1)
    assert game_one.grids()[1] == ['.....?????', '.....?????', '.....?????', '.....?????', '.....?????', \
                                    '..........', '..AAA.....', '..BB......', '..........', '..........']
    assert game_one.players()[0].remaining_square_scan() == 0

    # tries to scan again but already out of scan
    with pytest.raises(AssertionError):
        game_one.square_scan(0, 0, 1)


    # try to scan where the square will go out of bounds
    game_two = BattleshipModel(10, (3, 2), Random(0), 5)

    # Scan Bot 1 (scan top right corner)
    assert game_two.grids()[1] == ['??????????', '??????????', '??????????', '??????????', '??????????', \
                                    '??????????', '??????????', '??????????', '??????????', '??????????']
    game_two.square_scan(0, 9, 1)
    assert game_two.players()[game_two.turn].remaining_square_scan() == 2
    assert game_two.grids()[1] == ['?????????.', '?????????.', '?????????.', '?????????.', '?????????.', \
                                    '??????????', '??????????', '??????????', '??????????', '??????????']

    # Scan Bot 1 (scan bottom left corner)
    game_two.square_scan(9, 0, 1)
    assert game_two.players()[game_two.turn].remaining_square_scan() == 1
    assert game_two.grids()[1] == ['?????????.', '?????????.', '?????????.', '?????????.', '?????????.', \
                                    '??????????', '??????????', '??????????', '??????????', '.....?????']

    # Scan Bot 1 (scan bottom, half column)
    game_two.square_scan(9, 5, 1)
    assert game_two.players()[game_two.turn].remaining_square_scan() == 0
    assert game_two.grids()[1] == ['?????????.', '?????????.', '?????????.', '?????????.', '?????????.', \
                                    '??????????', '??????????', '??????????', '??????????', '..........']


# TESTS FOR move_ship()
def test_move_ship():
    game_one = BattleshipModel(10, (3, 2), Random(0), 10)

    # Move a vertical ship (Bot 2)
    # Scan the whole grid of Bot 2 first
    game_one.square_scan(0, 0, 2)
    assert game_one.players()[game_one.turn].remaining_square_scan() == 2
    assert game_one.grids()[2] == ['..........', '..........', '..........', '..........', '..........', \
                                    '..........', '....B.....', '....B.....', '..........', '..AAA.....']
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    # Make B move
    assert game_one.turn == 2
    assert game_one.get_ships_that_can_move() != dict()
    # since Random(0) will yield the same results, get_random_ship_that_can_move is called a few times to get the desired i and j
    game_one.get_random_ship_that_can_move()
    game_one.get_random_ship_that_can_move()
    (i, j), _ = game_one.get_random_ship_that_can_move()
    # move ship downwards
    game_one.move_ship(i, j, -1)
    assert game_one.players()[game_one.turn].remaining_move_ship() == 2
    assert game_one.grids()[2] == ['..........', '..........', '..........', '..........', '..........', \
                                    '..........', '..........', '....B.....', '....B.....', '..AAA.....']
    # move ship upwards twice
    game_one.get_random_ship_that_can_move()
    (i, j), _ = game_one.get_random_ship_that_can_move()
    game_one.move_ship(i, j, 1)
    assert game_one.players()[game_one.turn].remaining_move_ship() == 1
    assert game_one.grids()[2] == ['..........', '..........', '..........', '..........', '..........', \
                                    '..........', '....B.....', '....B.....', '..........', '..AAA.....']
    game_one.get_random_ship_that_can_move()
    game_one.get_random_ship_that_can_move()
    (i, j), _ = game_one.get_random_ship_that_can_move()
    game_one.move_ship(i, j, 1)
    assert game_one.players()[game_one.turn].remaining_move_ship() == 0
    assert game_one.grids()[2] == ['..........', '..........', '..........', '..........', '..........', \
                                    '....B.....', '....B.....', '..........', '..........', '..AAA.....']


    # Move a horizontal ship (Bot 4)
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    assert game_one.turn == 0
    # Scan the whole grid of Bot 2 first
    game_one.square_scan(0, 0, 4)
    assert game_one.players()[game_one.turn].remaining_square_scan() == 1
    assert game_one.grids()[4] == ['..........', '..........', '..........', '.........B', '.........B', \
                                    '..........', '..........', '..........', '....AAA...', '..........']
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    game_one.go_to_next_turn()
    # Make A move
    assert game_one.turn == 4
    assert game_one.get_ships_that_can_move() != dict()
    (i, j), _ = game_one.get_random_ship_that_can_move()
    # move ship leftwards
    game_one.move_ship(i, j, -1)
    assert game_one.players()[game_one.turn].remaining_move_ship() == 2 
    assert game_one.grids()[4] == ['..........', '..........', '..........', '.........B', '.........B', \
                                    '..........', '..........', '..........', '...AAA....', '..........']
    # move ship rightwards
    game_one.get_random_ship_that_can_move()
    game_one.get_random_ship_that_can_move()
    (i, j), _ = game_one.get_random_ship_that_can_move()
    game_one.move_ship(i, j, 1)
    assert game_one.players()[game_one.turn].remaining_move_ship() == 1 
    assert game_one.grids()[4] == ['..........', '..........', '..........', '.........B', '.........B', \
                                    '..........', '..........', '..........', '....AAA...', '..........']
    game_one.get_random_ship_that_can_move()
    game_one.get_random_ship_that_can_move()
    (i, j), _ = game_one.get_random_ship_that_can_move()
    game_one.move_ship(i, j, 1)
    assert game_one.players()[game_one.turn].remaining_move_ship() == 0
    assert game_one.grids()[4] == ['..........', '..........', '..........', '.........B', '.........B', \
                                    '..........', '..........', '..........', '.....AAA..', '..........']

# TESTS FOR getting a random move for the bot
def test_randomness_validity():
    game_one = BattleshipModel(10, (3, 2), Random(0), 5)

    game_one.go_to_next_turn()
    assert game_one.turn == 1

    # case where move == 1
    move = game_one.get_random_move()
    target = 0
    game_one.target = target

    i, j = game_one.get_random_ij()
    direction = 0
    assert direction == 0

    assert move in (1, 3)
    assert 0 <= i < game_one.n
    assert 0 <= j < game_one.n
    assert direction in (-1, 0, 1)

    # case where move == 3
    move = game_one.get_random_move()
    target = 0
    game_one.target = target

    (i, j), direction_to_choose = game_one.get_random_ship_that_can_move()
    direction = game_one.get_random_direction(direction_to_choose)
    assert direction in (-1, 1)

    assert move in (1, 3)
    assert 0 <= i < game_one.n
    assert 0 <= j < game_one.n
    assert direction in (-1, 0, 1)

    # case where the Bot 1 cant move a ship
    game_one = BattleshipModel(4, (3, 3, 2, 2), Random(1), 5)

    game_one.go_to_next_turn()
    # move is always 1
    move = game_one.get_random_move()
    target = 0
    game_one.target = target

    i, j = game_one.get_random_ij()
    direction = 0
    assert direction == 0

    assert move in (1, 3)
    assert 0 <= i < game_one.n
    assert 0 <= j < game_one.n
    assert direction in (-1, 0, 1)


# TESTS FOR making sure that the ship that the player will choose to move is able to move
def test_for_player_wanting_to_move_a_ship():
    game_one = BattleshipModel(4, (3, 2), Random(0), 4)
    
    # the info presented to the player is if they can move a ship or not, 
    # if they can't, 3 cannot be chosen (see BattleshipView/Controller)
    # Upon asking for a ship to move, the view class requires the 
    # orientation of the ships and the ships that can move
    # The view class will make sure that the player will choose a ship that can move, resulting to ship_type

    # Therefore, we only have to assert that the orientation for each ship exists
    orientations = game_one.get_ship_orientation()
    assert len(orientations) == len(game_one.ship_sizes)
    for ship in orientations:
        assert orientations[ship] in "VH"

    # and that the i and j coordinates of the ship are within bounds 
    # (using get_location_of_ships_that_can_move(ship_type))
    ships_that_can_move = game_one.get_ships_that_can_move()
    for ship in ships_that_can_move:
        i, j = game_one.get_location_of_ships_that_can_move(ship)
        assert 0 <= i < game_one.n
        assert 0 <= j < game_one.n

    # since direction will always be valid (as seen in view class, we do not have to assert direction)