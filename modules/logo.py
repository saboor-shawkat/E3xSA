red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
violate = "\033[1;37m"
nc = "\033[00m"

class Logo:
    @classmethod
    def tool_header(cls):
        print(f'''\007

{yellow}
         _____           _    __  __
        |_   _|__   ___ | |   \ \/ /
          | |/ _ \ / _ \| |____\  /
          | | (_) | (_) | |____/  \    
          |_|\___/ \___/|_|   /_/\_\ {purple}v2.1


{cyan} =============================================
{yellow}|          Install Best Hacking Tool          |
{cyan} ============================================={nc}''')

    @classmethod
    def tool_footer(cls):
        print(f'''{cyan}_______________________________________________
==============================================={nc}''')

    @classmethod
    def not_installed(cls):
        cls.tool_header()
        print(f'''
{cyan}  [ + ]  {red}We can't install E3xSA.
{cyan}  [ + ]  {red}There are some errors.
{cyan}  [ + ]  {red}Please try again after some time!''')
        cls.tool_footer()

    @classmethod
    def install_terms(cls):
        cls.tool_header()
        print(f'''
{yellow}  [ + ] {green}Use It At Your Own Risk.
{yellow}  [ + ] {green}No Warranty.
{yellow}  [ + ] {green}Use it for legal purposes only.
{yellow}  [ + ] {green}We are not responsible for your actions.
{yellow}  [ + ] {green}Do not engage in forbidden activities.

{red} If you are installing this tool,
it means you agree with all terms.''')
        cls.tool_footer()

    @classmethod
    def install_success(cls):
        cls.tool_header()
        print(f'''
{yellow}    [ + ] {green}E3xSA installed successfully.
{yellow}    [ + ] {green}To run E3xSA,
{yellow}    [ + ] {green}Type E3xSA in your terminal.''')
        cls.tool_footer()

    @classmethod
    def update(cls):
        cls.tool_header()
        print(f'''
{yellow}  [ 1 ] {green}Update your E3xSA.
{yellow}  [ 0 ] {green}Go Back.{nc}''')
        cls.tool_footer()

    @classmethod
    def update_success(cls):
        cls.tool_header()
        print(f'''
{yellow}      [ + ] {green}E3xSA updated successfully.
{yellow}      [ + ] {green}Press Enter to continue.{nc}''')
        cls.tool_footer()

    @classmethod
    def no_network(cls):
        cls.tool_header()
        print(f'''
{cyan}  [ + ]  {red}No network connection?
{cyan}  [ + ]  {red}Are you offline?
{cyan}  [ + ]  {red}Please try again later.{nc}''')
        cls.tool_footer()

    @classmethod
    def update_error(cls):
        cls.tool_header()
        print(f'''
{red}  [ + ]  {red}We can't update E3xSA.
{red}  [ + ]  {red}Please try again later.{nc}''')
        cls.tool_footer()

    @classmethod
    def about(cls, total):
        cls.tool_header()
        print(f'''
{yellow}       [+] Tool Name :- {green}E3xSA
{yellow}       [+] Latest Update :- {green}8/8/2024.{nc}
{yellow}       [+] Tools :- {green}Total {total} tools.{nc}

{yellow} [+] {green}E3xSA is an automatic tool installer.
{yellow} [+] {green}Made for Termux and Linux-based systems.
{red} [+] Note :- Use this tool at your own risk.''')
        cls.tool_footer()

    @classmethod
    def install_tools(cls):
        print(f"""{yellow} =============================================
{green}|_____________ Select your tool ______________|
 {yellow}============================================={nc}""")

    @classmethod
    def already_installed(cls, name):
        cls.tool_header()
        print(f'''
{yellow}  [ + ] {green}Sorry ??
{yellow}  [ + ] {violate}'{name}'{green} is already installed!''')
        cls.tool_footer()

    @classmethod
    def installed(cls, name):
        cls.tool_header()
        print(f'''
{yellow}  [ + ] {green}Installed successfully!
{yellow}  [ + ] {violate}'{name}'{green} has been installed successfully!''')
        cls.tool_footer()

    @classmethod
    def not_installed(cls, name):
        cls.tool_header()
        print(f'''
{yellow}  [ + ] {red}Sorry ??
{yellow}  [ + ] {violate}'{name}'{red} is not installed!''')
        cls.tool_footer()

    @classmethod
    def back(cls):
        print(f"""\033[01;36m =============================================
{yellow}|  00) Back                                   |
 \033[01;36m============================================={nc}""")

    @classmethod
    def updating(cls):
        print(f"""{yellow} =============================================
{green}|______________ Updating E3xSA ______________|
 {yellow}============================================={nc}""")

    @classmethod
    def installing(cls):
        print(f"""{yellow} =============================================
{green}|________________ Installing _________________|
 {yellow}============================================={nc}""")

    @classmethod
    def menu(cls, total):
        cls.tool_header()
        print(f'''
{yellow}  [ 1 ] {green}Show all tools.{yellow} [ {purple}{total} tools{yellow} ]
{yellow}  [ 2 ] {green}Tools Category.
{yellow}  [ 3 ] {green}Update E3xSA.
{yellow}  [ 4 ] {green}About Us.
{yellow}  [ x ] {green}Exit.''')
        cls.tool_footer()

    @classmethod
    def exit(cls):
        cls.tool_header()
        print(f'''
{yellow}         [ + ] {green}Thanks for using E3xSA
{yellow}         [ + ] {green}Goodbye!{nc}''')
        cls.tool_footer()
      
