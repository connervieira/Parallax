# Parallax

# Copyright (C) 2024 V0LT - Conner Vieira 

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by# the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program (LICENSE.md)
# If not, see https://www.gnu.org/licenses/ to read the license agreement.





# This script contains several funtions and classes used in main.py







import os # Required to interact with certain operating system functions
import json # Required to process JSON data

parallax_root_directory = str(os.path.dirname(os.path.realpath(__file__))) # This variable determines the folder path of the root Parallax directory. This should usually automatically recognize itself, but it if it doesn't, you can change it manually.

config = json.load(open(parallax_root_directory + "/config.json")) # Load the configuration database from config.json


import time # Required to add delays and handle dates/times
import subprocess # Required for starting some shell commands
import sys
import urllib.request # Required to make network requests
import requests # Required to make network requests
import re # Required to use Regex
import validators # Required to validate URLs
import datetime # Required for converting between timestamps and human readable date/time information
from xml.dom import minidom # Required for processing GPX data
import fnmatch # Required to use wildcards to check strings
import lzma # Required to load ExCam database
import math # Required to run more complex math calculations
from geopy.distance import great_circle # Required to calculate distance between locations.
from gps import * # Required to access GPS information.
import gpsd
from mutagen.mp3 import MP3 # Required to access information about MP3 files.






# This function will be used to process GPX files into a Python dictionary.
def process_gpx(gpx_file):
    gpx_file = open(gpx_file, 'r') # Open the GPX document.

    xmldoc = minidom.parse(gpx_file) # Load the full XML GPX document.

    track = xmldoc.getElementsByTagName('trkpt') # Get all of the location information from the GPX document.
    timing = xmldoc.getElementsByTagName('time') # Get all of the timing information from the GPX document.

    gpx_data = {} 

    for i in range(0, len(timing)): # Iterate through each point in the GPX file.
        point_lat = track[i].getAttribute('lat') # Get the latitude for this point.
        point_lon = track[i].getAttribute('lon') # Get the longitude for this point.
        point_time = str(timing[i].toxml().replace("<time>", "").replace("</time>", "").replace("Z", "").replace("T", " ")) # Get the time for this point in human readable text format.

        point_time = round(time.mktime(datetime.datetime.strptime(point_time, "%Y-%m-%d %H:%M:%S").timetuple())) # Convert the human readable timestamp into a Unix timestamp.

        gpx_data[point_time] = {"lat":point_lat, "lon":point_lon} # Add this point to the decoded GPX data.


    return gpx_data




# Define the function that will be used to clear the screen.
def clear():
    os.system("clear")



# Define the function that will be used to save files for exported data.
def save_to_file(file_name, contents, silence=False):
    fh = None
    success = False
    try:
        fh = open(file_name, 'w')
        fh.write(contents)
        success = True   
        if (silence == False):
            print("Successfully saved at " + file_name + ".")
    except IOError as e:
        success = False
        if (silence == False):
            print(e)
            print("Failed to save!")
    finally:
        try:
            if fh:
                fh.close()
        except:
            success = False
    return success



# Define the fuction that will be used to add to the end of a file.
def add_to_file(file_name, contents, silence=False):
    fh = None
    success = False
    try:
        fh = open(file_name, 'a')
        fh.write(contents)
        success = True
        if (silence == False):
            print("Successfully saved at " + file_name + ".")
    except IOError as e:
        success = False
        if (silence == False):
            print(e)
            print("Failed to save!")
    finally:
        try:
            if fh:
                fh.close()
        except:
            success = False
    return success




# This is a simple function used to display large ASCII shapes.
def display_shape(shape):
    if (shape == "square"):
        print(style.bold)
        print("######################")
        print("######################")
        print("######################")
        print("######################")
        print("######################")
        print("######################")
        print("######################")
        print("######################")
        print("######################")
        print("######################")
        print("######################")
        print("######################")
        print(style.end)

    elif (shape == "circle"):
        print(style.bold)
        print("        ######")
        print("     ############")
        print("   ################")
        print("  ##################")
        print(" ####################")
        print("######################")
        print("######################")
        print("######################")
        print(" ####################")
        print("  ##################")
        print("   ################")
        print("     ############")
        print("        ######")
        print(style.end)

    elif (shape == "triangle"):
        print(style.bold)
        print("           #")
        print("          ###")
        print("         #####")
        print("        #######")
        print("       #########")
        print("      ###########")
        print("     #############")
        print("    ###############")
        print("   #################")
        print("  ###################")
        print(" #####################")
        print("#######################")
        print(style.end)

    elif (shape == "diamond"):
        print(style.bold)
        print("           #")
        print("          ###")
        print("         #####")
        print("        #######")
        print("       #########")
        print("      ###########")
        print("     #############")
        print("      ###########")
        print("       #########")
        print("        #######")
        print("         #####")
        print("          ###")
        print("           #")
        print(style.end)

    elif (shape == "cross"):
        print(style.bold)
        print("########              ########")
        print("  ########          ########")
        print("    ########      ########")
        print("      ########  ########")
        print("        ##############")
        print("          ##########")
        print("        ##############")
        print("      ########  ########")
        print("    ########      ########")
        print("  ########          ########")
        print("########              ########")
        print(style.end)

    elif (shape == "horizontal"):
        print(style.bold)
        print("############################")
        print("############################")
        print("############################")
        print("############################")
        print(style.end)

    elif (shape == "vertical"):
        print(style.bold)
        print("           ######")
        print("           ######")
        print("           ######")
        print("           ######")
        print("           ######")
        print("           ######")
        print("           ######")
        print("           ######")
        print("           ######")
        print("           ######")
        print("           ######")
        print("           ######")
        print(style.end)


# Define some styling information
class style:
    # Define colors
    red = '\033[91m'
    yellow = '\033[93m'
    green = '\033[92m'
    blue = '\033[94m'
    cyan = '\033[96m'
    pink = '\033[95m'
    purple = '\033[1;35m'
    gray = '\033[1;37m'
    brown = '\033[0;33m'
    black = '\033[0;30m'


    # Define text decoration
    bold = '\033[1m'
    underline = '\033[4m'
    italic = '\033[3m'
    faint = '\033[2m'

    # Define styling end marker
    end = '\033[0m'




# Define a function for running a countdown timer.
def countdown(timer):
    for iteration in range(1, timer + 1): # Loop however many times specified by the `timer` variable.
        print(str(timer - iteration + 1)) # Display the current countdown number for this iteration, but subtracting the current iteration count from the total timer length.
        time.sleep(1) # Wait for 1 second.






# Define the function that will be used to get the current GPS coordinates.
def get_gps_location(demo=False): # Placeholder that should be updated at a later date.
    if (config["general"]["gps"]["demo_mode"]["enabled"] == True): # Check to see if GPS demo mode is enabled in the configuration.
        return float(config["general"]["gps"]["demo_mode"]["longitude"]), float(config["general"]["gps"]["demo_mode"]["latitude"]), float(config["general"]["gps"]["demo_mode"]["speed"]), float(config["general"]["gps"]["demo_mode"]["altitude"]), float(config["general"]["gps"]["demo_mode"]["heading"]), int(config["general"]["gps"]["demo_mode"]["satellites"]) # Return the sample GPS information defined in the configuration.
    else: # GPS demo mode is disabled, so attempt to get the actual GPS data from GPSD.
        try: # Don't terminate the entire script if the GPS location fails to be aquired.
            if (config["general"]["gps"]["provider"] == "gpsd"): # Check to see if Parallax is configured to use the GPSD location provider.
                gpsd.connect() # Connect to the GPS daemon.
                gps_data_packet = gpsd.get_current() # Get the current information.
                return gps_data_packet.position()[0], gps_data_packet.position()[1], gps_data_packet.speed(), gps_data_packet.altitude(), gps_data_packet.movement()["track"], gps_data_packet.sats # Return GPS information.
            elif (config["general"]["gps"]["provider"] == "termux"): # Check to see if Parallax is configured to use the Termux API location provider.
                  raw_termux_response = str(os.popen("termux-location").read()) # Execute the Termux location command.
                  termux_response = json.loads(raw_termux_response) # Load the location information from the Termux response.
                  debug_message("Received termux-location information")
                  return termux_response["latitude"], termux_response["longitude"], termux_response["speed"], termux_response["altitude"], termux_response["bearing"], 0 # Return the fetched GPS information.
        except: # If the current location can't be established, then return placeholder location data.
            return 0.0000, -0.0000, 0.0, 0.0, 0.0, 0 # Return a default placeholder location.




# Define a simple function to calculate the approximate distance between two points in miles.
def get_distance(lat1, lon1, lat2, lon2):
    return great_circle((lat1, lon1), (lat2, lon2)).miles








def convert_speed(speed, unit="mph"): # This function is used to convert speeds from meters per second, to other units.
    unit = unit.lower() # Convert the unit to all lowercase in order to make it easier to work with and remove inconsistencies in configuration setups.

    if (unit == "kph"): # Convert the speed to kilometers per hour.
        speed = speed * 3.6 # The speed is already measured in kilometers per hour, so there is no reason to convert it.
    elif (unit == "mph"): # Convert the speed to miles per hour.
        speed = speed * 2.236936
    elif (unit == "mps"): # Convert the speed to meters per second.
        speed = speed # The speed is already measured in meters per second, so there is no reason to convert it.
    elif (unit == "knot"): # Convert the speed to knots.
        speed = speed * 1.943844
    elif (unit == "fps"): # Convert the speed to feet per second.
        speed = speed * 3.28084
    else: # If an invalid unit was supplied, then simply return a speed of zero.
        speed = 0

    return speed # Return the convert speed.





def display_number(display_number="0"): # This function is used to display a number as a large ASCII character.
    numbers = {} # Create a placeholder dictionary for all numbers.
    numbers["."] = ["    ", "    ", "    ", "    ", "    ", "    ", " ## ", " ## "] # Define each line in the ASCII art for zero.
    numbers["0"] = [" $$$$$$\\  ", "$$$ __$$\\ ", "$$$$\\ $$ |", "$$\\$$\\$$ |", "$$ \\$$$$ |", "$$ |\\$$$ |", "\\$$$$$$  /", " \\______/ "] # Define each line in the ASCII art for zero.
    numbers["1"] = ["  $$\\   ", "$$$$ |  ", "\\_$$ |  ", "  $$ |  ", "  $$ |  ", "  $$ |  ", "$$$$$$\ ", "\\______|"] # Define each line in the ASCII art for one.
    numbers["2"] = [" $$$$$$\\  ", "$$  __$$\\ ", "\\__/  $$ |", " $$$$$$  |", "$$  ____/ ", "$$ |      ", "$$$$$$$$\\ ", "\\________|"] # Define each line in the ASCII art for two.
    numbers["3"] = [" $$$$$$\\  ", "$$ ___$$\\ ", "\\_/   $$ |", "  $$$$$ / ", "  \\___$$\\ ", "$$\   $$ |", "\\$$$$$$  |", " \\______/ "] # Define each line in the ASCII art for three.
    numbers["4"] = ["$$\\   $$\\ ", "$$ |  $$ |", "$$ |  $$ |", "$$$$$$$$ |", "\\_____$$ |", "      $$ |", "      $$ |", "      \\__|"] # Define each line in the ASCII art for four.
    numbers["5"] = ["$$$$$$$\\  ", "$$  ____| ", "$$ |      ", "$$$$$$$\\  ", "\_____$$\\ ", "$$\\   $$ |", "\\$$$$$$  |", " \\______/ "] # Define each line in the ASCII art for five.
    numbers["6"] = [" $$$$$$\\  ", "$$  __$$\\ ", "$$ /  \\__|", "$$$$$$$\\  ", "$$  __$$\\ ", "$$ /  $$ |", " $$$$$$  |", " \\______/ "] # Define each line in the ASCII art for six.
    numbers["7"] = ["$$$$$$$$\\ ", "\\____$$  |", "    $$  / ", "   $$  /  ", "  $$  /   ", " $$  /    ", "$$  /     ", "\\__/      "] # Define each line in the ASCII art for seven.
    numbers["8"] = [" $$$$$$\\  ", "$$  __$$\\ ", "$$ /  $$ |", " $$$$$$  |", "$$  __$$< ", "$$ /  $$ |", "\\$$$$$$  |", " \\______/ "] # Define each line in the ASCII art for eight.
    numbers["9"] = [" $$$$$$\\  ", "$$  __$$\\ ", "$$ /  $$ |", "\\$$$$$$$ |", " \\____$$ |", "$$\\   $$ |", "\\$$$$$$  |", " \\______/ "] # Define each line in the ASCII art for nine.

    display_lines = {} # Create a placeholder for each line that will be printed to the console.

    for line_count in range(0, 8): # Iterate through each of the 8 lines that the output will have.
        display_lines[line_count] = "" # Set each line to an empty placeholder string.

    for display_character in str(display_number): # Iterate through each character that needs to be displayed.
        for individual_display_line in range(0, 8): # Iterate through each line that will be displayed to the console output.
            display_lines[individual_display_line] = str(display_lines[individual_display_line]) + numbers[str(display_character)][individual_display_line] # Add each number to each line of the output.

    for line_index in display_lines: # Iterate through each line that needs to displayed.
        print(display_lines[line_index]) # Print each individual line.





def get_cardinal_direction(heading=0): # Define the function used to convert degrees into cardinal directions.
    direction = round(heading / 45) # Divide the current heading in degrees into 8 segments, each representing a cardinal direction or sub-cardinal direction.
    if (direction == 0 or direction == 8):
        return "N"
    elif (direction == 1):
        return "NE"
    elif (direction == 2):
        return "E"
    elif (direction == 3):
        return "SE"
    elif (direction == 4):
        return "S"
    elif (direction == 5):
        return "SW"
    elif (direction == 6):
        return "W"
    elif (direction == 7):
        return "NW"
    else: # This case should never occur, unless the degrees supplied to the function exceeded 360 or were below 0.
        return "ERROR" # Return an error indicating that the information supplied to the function was invalid.






def play_sound(sound_id):
    if (str(sound_id) in config["audio"]["sounds"]): # Check to see that a sound with the specified sound ID exists in the configuration.
        if (int(config["audio"]["sounds"][str(sound_id)]["repeat"]) > 0): # Check to see if this sound effect is enabled.
            if (os.path.exists(str(config["audio"]["sounds"][str(sound_id)]["path"])) == True and str(config["audio"]["sounds"][str(sound_id)]["path"]) != ""): # Check to see if the sound file associated with the specified sound ID actually exists.
                for i in range(0, int(config["audio"]["sounds"][str(sound_id)]["repeat"])): # Repeat the sound several times, if the configuration says to do so.
                    os.system("mpg321 " + config["audio"]["sounds"][str(sound_id)]["path"] + " > /dev/null 2>&1 &") # Play the sound file associated with this sound ID in the configuration.
                    time.sleep(float(config["audio"]["sounds"][str(sound_id)]["delay"])) # Wait before playing the sound again.
            elif (str(config["audio"]["sounds"][str(sound_id)]["path"]) == ""): # The file path associated with this sound ID is left blank, and therefore the sound can't be played.
                print(style.yellow + "Warning: The sound file path associated with sound ID (" + str(sound_id) + ") is blank." + style.end)
                input("Press enter to continue...")
            elif (os.path.exists(str(config["audio"]["sounds"][str(sound_id)]["path"])) == False): # The file path associated with this sound ID does not exist, and therefore the sound can't be played.
                print(style.yellow + "Warning: The sound file path associated with sound ID (" + str(sound_id) + ") does not exist." + style.end)
                input("Press enter to continue...")
    else: # No sound with this ID exists in the configuration database, and therefore the sound can't be played.
        print(style.yellow + "Warning: No sound with the ID (" + str(sound_id) + ") exists in the configuration." + style.end)
        input("Press enter to continue...")


def play_voice(sound_file_path):
    if (config["audio"]["voice"]["enabled"] == True):
        full_sound_file_path = config["audio"]["voice"]["base_directory"] + sound_file_path
        if (os.path.exists(full_sound_file_path) == True):

            audio_file = MP3(full_sound_file_path) # Load the audio file.
            os.system("mpg321 " + full_sound_file_path + " > /dev/null 2>&1 &") # Play the sound file.
            time.sleep(audio_file.info.length) # Wait for the audio file to finish.
            del audio_file # Delete the audio file from memory.
        else:
            print(style.yellow + "Warning: The specified voice sample (" + full_sound_file_path + ") does not exist." + style.end)



# This function displays notices, warnings, and errors.
def display_notice(message, level=1):
    level = int(level) # Convert the message level to an integer.

    if (level == 1): # The level is set to 1, indicating a standard notice.
        print(str(message))
        if (config["display"]["notices"]["1"]["wait_for_input"] == True): # Check to see if the configuration indicates to wait for user input before continuing.
            input("Press enter to continue...") # Wait for the user to press enter before continuning.
        else: # If the configuration doesn't indicate to wait for user input, then wait for a delay specified in the configuration for this notice level.
            time.sleep(float(config["display"]["notices"]["1"]["delay"])) # Wait for the delay specified in the configuration.

    elif (level == 2): # The level is set to 2, indicating a warning.
        print(style.yellow + "Warning: " + str(message) + style.end)
        if (config["display"]["notices"]["2"]["wait_for_input"] == True): # Check to see if the configuration indicates to wait for user input before continuing.
            input("Press enter to continue...") # Wait for the user to press enter before continuning.
        else: # If the configuration doesn't indicate to wait for user input, then wait for a delay specified in the configuration for this notice level.
            time.sleep(float(config["display"]["notices"]["2"]["delay"])) # Wait for the delay specified in the configuration.

    elif (level == 3): # The level is set to 3, indicating an error.
        print(style.red + "Error: " + str(message) + style.end)
        if (config["display"]["notices"]["3"]["wait_for_input"] == True): # Check to see if the configuration indicates to wait for user input before continuing.
            input("Press enter to continue...") # Wait for the user to press enter before continuning.
        else: # If the configuration doesn't indicate to wait for user input, then wait for a delay specified in the configuration for this notice level.
            time.sleep(float(config["display"]["notices"]["3"]["delay"])) # Wait for the delay specified in the configuration.



# This function calculates the average change in speed given a dictionary of speed datapoints and a target age (in seconds) to calculate the acceleration over.
def calculate_average_speed(speed_history, target_age):
    if (len(speed_history) >= 2): # Make sure there are at least 2 entries in the speed history before attempting to calculate the average change in speed.
        target_time = time.time() - target_age
        current_closest_time = 0 # This will hold the time from the speed history that is the closest to the target time.
        for history_entry_time in speed_history.keys(): # Iterate through each timestamp in the speed history.
            if (abs(history_entry_time - target_time) < abs(current_closest_time - target_time)): # Check to see if this timestamp is closer than the current closest.
                current_closest_time = history_entry_time # Make this timestamp the new current closest.
        
        most_recent_time = sorted(speed_history.keys())[-1] # Get the time of the most recent datapoint in the speed history.
        time_difference = most_recent_time - current_closest_time # Calculate the exact time difference between the two speed datapoints.
        speed_difference = speed_history[most_recent_time] - speed_history[current_closest_time] # Calculate the speed difference between the two speed datapoints.
        if (time_difference == 0):
            average_acceleration = 0
        else:
            average_acceleration = speed_difference / time_difference # Calculate the average acceleration.
    else: # If there aren't enough datapoints to calculate the average speed, default to an acceleration of 0 m/s/s.
        average_acceleration = 0

    return average_acceleration
