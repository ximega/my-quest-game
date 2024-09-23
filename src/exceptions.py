class PlayerAlreadyExist(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        
class InventoryIsFull(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        
class InventoryWillBeFull(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
    
class IncorrectCommand(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        
class ProtectionTypeDoesNotExist(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        
class ItemCannotAtack(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        
class UnnecessaryIngridients(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        
class NoRequiredIngridients(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        
class IncorrectArgument(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        
class CraftingErrorRecipe(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        
class CommandArgumentDoesnotExist(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        
class InstanceAlreadyExists(Exception):
    def __init__(self, obj) -> None:
        super().__init__(f'The {obj} object already exists and new instance can\'t be created')
        
class UnrecognisedValue(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
    
class TemporarilyInaccessableCommand(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)   
    
class DontHaveRequiredItem(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)   

class InaccessableRoom(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

class RoomAlreadyOpen(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

class ProcessError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)