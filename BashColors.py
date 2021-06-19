# 09/08/2020

class Colors:
    def __init__(self):
        self.C = Colors

    # Reset
    ColorOff='\033[0m'
    
    # Regular Colors
    Black='\033[0;30m'
    Red='\033[0;31m'
    Green='\033[0;32m'
    Yellow='\033[0;33m'
    Blue='\033[0;34m'
    Purple='\033[0;35m'
    Cyan='\033[0;36m'
    White='\033[0;37m'
    
    # Bold
    BBlack='\033[1;30m'
    BRed='\033[1;31m'
    BGreen='\033[1;32m'
    BYellow='\033[1;33m'
    BBlue='\033[1;34m'
    BPurple='\033[1;35m'
    BCyan='\033[1;36m'
    BWhite='\033[1;37m'
    
    # Underline
    UBlack='\033[4;30m'
    URed='\033[4;31m'
    UGreen='\033[4;32m'
    UYellow='\033[4;33m'
    UBlue='\033[4;34m'
    UPurple='\033[4;35m'
    UCyan='\033[4;36m'
    UWhite='\033[4;37m'
    
    # Background
    OnBlack='\033[40m'
    OnRed='\033[41m'
    OnGreen='\033[42m'
    OnYellow='\033[43m'
    OnBlue='\033[44m'
    OnPurple='\033[45m'
    OnCyan='\033[46m'
    OnWhite='\033[47m'
    
    # High Intensity
    IBlack='\033[0;90m'
    IRed='\033[0;91m'
    IGreen='\033[0;92m'
    IYellow='\033[0;93m'
    IBlue='\033[0;94m'
    IPurple='\033[0;95m'
    ICyan='\033[0;96m'
    IWhite='\033[0;97m'
    
    # Bold High Intensity
    BIBlack='\033[1;90m'
    BIRed='\033[1;91m'
    BIGreen='\033[1;92m'
    BIYellow='\033[1;93m'
    BIBlue='\033[1;94m'
    BIPurple='\033[1;95m'
    BICyan='\033[1;96m'
    BIWhite='\033[1;97m'
    
    # High Intensity backgrounds
    OnIBlack='\033[0;100m'
    OnIRed='\033[0;101m'
    OnIGreen='\033[0;102m'
    OnIYellow='\033[0;103m'
    OnIBlue='\033[0;104m'
    OnIPurple='\033[0;105m'
    OnICyan='\033[0;106m'
    OnIWhite='\033[0;107m'

C = Colors()