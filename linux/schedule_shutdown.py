import sys
import os


def shut_down(minutes):
    print(">>> schedule_shutdown.py script started... <<<")
    os.system("shutdown -h " + minutes)
    print(">>> schedule_shutdown.py finished. This PC is shutting down in " + minutes + " minutes. <<<")


def shut_down_params():
    if len(sys.argv) >=2:
        minutes = sys.argv[1]
        shut_down(minutes) if minutes.isnumeric() else print("ERROR! Please use a number!")
    else:
        number = input("Please insert the number of minutes:")
        shut_down(number) if number.isnumeric() else print("ERROR! Please use a number!")


if __name__ == '__main__':
    shut_down_params()
