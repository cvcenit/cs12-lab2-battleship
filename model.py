# pyright: strict
from random import Random
from utils import generate_grid
from collections.abc import Sequence

grid_type = list[list[str]]

class Player:
    def __init__(self, n: int, grid: grid_type, ship_sizes: Sequence[int]):
        self._grid: grid_type = grid
        self.n = n
        self.ship_sizes: Sequence[int] = ship_sizes
        self._ship_types: str = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:len(self.ship_sizes)]

        self._remaining_move_ship = 3
        self._remaining_square_scan = 3
        self._remaining_ships_amount: int = len(ship_sizes)
        self._revealed_cells: set[tuple[int, int]] = set()

        self._remaining_ships_location: \
        dict[str, list[tuple[int, int]]] = self._find_initial_ship_positions()

        self._ships_and_their_orientation: dict[str, str] = \
        dict((ship_type, self.ship_orientation(ship_type)) for ship_type in self._ship_types)

        self._ships_and_directions_they_can_move_to: \
        dict[str, tuple[()] | tuple[int] | tuple[int, int]] = self._get_ships_and_directions_they_can_move_to()

    def grid(self) -> grid_type:
        return self._grid


    # Functions concerning ship locations/orientations/directions
    def are_there_ships_remaining(self) -> bool:
        return self._remaining_ships_amount > 0

    def remaining_ships_location(self) -> dict[str, list[tuple[int, int]]]:
        return self._remaining_ships_location

    def ships_and_their_orientation(self) -> dict[str, str]:
        return self._ships_and_their_orientation

    def ships_and_directions_they_can_move_to(self) -> dict[str, tuple[()] | tuple[int] | tuple[int, int]]:
        return self._ships_and_directions_they_can_move_to

    def ship_orientation(self, ship_type: str) -> str:
        i, j = self.remaining_ships_location()[ship_type][0]
        return "H" if self._other_parts_on_side(self._grid, i, j) else "V"

    def _get_ships_and_directions_they_can_move_to(self) -> dict[str, tuple[()] | tuple[int] | tuple[int, int]]:
        ships = self._remaining_ships_location
        result: dict[str, tuple[()] | tuple[int] | tuple[int, int]] = {}
        for ship in ships:
            location = ships[ship]
            i, j = location[0]

            available_directions: tuple[()] | tuple[int] | tuple[int, int] = ()
            if (self._ship_can_move_to_left_bottom(i, j) and self._ship_can_move_to_right_top(i, j)):
                available_directions = (-1, 1)
            elif self._ship_can_move_to_left_bottom(i, j):
                available_directions = (-1,)
            elif self._ship_can_move_to_right_top(i, j):
                available_directions = (1,)
            else:
                available_directions = ()
            result[ship] = available_directions
        return result

    def _find_initial_ship_positions(self) -> dict[str, list[tuple[int, int]]]:
        n = self.n
        grid = self._grid
        result: dict[str, list[tuple[int, int]]] = dict((ship, list()) for ship in self._ship_types)
        for i in range(n):
            for j in range(n):
                if grid[i][j] in self._ship_types:
                    result[grid[i][j]].append((i, j))
        return result


    # Functions concerning moving a ship
    def remaining_move_ship(self) -> int:
        return self._remaining_move_ship

    def use_move_ship(self, i: int, j: int, direction: int):
        assert self.remaining_move_ship() > 0

        if self._other_parts_on_side(self._grid, i, j):
            self._move_ship_horizontally(i, j, direction)
        else:
            self._move_ship_vertically(i, j, direction)

        self._remaining_move_ship -= 1

    def can_move_ship(self) -> bool:
        return self.remaining_move_ship() > 0 and not self._all_ships_cant_move()

    def _update_ship_locations(self, ship_type: str, remove: tuple[int, int], add: tuple[int, int]):
        remaining_ships_locations = self._remaining_ships_location

        remaining_ships_locations[ship_type].remove(remove)
        remaining_ships_locations[ship_type].append(add)

    def _update_ships_and_directions_they_can_move_to(self):
        self._ships_and_directions_they_can_move_to = self._get_ships_and_directions_they_can_move_to()

    def _ship_can_move_to_right_top(self, i: int, j: int) -> bool:
        n = self.n
        if self._other_parts_on_side(self._grid, i, j):
            j_to_right = self._find_right_most_part(i, j) + 1
            if 0 <= j_to_right < n:
                return not (self.ships_broken_and_not_was_in(i, j_to_right))
            else:
                return False
        else:
            i_to_top = self._find_top_most_part(i, j) - 1
            if 0 <= i_to_top < n:
                return not (self.ships_broken_and_not_was_in(i_to_top, j))
            else:
                return False

    def _ship_can_move_to_left_bottom(self, i: int, j: int) -> bool:
        n = self.n
        if self._other_parts_on_side(self._grid, i, j):
            j_to_left = self._find_left_most_part(i, j) - 1
            if 0 <= j_to_left < n:
                return not (self.ships_broken_and_not_was_in(i, j_to_left))
            else:
                return False
        else:
            i_to_bottom = self._find_bottom_most_part(i, j) + 1
            if 0 <= i_to_bottom < n:
                return not (self.ships_broken_and_not_was_in(i_to_bottom, j))
            else:
                return False

    def _all_ships_cant_move(self) -> bool:
        ships = self._ships_and_directions_they_can_move_to
        for ship in ships:
            if ships[ship]:
                return False
        return True

    def _move_ship_horizontally(self, i: int, j: int, direction: int):
        leftmost = self._find_left_most_part(i, j)
        rightmost = self._find_right_most_part(i, j)

        if direction == -1:
            self._update_ship_locations(self._grid[i][j], (i, rightmost), (i, leftmost + direction))
            self._grid[i][leftmost + direction] = self._grid[i][j]
            self._grid[i][rightmost] = "."
        else:
            self._update_ship_locations(self._grid[i][j], (i, leftmost), (i, rightmost + direction))
            self._grid[i][rightmost + direction] = self._grid[i][j]
            self._grid[i][leftmost] = "."
        self._update_ships_and_directions_they_can_move_to()
    
    def _find_left_most_part(self, i: int, j: int) -> int:
        return (''.join(self._grid[i])).find(self._grid[i][j])

    def _find_right_most_part(self, i: int, j: int) -> int:
        return (''.join(self._grid[i])).rfind(self._grid[i][j])

    def _move_ship_vertically(self, i: int, j: int, direction: int):
        topmost = self._find_top_most_part(i, j)
        botmost = self._find_bottom_most_part(i, j)
        
        if direction == 1:
            self._update_ship_locations(self._grid[i][j], (botmost, j), (topmost - direction, j))
            self._grid[topmost - direction][j] = self._grid[i][j]
            self._grid[botmost][j] = "."
        else:
            self._update_ship_locations(self._grid[i][j], (topmost, j), (botmost - direction, j))
            self._grid[botmost - direction][j] = self._grid[i][j]
            self._grid[topmost][j] = "."
        self._update_ships_and_directions_they_can_move_to()
    
    def _find_top_most_part(self, i: int, j: int) -> int:
        result: list[str] = []
        for row in self._grid:
            result += [row[j]]
        return (''.join(result)).find(self._grid[i][j])

    def _find_bottom_most_part(self, i: int, j: int) -> int:
        result: list[str] = []
        for row in self._grid:
            result += [row[j]]
        return (''.join(result)).rfind(self._grid[i][j])


    # Functions for square scan
    def remaining_square_scan(self) -> int:
        return self._remaining_square_scan
    
    def use_square_scan(self):
        assert self.remaining_square_scan() > 0
        self._remaining_square_scan -= 1

    def revealed_cells(self) -> set[tuple[int, int]]:
        return self._revealed_cells

    def reveal_cell(self, i: int, j: int):
        self._revealed_cells.add((i, j))


    # Function for destroying a ship
    def destroy_ship(self, i: int, j: int):
        '''Destroys the target ship part by part'''
        grid_to_shoot = self._grid
        grid_to_shoot[i][j] = grid_to_shoot[i][j].lower()
        ship_type = grid_to_shoot[i][j]
        possible_cells = set("ABCDabcd.") - set((ship_type.upper(),))

        # check if other parts of the ship is on the side
        if self._other_parts_on_side(grid_to_shoot, i, j):
            # check to the right
            for dagdag in range(1, 1 + max(self.ship_sizes)):
                if j + dagdag >= self.n:
                    continue
                elif grid_to_shoot[i][j + dagdag] in possible_cells:
                    continue
                else:
                    grid_to_shoot[i][j + dagdag] = ship_type
            # check to the left
            for bawas in range(1, 1 + max(self.ship_sizes)):
                if j - bawas <= -1:
                    continue
                elif grid_to_shoot[i][j - bawas] in possible_cells:
                    continue
                else:
                    grid_to_shoot[i][j - bawas] = ship_type
        else:
            # check below
            for dagdag in range(1, 1 + max(self.ship_sizes)):
                if i + dagdag >= self.n:
                    continue
                elif grid_to_shoot[i + dagdag][j] in possible_cells:
                    continue
                else:
                    grid_to_shoot[i + dagdag][j] = ship_type
            # check above
            for bawas in range(1, 1 + max(self.ship_sizes)):
                if i - bawas <= -1:
                    continue
                elif grid_to_shoot[i - bawas][j] in possible_cells:
                    continue
                else:
                    grid_to_shoot[i - bawas][j] = ship_type

        self._remaining_ships_location.pop(ship_type.upper())
        self._ships_and_directions_they_can_move_to.pop(ship_type.upper())
        self._remaining_ships_amount -= 1


    # Functions that are used by almost everything
    def ship_was_in(self, i: int, j: int) -> bool:
        return self._grid[i][j] in self._ship_types

    def ships_broken_and_not_was_in(self, i: int, j: int) -> bool:
        return self._grid[i][j] in (set(self._ship_types) | set(self._ship_types.lower()))

    def _other_parts_on_side(self, grid: grid_type, i: int, j: int) -> bool:
        ship_type = grid[i][j].upper()
        # consider corners, edges
        if j == 0:
            return ship_type == grid[i][j + 1]
        elif j == self.n - 1:
            return ship_type == grid[i][j - 1]
        else:
            return ship_type == grid[i][j + 1] or ship_type == grid[i][j - 1]



class BattleshipModel:
    def __init__(self, n: int, ship_sizes: Sequence[int], rng: Random, k: int) -> None:
        self.n: int = n
        self.ship_sizes: Sequence[int] = ship_sizes
        self.rng: Random = rng
        self.k: int = k
        self.turn: int = 0
        self.target: int = 0

        self._shot_cells: set[tuple[int, int]] = set()
        self._is_game_over: bool = False
        self._winner: int = -1
        self.enemy_count: int = 4

        # generates players, with the first being the player and the rest the (4) bots
        self._players: Sequence[Player] = [Player(self.n, generate_grid(self.n, self.ship_sizes, self.rng), self.ship_sizes) for _ in range(self.enemy_count + 1)]

    def is_game_over(self) -> bool:
        return self._is_game_over

    def players(self) -> Sequence[Player]:
        return self._players

    def get_ship_orientation(self) -> dict[str, str]:
        return self._players[self.turn].ships_and_their_orientation()

    def grids(self) -> Sequence[Sequence[str]]:
        return (self._your_grid(), *self._opponent_grids())

    def _your_grid(self) -> Sequence[str]:
        you = self._players[0].grid()
        you_str: list[str] = []

        for row in you:
            you_str += [''.join(row)]

        return you_str

    def _opponent_grids(self) -> Sequence[Sequence[str]]:
        opponents = [player for player in self._players[1:]]
        opponent_grids: list[list[str]] = []

        for opponent in opponents:
            opponent_grids += [self._mask_grid(opponent)]

        return opponent_grids

    def _mask_grid(self, target: Player) -> list[str]:
        grid_string: list[str] = []
        grid_to_mask = target.grid()

        for i in range(len(grid_to_mask)):
            row_list_of_string: list[str] = []
            for j in range(len(grid_to_mask[i])):
                cell = grid_to_mask[i][j]
                row_list_of_string += [cell] if self._is_revealed(i, j, target) else ['?']
            grid_string += [''.join(row_list_of_string)]

        return grid_string

    def _is_revealed(self, i: int, j: int, target: Player) -> bool:
        return (i, j) in target.revealed_cells()

    def winner(self) -> int:
        assert self.is_game_over()
        return self._winner
    
    def go_to_next_turn(self) -> None:
        self.turn += 1
        self.turn %= self.enemy_count + 1

    def get_random_ij(self) -> tuple[int, int]:
        return (self.rng.randint(0, self.n - 1), self.rng.randint(0, self.n - 1))

    def get_random_move(self) -> int:
        current_player = self._players[self.turn]
        if current_player.can_move_ship() and current_player.are_there_ships_remaining():
            choices = (1, 3)
        elif current_player.are_there_ships_remaining():
            choices = (1,)
        else:
            return 0
        return self.rng.choice(choices)

    def get_random_direction(self, directions_to_choose: tuple[()] | tuple[int] | tuple[int, int]) -> int:
        return self.rng.choice(directions_to_choose)

    def get_random_ship_that_can_move(self) -> tuple[tuple[int, int], tuple[()] | tuple[int] | tuple[int, int]]:
        current_player = self.players()[self.turn]
        ships = current_player.ships_and_directions_they_can_move_to()

        # choose from ships that can move
        valid_ships = list((ship, ships[ship]) for ship in ships if ships[ship])
        ship_type, available_directions = self.rng.choice(valid_ships)

        # get the i, j and available direction of the ship
        location_of_chosen_ship = current_player.remaining_ships_location()[ship_type]
        chosen_location = self.rng.choice(location_of_chosen_ship)

        return chosen_location, available_directions

    def get_ships_that_can_move(self) -> dict[str, tuple[()] | tuple[int] | tuple[int, int]]:
        return self.players()[self.turn].ships_and_directions_they_can_move_to()

    def shoot(self, i: int, j: int):
        # checks if the game is already won or lost
        assert not self.is_game_over()
        assert self.players()[self.turn].are_there_ships_remaining()

        player_to_shoot = self._players[self.target]
        if player_to_shoot.ship_was_in(i, j):
            player_to_shoot.destroy_ship(i, j)
        player_to_shoot.reveal_cell(i, j)

        if not self._players[0].are_there_ships_remaining():
            self._is_game_over = True
            self._winner = -1
            return
        if self._all_bots_have_no_more_ships():
            self._is_game_over = True
            self._winner = 0
            return

    def _all_bots_have_no_more_ships(self) -> bool:
        bots = self.players()[1:]
        bots_remaining_ships: list[bool] = []
        for bot in bots:
            bots_remaining_ships += [not bot.are_there_ships_remaining()]
        return all(bots_remaining_ships)

    def square_scan(self, i: int, j: int, target: int):
        k = self.k
        n = self.n
        for _i in range(k):
            resultant_i = _i + i
            if not (0 <= resultant_i < n):
                break
            for _j in range(k):
                resultant_j = _j + j
                if not (0 <= resultant_j < n):
                    break
                self._players[target].reveal_cell((_i + i), (_j + j))
        self._players[self.turn].use_square_scan()

    def move_ship(self, i: int, j: int, direction: int):
        self._players[self.turn].use_move_ship(i, j, direction)

    def get_location_of_ships_that_can_move(self, ship_type: str) -> tuple[int, int]:
        return self.players()[self.turn].remaining_ships_location()[ship_type][0]