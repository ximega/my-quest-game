from typing import Self
from src.ui import *
from src.commands import *
from src.rooms.sets import *
from src.classes.entities import Player
from src.classes.crafting import Machine
from src.classes.enchants import Enchant
import src.commands
from src.player import playerObject
from settings.default import (
    MAX_HEALTH, 
    MAX_PROJECTILE_PROTECTION, 
    MAX_PROTECTION, 
    MAX_SUBPROTECTION,
    MAX_DAMAGE,
    AUTO_SAVE
)


class Game:
    def __init__(self) -> None:
        return
        
    def initialize_all_commands(self) -> Self:
        self.all_commands = list(filter(lambda x: x.startswith('c_'), dir(src.commands)))
        return self
    
    def set_current_interface(self, ui: UserInterface) -> Self:
        self.current_interface = ui
        return self

        
    def set_current_room(self, room: Room) -> Self:
        self.current_room = room
        return self
        
    def set_player(self, player: Player) -> Self:
        self.player = player
        return self
        
    def update_MainUI(self) -> None:      
        self.current_interface.update_section(
            'player_main_info',
            
            f'Health: {self.player.health}/{MAX_HEALTH} ({str_format_health_level(self.player.health, MAX_HEALTH)})\nProtection: {self.player.protection} ({str_format_protection_level(self.player.protection, MAX_PROTECTION)})\nSubprotection: {self.player.subprotection} ({str_format_protection_level(self.player.subprotection, MAX_SUBPROTECTION)})\nProtection: {self.player.projectile_protection} ({str_format_protection_level(self.player.projectile_protection, MAX_PROJECTILE_PROTECTION)})\nDamage: {self.player.damage} ({str_format_damage_level(self.player.damage, MAX_DAMAGE)})'
        )
        
        self.current_interface.update_section(
            'player_add_info',
            
            f'Nutrition: {int(self.player.nutrition * 100)}%\nGold coins: {self.player.gold_coins}\nMinis count: {len(self.player.minis)}'
        )
        
        self.current_interface.update_section(
            'player_active_inv',
            
            self.player.get_active_items()
        )
        
    def prompt_commands(self) -> list[str]:
        return input('\n$: ').split(' ')
    
    def match_commands(self, commands: list[str]) -> Response:
        response = None
        
        match commands[0]:
            case 'debug':
                response = r_command_exc(c_debug, *commands[1:], all_commands = self.all_commands, current_room = self.current_room)
            
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
                response = r_command_exc(c_room, *commands[1:], current_room = self.current_room, player = self.player)

            case 'go':
                go_response = r_command_exc(c_go, *commands[1:], current_room = self.current_room)

                if isinstance(go_response, tuple):
                    response, current_room = go_response
                elif isinstance(go_response, Response):
                    response = go_response
                else:
                    raise TypeError(f'Unrecognized type of {type(go_response)}, with value {go_response}')
            case 'pass':
                response = r_command_exc(c_pass)
            case _:
                if f'c_{commands[0]}' in self.all_commands:
                    response = Response(f"You can't temporarily use `{commands[0]}` command, since implementation is not done")
                else:
                    response = Response('Unknown command')
                    
        return response
        
    def run(self) -> None:
        while True:           
            if self.current_interface is MainUI:  
                self.update_MainUI()
            
            print(self.current_interface.show())
            
            commands = self.prompt_commands()
            
            response = None

            # take damage if there is mobs in the room
            self.player = c_opponent_damage(current_room = self.current_room, player = self.player)
            
            response = self.match_commands(commands)
                             
            self.current_interface.update_section(
                'command_output', 
                response.content
            )