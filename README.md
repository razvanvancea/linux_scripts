# These scripts are shortcuts for your daily tasks
Prerequisites: Python v3.7.6, Docker, Git
Setup:
1. Clone this project in your home directory)
  cd ~/
  git clone https://github.com/razvanvancea/scripts.git
2. Open the .bashrc file (e.g. nano ~/.bashrc)
3. For LINUX users: Add the following aliases at the bottom of the file
  alias sdocker='python3 ~/scripts/linux/startdocker.py'
  alias szalenium='python3 ~/scripts/linux/startzalenium.py'
3. For MACOS users: Add the following aliases at the bottom of the file
alias szalenium='python3 ~/scripts/macos/startzalenium.py'

NOTE: 'sdocker' and 'szalenium' are only shortcut names. They can be renamed with any other name.

4. Save and close the file
5. Reload the .bashrc file, using the following CLI command
  source ~/.bashrc

How to start the scripts?

Start Docker, executing via CLI: sdocker

It it will verify if the Docker daemon is already running. If so, it will notify you by a message. Otherwise, it will start the docker service.

Start Zalenium with a desired number of containers, executing via CLI: szalenium 3

The above command will create 3 containers. If you do not pass the second argument (3), a message asking for the number will be prompted in the terminal, waiting for your input (accepts only numbers).
