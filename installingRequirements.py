import os
def installing_requirements():
    print("Installing requirements.")
    os.system("sudo apt-get install python3-pip")
    os.system("pip3 install -r requirements.txt")
installing_requirements()