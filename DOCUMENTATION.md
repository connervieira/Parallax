# Documentation

This document contains the information you need to know to set up and use Parallax.


## Installation

This is the installation process for Parallax and all of it's dependencies. This process is written assuming you're running a Debian based distribution of GNU/Linux, but it's theoretically possible to get Parallax to function on MacOS and BSD as well.

1. Install the required Python packages. (Required)
    - `pip3 install validators gps geopy gpsd-py3 gpsd requests`
2. Install GPSD (Required)
    - GPSD is required for Parallax to communicate with GPS devices.
    - You can install GPSD using this command on a Debian based Linux machine: `sudo apt-get install gpsd gpsd-clients`
    - It may also be necessary to start GPSD. You can test to see if GPSD is working properly using the `cgps` command.
3. Optionally, install MPG321 (Recommended)
    - Parallax requires MPG321 in order to play audio effects for alerts.
    - If you don't install MPG321, Parallax will encounter errors when audio alerts are enabled in the configuration.
    - You can install MPG321 using the following command on a Debian based Linux machine: `sudo apt-get install mpg321`
4. Optionally, install RaspAP
    - If you're installing Parallax on a Raspberry Pi, you may find it useful to install a program like [RaspAP](https://github.com/RaspAP/raspap-webgui) (or similar program) in order to remotely manage your Parallax instance, and eliminate the need for a full keyboard and display.
    - Parallax works entirely via command line, meaning any set up that enables SSH access to the host will allow for remote management of Parallax.
    - If you already have an access point installed in the same area as Parallax, you can simply connect Parallax to it, and use SSH on a separate device to access the instance remotely.
5. Download Parallax
    - Download Parallax from wherever you received it, and extract it to somewhere on your filesystem. The Parallax folder can be placed anywhere with appropriate permissions, but don't place any external files in the Parallax root directory to prevent any conflicts.


## Configuration

After installing Parallax, you should do some quick configuration in order to get the most out of it.

1. Open the Parallax configuration
    - Open the `config.json` file in the Parallax root directory using your text editor of choice.
2. Make configuration changes
    - All configuration values are explained extensively in the [CONFIGURATION.md](CONFIGURATION.md) document.
    - Make changes to any of the configuration values to better fit your usage context.
    - This step is very open-ended. Depending on your situation, you may leave the configuration almost untouched, while other situations might involve intensive changes.
3. Depending on the platform, Parallax might not be able to locate the `config.json` file. If you encounter issues during the steps described in the "Usage" section, you may need to manually set Parallax's directory. Under normal circumstances, this shouldn't be necessary.
    - At the top of the `main.py` and `utils.py` scripts, you should see a variable titled `parallax_root_directory`. By default, a Python function is used to find the current directory of the script.
    - If you receive errors related to missing configuration files when trying to run Parallax, try setting this variable to a static file path.
    - Example:
        - `parallax_root_directory = "/home/user/Parallax/"`


## Usage

After configuring Parallax, you can try it out for the first time!

1. Run Parallax
    - To run Parallax, simply navigate to it's folder, then run `main.py` using the `python3` command.
        - `python3 main.py`
    - After Parallax finishes loading, you should see a quick message displaying the "Parallax" name, followed by the main menu.
2. Use Parallax
    - Parallax uses a nested menu system. At the top of the hierarchy is the main menu. Simply enter the number associated with an option, then press enter to select it.
    - Upon selecting an option, it's respective menu of function will open. Once you've finished using a particular menu or function, press `Ctrl + C` to return to the previous menu.
3. Quit Parallax
    - When you finish using Parallax, simply press `Ctrl + C` repeatedly until the program is terminated.
