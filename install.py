import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

# Updated color scheme
red = "\033[1;31m"
green = "\033[1;32m"
nc = "\033[00m"

class tool:
  @classmethod
  def install(self):
    while True:
      system = sys()
      os.system("clear")
      logo.ins_tnc()
      inp = input(f"{green}Do you want to install E3xSA [Y/n]> {nc}")
      if inp.lower() == "y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          # require root permission
          if not os.path.exists(system.conf_dir + "/E3xSA"):
            os.system(system.sudo + " mkdir " + system.conf_dir + "/E3xSA")
          os.system(system.sudo + " cp -r modules core E3xSA.py " + system.conf_dir + "/E3xSA")
          os.system(system.sudo + " cp -r core/E3xSA " + system.bin)
          os.system(system.sudo + " cp -r core/e3xsa " + system.bin)
          os.system(system.sudo + " chmod +x " + system.bin + "/E3xSA")
          os.system(system.sudo + " chmod +x " + system.bin + "/e3xsa")
          os.system("cd .. && " + system.sudo + " rm -rf E3xSA")
          if os.path.exists(system.bin + "/E3xSA") and os.path.exists(system.conf_dir + "/E3xSA"):
            os.system("clear")
            logo.ins_sc()
            tmp = input(f"{red}E3xSA{nc}@{red}space {green}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp = input(f"{red}E3xSA{nc}@{red}space {green}$ {nc}")
            break
        else:
          if not os.path.exists(system.conf_dir + "/E3xSA"):
            os.system("mkdir " + system.conf_dir + "/E3xSA")
          os.system("cp -r modules core E3xSA.py " + system.conf_dir + "/E3xSA")
          os.system("cp -r core/E3xSA " + system.bin)
          os.system("cp -r core/e3xsa " + system.bin)
          os.system("chmod +x " + system.bin + "/E3xSA")
          os.system("chmod +x " + system.bin + "/e3xsa")
          os.system("cd .. && rm -rf E3xSA")
          if os.path.exists(system.bin + "/E3xSA") and os.path.exists(system.conf_dir + "/E3xSA"):
            os.system("clear")
            logo.ins_sc()
            tmp = input(f"{red}E3xSA{nc}@{red}space {green}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp = input(f"{red}E3xSA{nc}@{red}space {green}$ {nc}")
            break
      else:
        break

if __name__ == "__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
