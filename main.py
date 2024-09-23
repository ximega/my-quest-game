from src.classes.entities import Player
from src.classes.crafting import Machine
from src.classes.enchants import Enchant
from src.commands import *
import src.commands
from src.ui import *
from src.player import playerObject
from settings.default import (
    MAX_HEALTH, 
    MAX_PROJECTILE_PROTECTION, 
    MAX_PROTECTION, 
    MAX_SUBPROTECTION,
    MAX_DAMAGE,
    AUTO_SAVE
)
from src.rooms.sets import *




ALL_COMMANDS = list(filter(lambda x: x.startswith('c_'), dir(src.commands)))



def main() -> None: 
    current_interface = MainUI
    current_room = room_init
    player = playerObject

    while True:            
        if current_interface is MainUI:        
            current_interface.update_section(
                'player_main_info',
                
                f'Health: {player.health}/{MAX_HEALTH} ({str_format_health_level(player.health, MAX_HEALTH)})\nProtection: {player.protection} ({str_format_protection_level(player.protection, MAX_PROTECTION)})\nSubprotection: {player.subprotection} ({str_format_protection_level(player.subprotection, MAX_SUBPROTECTION)})\nProtection: {player.projectile_protection} ({str_format_protection_level(player.projectile_protection, MAX_PROJECTILE_PROTECTION)})\nDamage: {player.damage} ({str_format_damage_level(player.damage, MAX_DAMAGE)})'
            )
            
            current_interface.update_section(
                'player_add_info',
                
                f'Nutrition: {int(player.nutrition * 100)}%\nGold coins: {player.gold_coins}\nMinis count: {len(player.minis)}'
            )
            
            current_interface.update_section(
                'player_active_inv',
                
                player.get_active_items()
            )
        
        print(current_interface.show())
        
        commands: list[str] = input('\n$: ').split(' ')
        
        response = None

        # take damage if there is mobs in the room
        opp_damage_response = r_command_exc(c_opponent_damage, *commands[1:], current_room = current_room, player = player)

        if isinstance(opp_damage_response, tuple):
            response, player = opp_damage_response
        elif isinstance(opp_damage_response, Response):
            response = opp_damage_response
        else:
            raise TypeError(f'Unrecognized type of {type(opp_damage_response)}, with value {opp_damage_response}')
        
        match commands[0]:
            case 'debug':
                response = r_command_exc(c_debug, *commands[1:], all_commands = ALL_COMMANDS, current_room = current_room)
            
            case 'exit':
                if AUTO_SAVE:
                    response = Response("You can't temporarily set AUTO_SAVE to True, since implementation is not done")
                    c_save_game()
                
                c_exit_game()
            
            case 'save':
                # TODO: implement it later, 
                # now i have more 
                # interesting stuff to deal with :nyam-nyam:
                # temporarily raises TemporarilyInaccessableCommand
                response = Response("You can't temporarily use `save` command, since implementation is not done")
                c_save_game(player = Player)
            
            case 'set':
                response = r_command_exc(c_set, *commands[1:])
                
            case 'room':
                response = r_command_exc(c_room, *commands[1:], current_room = current_room, player = player)

            case 'go':
                go_response = r_command_exc(c_go, *commands[1:], current_room = current_room)

                if isinstance(go_response, tuple):
                    response, current_room = go_response
                elif isinstance(go_response, Response):
                    response = go_response
                else:
                    raise TypeError(f'Unrecognized type of {type(go_response)}, with value {go_response}')
            case 'pass':
                response = r_command_exc(c_pass)
            case _:
                if f'c_{commands[0]}' in ALL_COMMANDS:
                    response = Response(f"You can't temporarily use `{commands[0]}` command, since implementation is not done")
                else:
                    response = Response('Unknown command')
                
            
        current_interface.update_section(
            'command_output', 
            response.content
        )
            
            


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        c_exit_game()