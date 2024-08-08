import os
import json
from time import sleep
from .logo import *
from .system import *

red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
violate = "\033[1;37m"
nc = "\033[00m"

class Main:
    def __init__(self):
        self.tool = tools()
        self.total_tools = len(self.tool.names)

    def handle_input(self, valid_inputs, error_message="Invalid input!"):
        cmd = input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
        if cmd in valid_inputs:
            return cmd
        print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}{error_message}{nc}")
        sleep(1)
        return None

    def install_tools(self):
        while True:
            os.system("clear")
            logo.install_tools()
            for num, tool_name in enumerate(self.tool.names, 1):
                print(f" {green}[ {violate}{num} {green}] {yellow}Install {green}{tool_name}{nc}")
            print("")
            logo.back()

            cmd = self.handle_input(map(str, range(1, self.total_tools + 1)) | {"00", "back"})
            if cmd in {"00", "back"}:
                self.menu()
                break
            if cmd:
                self.install_tool(int(cmd) - 1)

    def install_tool(self, index):
        tool_name = self.tool.names[index]
        os.system("clear")
        logo.installing()
        print(f"{green}Installing ....{nc}")
        self.tool.install(tool_name)

    def category(self):
        while True:
            os.system("clear")
            logo.tool_header()
            for num, cat in enumerate(self.tool.category, 1):
                print(f"  {green}[ {violate}{num} {green}] {yellow}{self.tool.category_data[cat]}{nc}")
            print("")
            logo.back()

            cmd = self.handle_input(map(str, range(1, len(self.tool.category) + 1)) | {"00", "back"})
            if cmd in {"00", "back"}:
                self.menu()
                break
            if cmd:
                self.show_category_tools(int(cmd) - 1)

    def show_category_tools(self, index):
        category = self.tool.category[index]
        os.system("clear")
        logo.tool_header()
        tmp_cat_tool = [tool['name'] for tool in self.tool.data.values() if category in tool['category']]
        
        for cnt, tool_name in enumerate(tmp_cat_tool, 1):
            print(f" {green}[ {violate}{cnt} {green}] {yellow}Install {green}{tool_name}{nc}")
        print("")
        logo.back()

        tcmd = self.handle_input(map(str, range(1, len(tmp_cat_tool) + 1)) | {"00", "back"})
        if tcmd in {"00", "back"}:
            return
        if tcmd:
            self.install_tool(tmp_cat_tool[int(tcmd) - 1])

    def update(self):
        while True:
            os.system("clear")
            logo.update()
            cmd = self.handle_input({"1", "0", "back"})
            if cmd == "1":
                self.perform_update()
            elif cmd in {"0", "back"}:
                self.menu()
                break

    def perform_update(self):
        system = sys()
        if system.connection():
            os.system("clear")
            logo.updating()
            update_cmd = f"{system.sudo} git clone https://github.com/rajkumardusad/Tool-X.git {system.home}/Tool-X"
            install_cmd = f"cd {system.home}/Tool-X && {system.sudo} sh install.aex"

            if not os.path.exists(system.home + "/Tool-X"):
                os.system(update_cmd)
            if os.path.exists(system.home + "/Tool-X/install.aex"):
                os.system(install_cmd)
                if os.path.exists(system.bin + "/Tool-X") and os.path.exists(system.conf_dir + "/Tool-X"):
                    os.system("clear")
                    logo.updated()
                else:
                    os.system("clear")
                    logo.update_error()
            else:
                os.system("clear")
                logo.update_error()
            input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
        else:
            os.system("clear")
            logo.nonet()
            input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")

    def about(self):
        while True:
            os.system("clear")
            logo.about(self.total_tools)
            self.menu()
            break

    def menu(self):
        while True:
            os.system("clear")
            logo.menu(self.total_tools)
            cmd = self.handle_input({"1", "2", "3", "4", "x", "X", "exit", "rm -t", "rm -T", "uninstall tool-x", "unistall Tool-X"})
            if cmd == "1":
                self.install_tools()
                break
            elif cmd == "2":
                self.category()
                break
            elif cmd == "3":
                self.update()
                break
            elif cmd == "4":
                self.about()
                break
            elif cmd in {"x", "X", "exit"}:
                os.system("clear")
                logo.exit()
                break
            elif cmd in {"rm -t", "rm -T", "uninstall tool-x", "unistall Tool-X"}:
                self.uninstall()
                break

    def uninstall(self):
        system = sys()
        remove_cmds = [
            f"{system.sudo} rm -rf {system.bin}/Tool-X",
            f"{system.sudo} rm -rf {system.bin}/toolx",
            f"{system.sudo} rm -rf {system.conf_dir}/Tool-X"
        ]
        for cmd in remove_cmds:
            os.system(cmd)
        os.system("clear")
        logo.exit()

class tools:
    def __init__(self):
        system = sys()
        with open(system.conf_dir + "/Tool-X/core/data.json") as data_file:
            self.data = json.load(data_file)
        with open(system.conf_dir + "/Tool-X/core/cat.json") as cat_file:
            self.category_data = json.load(cat_file)
        self.names = list(self.data.keys())
        self.category = list(self.category_data.keys())

    def install(self, name):
        tool_info = self.data[name]
        package_name = tool_info["package_name"]
        package_manager = tool_info["package_manager"]
        url = tool_info["url"]
        req = list(tool_info["dependency"])

        system = sys()
        if system.connection():
            self.install_dependencies(req, system)
            self.install_package(package_name, package_manager, url, system)
        else:
            os.system("clear")
            logo.nonet()
            input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")

    def install_dependencies(self, req, system):
        for dep in req:
            if not os.path.exists(system.bin + "/" + dep):
                install_cmd = f"{system.sudo} {system.pac} install {dep} -y" if system.sudo else f"{system.pac} install {dep} -y"
                os.system(install_cmd)

    def install_package(self, package_name, package_manager, url, system):
        if package_manager == "package_manager":
            self.install_with_package_manager(package_name, system)
        elif package_manager == "git":
            self.install_with_git(package_name, url, system)
        elif package_manager == "wget":
            self.install_with_wget(package_name, url, system)
        elif package_manager == "curl":
            self.install_with_curl(package_name, url, system)

    def install_with_package_manager(self, package_name, system):
        if os.path.exists(system.bin + "/" + package_name):
            os.system("clear")
            logo.already_installed(package_name)
        else:
            install_cmd = f"{system.sudo} {system.pac} install {package_name} -y" if system.sudo else f"{system.pac} install {package_name} -y"
            os.system(install_cmd)
            self.check_installation(package_name, system)

    def install_with_git(self, package_name, url, system):
        if os.path.exists(system.home + "/" + package_name):
            os.system("clear")
            logo.already_installed(package_name)
        else:
            clone_cmd = f"{system.sudo} git clone {url} {system.home}/{package_name}" if system.sudo else f"git clone {url} {system.home}/{package_name}"
            os.system(clone_cmd)
            self.check_installation(package_name, system)

    def install_with_wget(self, package_name, url, system):
        if os.path.exists(system.home + "/" + package_name):
            os.system("clear")
            logo.already_installed(package_name)
        else:
            wget_cmd = f"{system.sudo}
