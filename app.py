import datetime
import platform

print("===================================")
print("   Welcome to Python CI Demo")
print("===================================")

current_time = datetime.datetime.now()

print(f"Current Time : {current_time}")
print(f"Python Version : {platform.python_version()}")
print(f"Operating System : {platform.system()}")

print("Application executed successfully!")