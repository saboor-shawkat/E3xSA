import os
import subprocess
import requests

class Sys:
    def __init__(self):
        self.home = os.getenv("HOME")
        self.sudo = self._find_sudo()
        self.conf_dir = self._find_conf_dir()
        self.pac, self.bin = self._find_package_manager()

    def _find_sudo(self):
        sudo_paths = [
            "/usr/lib/sudo", "/lib/sudo", "/usr/bin/sudo",
            "/bin/sudo", "/usr/sbin/sudo", "/sbin/sudo"
        ]
        for path in sudo_paths:
            if os.path.exists(path):
                return "sudo"
        return None

    def _find_conf_dir(self):
        conf_dirs = [
            "/usr/etc", "/data/data/com.termux/files/usr/etc", "/etc"
        ]
        for path in conf_dirs:
            if os.path.exists(path):
                return path
        return None

    def _find_package_manager(self):
        package_managers = {
            "yum": ["/usr/bin/yum", "/bin/yum", "/usr/sbin/yum", "/sbin/yum"],
            "apt-get": ["/usr/bin/apt", "/bin/apt", "/usr/sbin/apt", "/sbin/apt"],
            "pkg": ["/data/data/com.termux/files/usr/bin/pkg"],
            "brew": ["/usr/local/bin/brew"],
            "apk": ["/usr/bin/apk", "/bin/apk", "/usr/sbin/apk", "/sbin/apk"]
        }
        for pac, paths in package_managers.items():
            for path in paths:
                if os.path.exists(path):
                    return pac, os.path.dirname(path)
        return None, None

    def connection(self):
        try:
            response = requests.get("https://www.google.com")
            return response.ok
        except requests.RequestException:
            return False

    def install_requests(self):
        try:
            import requests
        except ImportError:
            subprocess.check_call([self.pac, 'install', 'requests', '-y'])

