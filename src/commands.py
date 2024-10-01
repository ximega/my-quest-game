from src.classes.entities import Player, Mob, Boss
from src.classes.room import Room
from collections.abc import Callable
from src.exceptions import (
    CommandArgumentDoesnotExist, 
    DontHaveRequiredItem,
    ProcessError
)
import settings.default
from src.ui import UserInterface


DIRECTIONS = ['north', 'south', 'east', 'west']

class Response:
    def __init__(self, content: str | list[str]) -> None:
        self.content = None
        if isinstance(content, str):
            self.content = content + '\n'
        elif isinstance(content, list):
            self.content = content
        else:
            raise KeyError('Unrecognized type of Response.content')
        
        
    def __str__(self) -> str:
        return str(self.content)
    
def r_command_exc(command: Callable, *args, **objects) -> Response | tuple[Response, Room]:
    try:
        return command(*args, **objects)
    except IndexError:
        return Response(f"{command.__name__} command can't run with provided arguments: {args}")
    except KeyError as exc:
        return Response(f"Required keywords weren't provided to the {command.__name__} command: {exc.args[0]}")
    except CommandArgumentDoesnotExist as exc:
        return Response(exc.args[0])
    except DontHaveRequiredItem as exc:
        return Response(f'Player do not have required "{exc.args[0]}"')
    

def c_use(*args, **objects) -> Response:
    ...
    
def c_attack(*args, **objects) -> Response:
    ...
    
def c_recent(*args, **objects) -> Response:
    ...
    
def c_inv(*args, **objects) -> Response:
    ...
        
def c_item(*args, **objects) -> Response:
    ...
        
def c_room(*args: str, **objects: str) -> Response:
    match args[0]:
        case 'near':
            current_room: Room = objects['current_room']

            try:
                if len(args) > 2:
                    raise CommandArgumentDoesnotExist(f'c_room: provided too many arguments for `room near [direction]`. Starting from {args[2:]} is/are unnecessary')

                return Response(current_room.get_next_room(args[1])) # TODO: remake it to readable UI, as it was in docs

            except IndexError:
                return Response(UserInterface.room_ui(current_room.next_rooms))
        case 'light':
            ...
        case 'openchest':
            ...
        case 'open':
            if args[1] is None:
                raise CommandArgumentDoesnotExist(f'c_room: Command argument wasn\'t provided, and thus the command can\'t be interpreted')
            if args[1] not in DIRECTIONS:
                raise CommandArgumentDoesnotExist(f'c_room: Command argument {args[1]} doesn\'t exist, and thus the command can\'t be executed')
            
            try:
                current_room: Room = objects['current_room']
                player: Player = objects['player']

                potential_room = current_room.get_next_room(args[1])

                if potential_room is None:
                    raise CommandArgumentDoesnotExist(f'c_room: Room in this direction doesn\'t exist')
                
                potential_room.open_room(player)

                return Response(f'You opened room with id {potential_room.id} in {args[1]} direction to you')
                
            except KeyError:
                raise CommandArgumentDoesnotExist(f'c_room: Sufficient objects (player and current_room) weren\'t provided to the command')
        case _:
            raise CommandArgumentDoesnotExist('c_room: Command argument doesn\'t exist, and thus the command can\'t be executed')

def c_go(*args, **objects) -> tuple[Response, Room]:
    if args[0] not in DIRECTIONS:
        raise CommandArgumentDoesnotExist(f'c_go: Command argument {args[1]} doesn\'t exist, and thus the command can\'t be executed')
    
    if len(args) > 1:
        raise CommandArgumentDoesnotExist(f'c_go: Command argument {args[1]} doesn\'t exist, and thus the command can\'t be executed')

    try:
        current_room: Room = objects['current_room']

        potential_room = current_room.get_next_room(args[0])

        if potential_room is None:
            raise CommandArgumentDoesnotExist(f"c_go: Room in this direction doesn't exist")

        if not potential_room.is_open:
            raise CommandArgumentDoesnotExist(f"c_go: You can't enter the room with id {potential_room.id}, since it is locked for the player")

        if not isinstance(potential_room, Room):
            raise CommandArgumentDoesnotExist(f'c_go: Potential room, where player specified does not exist. Type "Any" was provided. {potential_room=}')

        return (
            Response(f'You went to room with id {potential_room.id} in {args[0]} direction'),
            potential_room
        )

    except KeyError:
        return Response('You can\'t go through walls, neither enter them')

        
def c_quests(*args, **objects) -> Response:
    ...
        
def c_upgrade(*args, **objects) -> Response:
    ...
        
def c_shop(*args, **objects) -> Response:
    ...
        
def c_minis(*args, **objects) -> Response:
    ...
        
def c_spell(*args, **objects) -> Response:
    ...
        
def c_potion(*args, **objects) -> Response:
    ...
            
def c_machine(*args, **objects) -> Response:
    ...
            
def c_craft(*args, **objects) -> Response:
    ...
            
def c_save_game(*args, **objects) -> Response:
    ...
            
def c_exit_game(*args, **objects) -> None:
    exit(1)
            
def c_escape_interface(*args, **objects) -> Response:
    ...
    
def c_debug(*args, **objects) -> Response:
    content = str()
    
    match args[0]:
        case 'list':
            match args[1]:
                case 'all':
                    content = ", ".join(objects['all_commands'])
                case _:
                    raise CommandArgumentDoesnotExist(f'c_debug: Command argument {args[1]} doesn\'t exist, and thus the command can\'t be executed')
        case 'room':
            match args[1]:
                case 'current':    
                    try:
                        some = args[2] # add future logic for specified args
                    except IndexError:
                        current_room: Room = objects['current_room']

                        content = f"{current_room.id=}\n\n{current_room.is_open=}\nloot_length={len(current_room.loot)}\n\n{current_room.tier=}\nnext_rooms_number={len(current_room.next_rooms)}"

                        if current_room.boss is not None:
                            content += f'\n{current_room.boss.name=}'
                        if current_room.mobs is not None:
                            content += f'\nmob_length={len(current_room.mobs)}'
                case _:
                    raise CommandArgumentDoesnotExist(f'c_debug: Command argument {args[1]} doesn\'t exist, and thus the command can\'t be executed')
        case _:
            raise CommandArgumentDoesnotExist(f'c_debug: Command argument {args[0]} doesn\'t exist, and thus the command can\'t be executed')
    
    return Response(content)

def c_set(*args, **objects) -> Response:    
    if args[0] != 'default':
        raise CommandArgumentDoesnotExist('c_set: Unrecognized settings scope')
    
    ALL_DEFAULT_SETTINGS: list[str] = dir(settings.default)
    
    if args[1] not in ALL_DEFAULT_SETTINGS:
        raise CommandArgumentDoesnotExist('c_set: Unrecognized settings.default constant')
    try:
        with open('settings/default.py', 'r') as file:
            default_settings_content_splitted: list[str] = file.read().split('\n')
            
            new_list_settings: list[str] = []
            
            for setting in default_settings_content_splitted:
                splitted_setting = setting.split(' ')
                
                if setting.startswith(args[1]):
                    new_list_settings.append(f"{splitted_setting[0]} = {args[2]}")
                else:
                    new_list_settings.append(setting)
                    
            new_settings: str = "\n".join(new_list_settings)
            
            with open('settings/default.py', 'w') as same_file:          
                same_file.write(new_settings)
            
            return Response(f'The value of {args[1]} was successfully changed to {args[2]}')
                
    except IndexError:
        raise CommandArgumentDoesnotExist('c_set: Received empty value')
                        
def c_opponent_damage(*args, **objects) -> Player:
    room: Room = objects['current_room']
    player: Player = objects['player']

    type MobList = list[Mob]
    amount = int()

    if len(args) > 0:
        raise CommandArgumentDoesnotExist('c_opponent_damage: Unnecessary number of arguments, can\'t be more than 1')
    
    if isinstance(room.boss, Boss):
        amount += player.take_damage('boss', boss_damage=room.boss.damage)
    if isinstance(room.mobs, list):
        amount += player.take_damage('mobs', mob_damage=room.mobs[0].damage, mob_count=len(room.mobs))
        
    if not isinstance(amount, int):
        raise ProcessError('c_opponent_damage: Amount of damage given is unknown, something has happened in higher hierarchy, which is unaccessible or unknown.')
        
    return player

def c_pass(*args, **objects) -> Response:
    if len(args) > 0: raise CommandArgumentDoesnotExist('c_pass: Provided too many arguments (more than 0). The command doesn\'t take any arguments')

    return Response('')