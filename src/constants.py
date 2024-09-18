from typing import TypeVar, Literal, Self, Tuple, List

T = TypeVar('T')

type DirectionLiteral = Literal['north', 'south', 'east', 'west']

type RoomsList = List[Tuple[Self, DirectionLiteral]]