from src.commands import c_exit_game
from src.game import Game
from src.ui import MainUI
from src.player import playerObject
from src.rooms.sets import room_init

if __name__ == "__main__":
    try:
        Game()\
            .initialize_all_commands() \
            .set_current_interface(MainUI) \
            .set_current_room(room_init) \
            .set_player(playerObject) \
            .run()
    except KeyboardInterrupt:
        c_exit_game()