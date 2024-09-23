# For debugging only
# When playing should equal True, 
# otherwise game wont be saved
AUTO_SAVE = False

DEFAULT_CHARACTER_NAME = 'SuperLox'

MAX_STACK_SIZE = 100

MAX_KEY_TIER = 10

# Defining properties for all objects in game
MAX_HEALTH = 100
MAX_PROTECTION = 500
MAX_SUBPROTECTION = 500
MAX_PROJECTILE_PROTECTION = 350
MAX_DAMAGE = 1000

MIN_DURABILITY = 100


PROTECTION_MODIFIER = 0.90
SUBPROTECTION_MODIFIER = 0.85
PROJECTILE_PROTECTION_MODIFIER = 0.90

# MAXIMUM ENCHANTS
MAX_ENCHANT_UNBREAKING = 10
MAX_ENCHANT_ATACK = 12


ENCHANT_MODIFIER = 0.02
ENCHANT_RESULTING_MODIFIER = 1 - ENCHANT_MODIFIER
ENCHANT_DAMAGE_MODIFIER = 0.5
ENCHANT_DAMAGE_RESULTING_MODIFIER = 1 + ENCHANT_DAMAGE_MODIFIER
ENCHANT_DEFENSE_MODIFIER = 0.3
ENCHANT_DEFENSE_RESULTING_MODIFIER = 1 - ENCHANT_DEFENSE_MODIFIER



INIT_INV_SIZE = 30
INIT_ACTIVE_INV_SIZE = 2
INIT_MINI_MAX_SIZE = 0



DEFAULT_VISIBILITY_OF_INTERFACE_SECTION = False

GAME_OVER_TEXT = """
  ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
 ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║██║   ██║██╔══╝  ██╔══██╗
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝╚██████╔╝███████╗██║  ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""