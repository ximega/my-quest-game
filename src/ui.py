from src.ctypes import RoomsList
from src.exceptions import UnrecognisedValue
from settings.default import (
    DEFAULT_VISIBILITY_OF_INTERFACE_SECTION
)
from copy import deepcopy
from src.utils2 import irange
from src.classes.room import Room

def str_format_health_level(level: int, health_max: int) -> str:
    if level in irange(1, int(health_max * 0.1)):
        return 'near death'
    elif level in irange(int(health_max * 0.1) + 1, int(health_max * 0.3)):
        return 'severely damaged'
    elif level in irange(int(health_max * 0.3) + 1, int(health_max * 0.5)):
        return 'considerably damaged'
    elif level in irange(int(health_max * 0.5) + 1, int(health_max * 0.75)):
        return 'damaged'
    elif level in irange(int(health_max * 0.75) + 1, int(health_max * 0.95)):
        return 'healthy'
    elif level in irange(int(health_max * 0.95) + 1, int(health_max * 0.99)):
        return 'almost fully healthy'
    elif level == health_max:
        return 'completely healthy'
    else:
        raise UnrecognisedValue(f'Health level of entity (probably player) is unrecognized, and thus the error was raised. Health value = {level}')
    
def str_format_protection_level(level: int, protection_max: int) -> str:
    if level == 0:
        return 'unprotected'
    elif level in irange(1, int(protection_max * 0.1)):
        return 'severely weakly protected'
    elif level in irange(int(protection_max * 0.1) + 1, int(protection_max * 0.3)):
        return 'weakly protected'
    elif level in irange(int(protection_max * 0.3) + 1, int(protection_max * 0.5)):
        return 'okay-level protection'
    elif level in irange(int(protection_max * 0.5) + 1, int(protection_max * 0.75)):
        return 'well-protected'
    elif level in irange(int(protection_max * 0.75) + 1, int(protection_max * 0.95)):
        return 'extremely good level of protection'
    elif level in irange(int(protection_max * 0.95) + 1, protection_max):
        return 'supposedly unkillable'
    else:
        raise UnrecognisedValue(f'Protection level of entetiy (probably player) is unrecognised, and thus the error was raised. Protection (protection type unidentified, can be either of three) value = {level}')
    
def str_format_damage_level(level: int, damage_max: int) -> str:
    if level in irange(1, int(damage_max * 0.1)):
        return 'weak'
    elif level in irange(int(damage_max * 0.1) + 1, int(damage_max * 0.3)):
        return 'developed'
    elif level in irange(int(damage_max * 0.3) + 1, int(damage_max * 0.5)):
        return 'strong'
    elif level in irange(int(damage_max * 0.5) + 1, int(damage_max * 0.75)):
        return 'powerful'
    elif level in irange(int(damage_max * 0.75) + 1, int(damage_max * 0.95)):
        return 'extreme power!'
    elif level in irange(int(damage_max * 0.95) + 1, damage_max):
        return 'god punch?'
    else:
        raise UnrecognisedValue(f'Damage level of entetiy (probably player) is unrecognised, and thus the error was raised. Damage value = {level}')
        
    
class UserInterface:
    def __init__(self, name: str) -> None:      
        # Sections are stored in a dictionary, 
        # where value is a tuple of 2 contents
        # at first place is the content of the section,
        # in the second it is visibility of the section
        # either True - visible, False - hidden
        self.name = name
        self.__content: dict[str, tuple[str, bool]] = {'init_gap': ('\n\n', DEFAULT_VISIBILITY_OF_INTERFACE_SECTION)}
        self.__gap: str = '\n\n'

    def show(self) -> str:
        return self.__gap.join([section[0] for section in self.__content.values()])
    
    def add_section(self, section_name: str, content: str) -> None:        
        if section_name in self.__content.keys():    
            raise KeyError(f'Section with name {section_name} already exists')    
        else:
            self.__content[section_name] = (content, False)
        
    # def add_section_totop(self, section_name: str, content: str) -> None:
    #     copied = deepcopy(self.__content)
        
    #     self.__content = {section_name: (content, False)}
    #     self.__content.update(copied)
        
    def add_section_beforeend(self, section_name: str, content: str) -> None:
        last_element_key = list(self.__content)[-1]
        first_part = {k: v for k, v in self.__content.items() if k != last_element_key}
        last_part = {last_element_key: self.__content[last_element_key]}
        
        self.__content = dict(first_part)
        self.__content[section_name] = content
        self.__content.update(last_part)
    
    def update_section(self, section_name: str, new_content: str) -> None: 
        if section_name in self.__content.keys():
            prev_visibility_state = self.__content[section_name][1]
            self.__content[section_name] = (new_content, prev_visibility_state)
        else:
            self.add_section(section_name, new_content)
    
    def hide_section(self, section_name: str) -> None: 
        self.__content[section_name][1] = False
    
    def show_section(self, section_name: str) -> None:
        self.__content[section_name][1] = True

    @classmethod
    def room_ui(cls, rooms: RoomsList) -> str:
        content = str()

        northern = Room.get_room_from_list(rooms, 'north')
        western = Room.get_room_from_list(rooms, 'west')
        eastern = Room.get_room_from_list(rooms, 'east')
        southern = Room.get_room_from_list(rooms, 'south')

        if northern is not None:
            # 1st line
            content += ' '*16 + f'[  {northern.id}  ]'
            content += '\n'
            # 2nd line
            content += ' '*14 + f'[  tier {northern.tier}  ]'
            content += '\n'
        else:
            # fill two lines with \n if north doesn't exist
            content += '\n'*2

        # 3rd line
        content += '\n'

        if western is not None:
            # 4th line
            content += ' '*3 + f'[  {western.id}  ]'
            if northern is not None:
                content += ' '*9 + '↑'
            content += '\n'

            # 5th line
            # Change 'YOU' to something else
            # if want to display different text
            # note: need to refactor spaces for text not to shift
            content += f'[  tier {western.tier}  ]' + ' '*4 + '← ' + 'YOU '
            if eastern is not None:
                '→' + ' '*7 + f'[  {eastern.id}  ]'
            content += '\n'
        else:
            # 4th line
            if northern is not None:
                content += ' '*19 + '↑'
            content += '\n'

            # 5th line
            if eastern is not None:
                content += ' '*18 + 'YOU →' + ' '*7 + f'[  {eastern.id}  ]'
            content += '\n'

        # 6th line
        if eastern is not None:
            if southern is not None:
                content += ' '*19 + '↓' + ' '*8 + f'[  tier {eastern.tier}  ]'
            else:
                content += ' '*28 + f'[  tier {eastern.tier}  ]'
        else:
            if southern is not None:
                content += ' '*19 + '↓'
        # indentation for 6th and 7th (where latter is empty)
        content += '\n'*2

        if southern is not None:
            # 8th line
            content += ' '*16 + f'[  {southern.id}  ]'
            content += '\n'
            # 9 th line
            content += ' '*14 + f'[  tier {southern.tier}  ]'
            content += '\n'
        else:
            # 8th & 9th lines
            content += '\n'*2

        return content


MainUI = UserInterface('main')