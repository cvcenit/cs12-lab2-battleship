# pyright: strict

from __future__ import annotations

from collections.abc import Sequence
from random import Random, seed
from model import BattleshipModel


grid_type = Sequence[Sequence[str]]

class BattleshipView:
    def show_grids(self, grids: Sequence[Sequence[str]]):
        for rows in zip(*grids, strict=True):
            print(*rows, sep="\t")
        print()

    def ask_for_location(self, n: int) -> tuple[int, int]:
        i, j = -1, -1

        while not 0 <= i < n:
            try:
                i = int(input(f"Choose a row    [0-{n-1}]: "))
            except KeyboardInterrupt:
                print()
                exit()
            except:
                ...

        while not 0 <= j < n:
            try:
                j = int(input(f"Choose a column [0-{n-1}]: "))
            except KeyboardInterrupt:
                print()
                exit()
            except:
                ...

        print()
        return i, j

    def ask_for_ship(self, n: int, ships: dict[str, tuple[()] | tuple[int] | tuple[int, int]], ships_orientation: dict[str, str]) -> str:
        choice: str = ""
        ships_that_can_move: tuple[str, ...] = tuple(ship for ship in ships if ships[ship])

        while not (choice in ships_that_can_move):
            try:
                up, down, left, right = "Upwards", "Downwards", "Leftwards", "Rightwards"

                formatted_strings: list[str] = list()
                for ship in ships:
                    if ships_orientation[ship] == "H":
                        formatted: str = f"[{ship}]: {f"[{left}] " if -1 in ships[ship] else ""}{f"[{right}]" if 1 in ships[ship] else ""} {"Can't move" if not ships[ship] else ""}"
                    else:
                        formatted: str = f"[{ship}]: {f"[{down}] " if -1 in ships[ship] else ""}{f"[{up}]" if 1 in ships[ship] else ""} {"Can't move" if not ships[ship] else ""}"  
                    formatted_strings += [formatted]
                print(f"""
Please choose a ship that can move
{'\n'.join(formatted_strings)}
""")
                choice = (input(f"Choose a ship: ")).upper()
            except KeyboardInterrupt:
                print()
                exit()
            except:
                ...

        print()
        return choice

    def ask_for_target(self, bot_number: int) -> int:
        target = -1

        while not 1 <= target < bot_number:
            try:
                target = int(input(f"Choose an enemy [1-{bot_number-1}]: "))
            except KeyboardInterrupt:
                print()
                exit()
            except:
                ...
        return target

    def ask_for_move(self, remaining_scans: int, remaining_moves: int, can_move_a_ship: bool) -> int:
        move = -1
        choices = (1, 2, 3) if can_move_a_ship else (1, 2)

        while not move in choices:
            try:
                print(f"""
[1] Shoot
[2] Square Scan ({remaining_scans} left)
[3] Move Ship ({remaining_moves} left) {"(Can't currently move a ship)" if not can_move_a_ship else ""}
""")
                move = int(input(f"Choose your move: "))
                if move == 2 and remaining_scans == 0 or move == 3 and remaining_moves == 0:
                    raise ValueError
            except KeyboardInterrupt:
                print()
                exit()
            except:
                ...

        return move

    def ask_for_n(self) -> int:
        n = -1

        while not 6 <= n <= 67:
            try:
                n = int(input("Choose a row (and column) size (6 - 67): "))
            except KeyboardInterrupt:
                print()
                exit()
            except:
                ...

        return n

    def ask_for_k(self, n: int) -> int:
        k = -1

        while not 1 <= k <= n:
            try:
                k = int(input(f"Choose the square scan's side length (1 to {n}) : "))
            except KeyboardInterrupt:
                print()
                exit()
            except:
                ...

        return k

    def ask_for_direction(self, ship_type: str, ships: dict[str, tuple[()] | tuple[int] | tuple[int, int]]) -> int:
        direction = 0
        available_direction = ships[ship_type]

        while not (direction in available_direction):
            try:
                direction = int(input(f"Choose direction [1 if upwards/rightwards, -1 otherwise]: "))
            except KeyboardInterrupt:
                print()
                exit()
            except:
                ...
        return direction

    def show_target(self, bot_number: int, target_number: int):
        if target_number == 0:
            print(f"Bot {bot_number} shot you!")
        else:
            print(f"Bot {bot_number} shot Bot {target_number}!")

    def show_shot(self, i: int, j: int):
        print(f"({i},{j}) was shot.")
        print()

    def show_end_message(self, winner: int):
        if winner == 0:
            print("You win!")
        else:
            print("You lose...")
        print()

    def say_ship_moved(self, bot_number: int):
        print(f"Bot {bot_number} moved a ship!")
        print()

class BattleshipController:
    def __init__(self, model: BattleshipModel, view: BattleshipView):
        self._model = model
        self._view = view

    def run(self):
        model = self._model
        view = self._view

        while not model.is_game_over():
            current_player = model.players()[model.turn]
            if model.turn == 0:
                view.show_grids(model.grids())

                player_remaining_scans = current_player.remaining_square_scan()
                player_remaining_move_ship = current_player.remaining_move_ship()
                can_move_a_ship = current_player.can_move_ship()
                move = view.ask_for_move(player_remaining_scans, player_remaining_move_ship, can_move_a_ship)

                if move != 3:
                    target = view.ask_for_target(model.enemy_count + 1)
                    model.target = target
                    i, j = view.ask_for_location(model.n)
                    ship_type = "0"
                else:
                    ship_type = view.ask_for_ship(model.n, model.get_ships_that_can_move(), model.get_ship_orientation())
                    i, j = model.get_location_of_ships_that_can_move(ship_type)
                    target = 0
                direction = view.ask_for_direction(ship_type, model.get_ships_that_can_move()) if move == 3 else 0

            else:
                target = 0
                model.target = target
                move = model.get_random_move()

                if move == 3:
                    (i, j), direction_to_choose = model.get_random_ship_that_can_move()
                    direction = model.get_random_direction(direction_to_choose)
                else:
                    i, j = model.get_random_ij()
                    direction = 0

                if move == 1:
                    view.show_target(model.turn, target)
                    view.show_shot(i, j)
                else:
                    view.say_ship_moved(model.turn)

            match move:
                case 1:
                    model.shoot(i, j)
                case 2:
                    model.square_scan(i, j, target)
                case 3:
                    model.move_ship(i, j, direction)
                case _:
                    raise ValueError

            model.go_to_next_turn()

        view.show_grids(model.grids())
        view.show_end_message(model.winner())

if __name__ == "__main__":
    game_view = BattleshipView()
    game_n = game_view.ask_for_n()
    game_k = game_view.ask_for_k(game_n)
    game_model = BattleshipModel(game_n, (4, 3, 2, 2), Random(seed()), game_k)
    game = BattleshipController(game_model, game_view)
    game.run()