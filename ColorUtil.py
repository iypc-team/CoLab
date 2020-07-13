"""Filename ColorUtil"""

__all__ = ['ColorOutput', 'C']

class ColorOutput:
    LITE =  '\033[96m'
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    WARNING = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    DARK = '\033[90m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    WHITE = '\033[0m'

global C
C = ColorOutput

print(f'{C.GREEN}OK')
