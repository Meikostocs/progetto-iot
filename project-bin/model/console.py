from colorama import Fore, Back, Style
class Console:
    
    def __init__(self,debug=False):
        self.debug_print = debug

    def error(self, message):
        print(Fore.RED + '[ERROR]: '+Style.RESET_ALL+message)
    
    def debug(self,message):
        if self.debug_print:
            print(Fore.YELLOW + '[DEBUG]: '+Style.RESET_ALL + message)
    
    def print(self,message):
        print(Fore.GREEN+ '[PRINT]: '+Style.RESET_ALL + message)
