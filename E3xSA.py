import os
import sys
from modules.menu import main
from modules.logo import logo

if __name__ == "__main__":
    try:
        main.menu()
    except KeyboardInterrupt:
        os.system("clear")
        logo.exit()
