import os
import json
from time import sleep
from .logo import *
from .system import System  # Updated import to match new class name

red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
violate="\033[1;37m"
nc="\033[00m"

class Main:
    def install_tools(self):
        while True:
            tool = Tools()
            num = 1
            total = len(tool.names)
            os.system("clear")
            logo.install_tools()
            print(f"\007")
            for tool_name in tool.names:
                print(f" {green}[ {violate}{num} {green}] {yellow}Install {green}{tool_name}{nc}")
                num += 1
            print(f"")
            logo.back()
            cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
            if cmd == "00" or cmd == "back":
                self.menu()
                break
            else:
                try:
                    if int(cmd) >= 1 and int(cmd) <= int(total):
                        os.system("clear")
                        logo.installing()
                        print(f"{green}Installing ....{nc}")
                        tool.install(tool.names[int(cmd) - 1])
                    else:
                        print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
                        sleep(1)
                except ValueError:
                    print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
                    sleep(1)

    def category(self):
        while True:
            tool = Tools()
            total = len(tool.category)
            num = 1
            os.system("clear")
            logo.tool_header()
            print(f"")
            for cat in tool.category:
                print(f"  {green}[ {violate}{num} {green}] {yellow}{tool.category_data[cat]}{nc}")
                num += 1
            print(f"")
            logo.back()
            cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
            if cmd == "00" or cmd == "back":
                self.menu()
                break
            else:
                try:
                    if int(cmd) in range(1, int(total) + 1):
                        while True:
                            print(int(cmd) - 1)
                            print(tool.category[int(cmd) - 1])
                            cnt = 1
                            os.system("clear")
                            logo.tool_header()
                            print(f"")
                            tmp_cat_tool = []
                            for i in tool.names:
                                if tool.category[int(cmd) - 1] in tool.data[i]["category"]:
                                    tmp_cat_tool.append(tool.data[i]['name'])
                                    print(f" {green}[ {violate}{cnt} {green}] {yellow}Install {green}{tool.data[i]['name']}{nc}")
                                    cnt += 1
                            print(f"")
                            logo.back()
                            tcmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
                            if tcmd == "00" or tcmd == "back":
                                break
                            else:
                                try:
                                    cat_total = len(tmp_cat_tool)
                                    if int(tcmd) in range(1, int(cat_total) + 1):
                                        os.system("clear")
                                        logo.installing()
                                        print(f"{green}Installing ....{nc}")
                                        tool.install(tmp_cat_tool[int(tcmd) - 1])
                                    else:
                                        print(f"\007{red}Sorry,{violate} '{tcmd}' {blue}: {red}invalid input !!{nc}")
                                        sleep(1)
                                except ValueError:
                                    print(f"\007{red}Sorry,{violate} '{tcmd}' {blue}: {red}invalid input !!{nc}")
                                    sleep(1)
                    else:
                        print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
                        sleep(1)
                except ValueError:
                    print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
                    sleep(1)

    def update(self):
        while True:
            os.system("clear")
            logo.update()
            cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
            if cmd == "1":
                system = System()  # Updated to use new class name
                if system.connection():
                    os.system("clear")
                    logo.updating()
                    if system.sudo is not None:
                        if os.path.exists(system.home + "/Tool-X"):
                            pass
                        else:
                            os.system(system.sudo + " git clone https://github.com/rajkumardusad/Tool-X.git " + system.home + "/Tool-X")
                        if os.path.exists(system.home + "/Tool-X/install.aex"):
                            os.system("cd " + system.home + "/Tool-X && " + system.sudo + " sh install.aex")
                            if os.path.exists(system.bin + "/Tool-X") and os.path.exists(system.conf_dir + "/Tool-X"):
                                os.system("clear")
                                logo.updated()
                                cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
                            else:
                                os.system("clear")
                                logo.update_error()
                                cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
                        else:
                            os.system("clear")
                            logo.update_error()
                            cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
                    else:
                        if os.path.exists(system.home + "/Tool-X"):
                            pass
                        else:
                            os.system("git clone https://github.com/rajkumardusad/Tool-X.git " + system.home + "/Tool-X")
                        if os.path.exists(system.home + "/Tool-X/install.aex"):
                            os.system("cd " + system.home + "/Tool-X && sh install.aex")
                            if os.path.exists(system.bin + "/Tool-X") and os.path.exists(system.conf_dir + "/Tool-X"):
                                os.system("clear")
                                logo.updated()
                                cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
                            else:
                                os.system("clear")
                                logo.update_error()
                                cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
                        else:
                            os.system("clear")
                            logo.update_error()
                            cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
                else:
                    os.system("clear")
                    logo.nonet()
                    tmp = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
            elif cmd == "0" or cmd == "back":
                self.menu()
                break
            else:
                print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
                sleep(1)

    def about(self):
        while True:
            tool = Tools()
            total = len(tool.names)
            os.system("clear")
            logo.about(total)
            cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
            self.menu()
            break

    @classmethod
    def menu(cls):
        while True:
            tool = Tools()
            total = len(tool.names)
            os.system("clear")
            logo.menu(total)
            cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
            if cmd == "1":
                cls.install_tools(cls)
                break
            elif cmd == "2":
                cls.category(cls)
                break
            elif cmd == "3":
                cls.update(cls)
                break
            elif cmd == "4":
                cls.about(cls)
                break
            elif cmd == "x" or cmd == "X" or cmd == "exit":
                os.system("clear")
                logo.exit()
                break
            elif cmd == "rm -t" or cmd == "rm -T" or cmd == "uninstall tool-x" or cmd == "unistall Tool-X":
                system = System()  # Updated to use new class name
                if system.sudo:
                    os.system(system.sudo + " rm -rf " + system.bin + "/Tool-X")
                    os.system(system.sudo + " rm -rf " + system.bin + "/toolx")
                    os.system(system.sudo + " rm -rf " + system.conf_dir + "/Tool-X")
                else:
                    os.system("rm -rf " + system.bin + "/Tool-X")
                    os.system("rm -rf " +
                  
