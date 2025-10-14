import subprocess
from config import Config

class EmulatorUtils:
    @staticmethod
    def __is_boot_completed():
        try:
            output = subprocess.check_output(
                [Config().ADB_PATH, "shell", "getprop", "sys.boot_completed"],
                stderr=subprocess.STDOUT
            ).decode().strip()

            return output == "1"
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def __is_systemui_alive():
        try:
            output = subprocess.check_output(
                [Config().ADB_PATH, "shell", "pidof", "com.android.systemui"],
                stderr=subprocess.STDOUT
            ).decode().strip()

            return bool(output)
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def __is_surfaceflinger_alive():
        try:
            output = subprocess.check_output(
                [Config().ADB_PATH, "shell", "pidof", "surfaceflinger"],
                stderr=subprocess.STDOUT
            ).decode().strip()

            return bool(output)
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def __adb_responds():
        try:
            subprocess.check_output([Config().ADB_PATH, "shell", "echo", "ping"])

            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def __has_launcher_started():
        try:
            output = subprocess.check_output(
                [Config().ADB_PATH, "shell", "pidof", "com.google.android.apps.nexuslauncher"],
                stderr=subprocess.STDOUT
            ).decode().strip()

            return bool(output)
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def __is_package_manager_ready():
        try:
            output = subprocess.check_output(
                [Config().ADB_PATH, "shell", "pm", "list", "packages"],
                stderr=subprocess.STDOUT
            ).decode().strip()

            return "package:" in output
        except subprocess.CalledProcessError:
            return False
    
    @staticmethod
    def is_adb_device_exists():
        try:
            output = subprocess.check_output(
                [Config().ADB_PATH, "devices"], stderr=subprocess.STDOUT
            ).decode().strip().splitlines()

            devices = [line.split()[0] for line in output[1:] if "\tdevice" in line]
            if any("127.0.0.1" in d or "emulator-" in d for d in devices):
                return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def is_activity_manager_ready():
        try:
            output = subprocess.check_output(
                [Config().ADB_PATH, "shell", "am", "start", "-a", "android.intent.action.MAIN", "-c", "android.intent.category.HOME"],
                stderr=subprocess.STDOUT
            ).decode().strip()

            return bool(output)
        except subprocess.CalledProcessError:
            return False

    @classmethod
    def is_android_emulator_ready(cls):
        return (cls.__is_boot_completed() 
                and cls.__is_systemui_alive() 
                and cls.__is_surfaceflinger_alive() 
                and cls.__adb_responds()
                and cls.__has_launcher_started()
                and cls.__is_package_manager_ready())