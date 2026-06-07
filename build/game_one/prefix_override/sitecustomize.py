import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/lenovoi/Projects/My-Projects/simple-turtlesim-game/install/game_one'
