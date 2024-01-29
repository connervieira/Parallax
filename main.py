# Parallax

# Copyright (C) 2024 V0LT - Conner Vieira 

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with this program (LICENSE)
# If not, see https://www.gnu.org/licenses/ to read the license agreement.





print("Loading Parallax...")


import os # Required to interact with certain operating system functions
import json # Required to process JSON data


parallax_root_directory = str(os.path.dirname(os.path.realpath(__file__))) # This variable determines the folder path of the root Parallax directory, containing all the program's support files. This should usually automatically recognize itself, but it if it doesn't, you can change it manually.


config = json.load(open(parallax_root_directory + "/config.json")) # Load the configuration database from config.json



import time # Required to add delays and handle dates/times
import subprocess # Required for starting some shell commands
import signal # Required to manage sub-proceses.
import sys
import urllib.request # Required to make network requests
import re # Required to use Regex
import validators # Required to validate URLs
import datetime # Required for converting between timestamps and human readable date/time information
import fnmatch # Required to use wildcards to check strings
import lzma # Required to open and manipulate certain databases.
import math # Required to run more complex math functions.
from geopy.distance import great_circle # Required to calculate distance between locations.
import random # Required to generate random numbers.

import utils # Import the utils.py script.
style = utils.style # Load the style from the utils script.
clear = utils.clear # Load the screen clearing function from the utils script.
process_gpx = utils.process_gpx # Load the GPX processing function from the utils script.
save_to_file = utils.save_to_file # Load the file saving function from the utils script.
add_to_file = utils.add_to_file # Load the file appending function from the utils script.
display_shape = utils.display_shape # Load the shape displaying function from the utils script.
countdown = utils.countdown # Load the timer countdown function from the utils script.
get_gps_location = utils.get_gps_location # Load the function to get the current GPS location.
get_distance = utils.get_distance # Load the function to get the distance between to global positions.
convert_speed = utils.convert_speed # Load the function used to convert speeds from meters per second to other units.
display_number = utils.display_number # Load the function used to display numbers as large ASCII font.
get_cardinal_direction = utils.get_cardinal_direction # Load the function used to convert headings from degrees to cardinal directions.
play_sound = utils.play_sound # Load the function used to play sounds specified in the configuration based on their IDs.
play_voice = utils.play_voice # Load the function used to play voice samples.
display_notice = utils.display_notice  # Load the function used to display notices, warnings, and errors.
calculate_average_speed = utils.calculate_average_speed # Load the function used to calculate the average speed over a given time.

import beacons # Import the beacons.py script.
get_nearby_beacons = beacons.get_nearby_beacons



if ("--autostart" in sys.argv): # Check to see if the autostart flag is in the command-line arguments.
    config["general"]["autostart"] = True # Override the autostart configuration value.




# Display the start-up intro header.
clear() # Clear the screen.
if (config["display"]["ascii_art_header"] == True and config["general"]["autostart"] == False): # Check to see whether the user has configured there to be a large ASCII art header, or a standard text header.
    print(style.red + style.bold)
    print("  ___  _   ___    _   _    _      _   __  __")
    print(" | _ \\/_\\ | _ \\  /_\\ | |  | |    /_\\  \\ \\/ /")
    print(" |  _/ _ \\|   / / _ \\| |__| |__ / _ \\  >  < ")
    print(" |_|/_/ \\_\\_|_\\/_/ \\_\\____|____/_/ \\_\\/_/\\_\\")
    print(style.end)

else: # If the user his disabled the large ASCII art header, then show a simple title header with minimal styling.
    print(style.red + style.bold + "PARALLAX" + style.end)


if (config["display"]["custom_startup_message"] != ""): # Only display the line for the custom message if the user has defined one.
    print(config["display"]["custom_startup_message"]) # Show the user's custom defined start-up message.


if (config["general"]["autostart"] == False): # Only delay to display the start-up header if autostart is disabled.
    time.sleep(float(config["general"]["startup_time"])) # Wait for a certain amount of time, as specified in the configuration to allow the logo to remain on screen.




play_sound("startup")
play_voice("/system/startup.mp3")





current_location = [] # Set the current location variable to a placeholder before starting the main loop.


times_started = 0
while True: # Run forever in a loop until terminated.
    if (config["general"]["autostart"] == True and times_started == 0):
        selection = "1"
    else:
        play_voice("/system/menu/base.mp3")
        clear()
        print("Please select an option.")
        print("1. Information Display")
        print("2. Create Beacon")
        print("3. Tools")
        selection = input("Selection: ")
    times_started += 1 # Increment the number of times Parallax has been started this session.


    if (selection == "1"): # The user has selected to open the information displays.
        beacon_file = config["general"]["working_directory"] + "/" + config["beacons"]["file_name"] # Form the full file path to the beacons file.
        try:
            if (os.path.exists(beacon_file)): # Check to see if the beacon file exists.
                beacons = json.load(open(beacon_file)) # Load the list of beacons from the file.
            else: # The beacon file does not exist.
                beacons = {} # Load a blank placeholder list of beacons.
                display_notice("The beacons file does not exist, so no beacons were loaded. This may be the case if this is the first time Parallax has been run.", level=2)
        except:
            beacons = {} # Load a blank placeholder list of beacons.
            display_notice("The beacon database file could not be loaded. It might be corrupted. No beacons have been loaded.", level=2)


        speed_history = {} # This is a placeholder dictionary that will record the vehicle's speed over time.
        while True: # Run the information display loop forever until terminated.
            try:
                clear() # Clear the console output at the beginning of every cycle.

                last_location = current_location # Set the last location to the current location immediately before we update the current location for the next cycle.
                current_location = get_gps_location() # Get the current location.
                speed_history[time.time()] = current_location[2] # Record the current speed to the speed history.
                average_acceleration = calculate_average_speed(speed_history, config["monitoring"]["launch"]["detection"]["time"]) # Calculate the average acceleration.
                current_speed = round(convert_speed(float(current_location[2]), config["display"]["displays"]["speed"]["unit"])*10**int(config["display"]["displays"]["speed"]["decimal_places"]))/(10**int(config["display"]["displays"]["speed"]["decimal_places"])) # Convert the speed data from the GPS into the units specified by the configuration.


                # Show all configured basic information displays.
                if (config["display"]["displays"]["speed"]["large_display"] == True): # Check to see the large speed display is enabled in the configuration.
                    display_number(current_speed) # Display the current speed in a large ASCII font.

                if (config["display"]["displays"]["time"] == True): # Check to see the time display is enabled in the configuration.
                    print("Time: " + str(time.strftime('%H:%M:%S'))) # Print the current time to the console.

                if (config["display"]["displays"]["date"]  == True): # Check to see the date display is enabled in the configuration.
                    print("Date: " + str(time.strftime('%A, %B %d, %Y'))) # Print the current date to the console.

                if (config["display"]["displays"]["speed"]["small_display"] == True): # Check to see the small speed display is enabled in the configuration.
                    print("Speed: " + str(current_speed) + " " + str(config["display"]["displays"]["speed"]["unit"])) # Print the current speed to the console.

                if (config["display"]["displays"]["location"] == True): # Check to see if the current location display is enabled in the configuration.
                    print("Position: " + str(current_location[0]) + " " + str(current_location[1])) # Print the current location as coordinates to the console.

                if (config["display"]["displays"]["altitude"] == True): # Check to see if the current altitude display is enabled in the configuration.
                    print("Altitude: " + str(current_location[3]) + " meters") # Print the current altitude to the console.

                if (config["display"]["displays"]["heading"]["degrees"] == True or config["display"]["displays"]["heading"]["direction"] == True): # Check to see if the current heading display is enabled in the configuration.
                    if (config["display"]["displays"]["heading"]["direction"] == True and config["display"]["displays"]["heading"]["degrees"] == True): # Check to see if the configuration value to display the current heading in cardinal directions and degrees are both enabled.
                        print("Heading: " + str(get_cardinal_direction(current_location[4])) + " (" + str(current_location[4]) + ")") # Print the current heading to the console in cardinal directions.
                    elif (config["display"]["displays"]["heading"]["direction"] == True): # Check to see if the configuration value to display the current heading in cardinal directions is enabled.
                        print("Heading: " + str(get_cardinal_direction(current_location[4]))) # Print the current heading to the console in cardinal directions.
                    elif (config["display"]["displays"]["heading"]["degrees"] == True): # Check to see if the configuration value to display the current heading in degrees is enabled.
                        print("Heading: " + str(current_location[4])) # Print the current heading to the console in degrees.

                if (config["display"]["displays"]["satellites"] == True): # Check to see if the current altitude display is enabled in the configuration.
                    print("Satellites: " + str(current_location[5])) # Print the current altitude satellite count to the console.


                nearby_beacons = get_nearby_beacons(current_location, beacons) # Determine a list of beacons that are within the alert distance.
                if (len(nearby_beacons) > 0): # Check to see if there is at least one nearby beacon.
                    print("Nearby Beacons:")
                    for beacon in nearby_beacons: # Iterate through each nearby beacon.
                        print("    " + str(beacon["id"]) + ": " + str(beacon["title"]))
                        if (float(beacon["distance"]) <= config["beacons"]["distances"]["thresholds"]["critical"]): # Check to see if this beacon is close enough to trigger a visit.
                            print("        " + "Distance: " + str(beacon["distance"]) + " miles (visited)") # Display the note associated with this beacon.
                        else:
                            print("        " + "Distance: " + str(beacon["distance"]) + " miles") # Display the note associated with this beacon.
                        if (beacon["note"] != "" and beacon["note"] != None): # Check to see if there is a note associated with this beacon.
                            print("        " + "Note: " + str(beacon["note"])) # Display the note associated with this beacon.
                        if (beacon["author"] != "" and beacon["author"] != None): # Check to see if there is an author associated with this beacon.
                            print("        " + "Author: " + str(beacon["author"])) # Display the note associated with this beacon.

                        if (float(beacon["distance"]) <= config["beacons"]["distances"]["thresholds"]["critical"]): # Check to see if this beacon is close enough to trigger a visit.
                            if (time.time() - beacons[beacon["id"]]["time"]["seen"] > 30): # Check to see if it has been at least 30 seconds since this beacon was visited. This prevents what the user would call the same visit from being logged repeatedly if they park nearby.
                                beacons[beacon["id"]]["visits"].append(round(time.time())) # Add this visit to the complete list of visits.
                            beacons[beacon["id"]]["time"]["seen"] = time.time() # Update the last time that this beacon was visited.

                        del(beacon["id"]) # Remove the temporary values from this beacon before saving it.
                        del(beacon["distance"]) # Remove the temporary values from this beacon before saving it.
                        beacon_file = config["general"]["working_directory"] + "/" + config["beacons"]["file_name"] # Form the full file path to the beacons file.
                        save_to_file(beacon_file, json.dumps(beacons), True) # Save the updated beacon dictionary to disk.


                if (average_acceleration > float(config["monitoring"]["launch"]["detection"]["threshold"])): # Check to see if the average acceleration exceeds the launch detection threshold.
                    print("Launch mode active (" + str(average_speed) + " m/s^2)")
                    if (time.time() - last_launch_time > float(config["monitoring"]["launch"]["detection"]["cooldown"])): # Check to see if a minimum amount of seconds have passed since Parallax has alerted to a launch event.
                        play_voice("/alerts/speed/launch.mp3")
                    last_launch_time = time.time() # Record the last time that a launch was detected as the current time.
                    print("Acceleration: " + str(average_speed) + " m/s^s")



                time.sleep(float(config["general"]["refresh_delay"])) # Wait for a certain amount of time, as specified in the configuration.

            except KeyboardInterrupt: # Wait for the user to press Control + C, then break the loop and return to the main menu.
                break # Break the information display loop.




    elif (selection == "2"): # The user has selected the beacon option.
        clear() # Clear the console output at the beginning of every cycle.

        input("Press enter to drop beacon...")
        current_location = get_gps_location() # Get the current location.
        play_voice("/system/menu/options/beacon/start.mp3")

        beacon_id = "" # Initialize the beacon ID value.
        while (beacon_id == ""): # Repeatedly prompt the user until a beacon ID is entered.
            beacon_id = input("ID: ") # Prompt the user to enter a beacon ID.
            if (beacon_id == ""): # Check to see if a beacon ID was entered.
                print("A unique beacon ID is required!") # Inform the user that a beacon ID is required.
        beacon_title = input("Title: ") # Prompt the user to enter a friendly title for the beacon.
        beacon_note = input("Note: ") # Prompt the user to associate a note with the beacon.
        beacon_tags = input("Tags: ") # Prompt the user to enter one or more space-separated tags.
        if (config["beacons"]["author"] == ""): # Check to see if the author setting was left blank.
            beacon_author = input("Author: ") # Prompt the user to enter an author name for this beacon.
        else:
            beacon_author = config["beacons"]["author"] # Set the author of this beacon to the author set in the configuration.

        beacon_file = config["general"]["working_directory"] + "/" + config["beacons"]["file_name"] # Form the full file path to the beacons file.

        if (os.path.exists(beacon_file)): # Check to see if the beacon file exists.
            beacons = json.load(open(beacon_file)) # Load the dictionary of beacons from the file.
        else: # The beacon file does not exist.
            beacons = {} # Load a blank placeholder dictionary of beacons.

        beacon_data = {}
        beacon_data["location"] = {"lon": current_location[0], "lat": current_location[1], "alt": current_location[3]}
        beacon_data["title"] = beacon_title
        beacon_data["note"] = beacon_note
        beacon_data["tags"] = beacon_tags.split(",")
        beacon_data["author"] = beacon_author
        beacon_data["time"] = {}
        beacon_data["time"]["created"] = time.time()
        beacon_data["time"]["modified"] = time.time()
        beacon_data["time"]["seen"] = time.time()
        beacon_data["visits"] = [] # This will be used to hold each instance that the user visits this beacon.

        for key, tag in enumerate(beacon_data["tags"]): # Iterate through each tag entered by the user.
            beacon_data["tags"][key] = tag.strip() # Remove any trailing or leading whitespaces from each tag.

        beacons[beacon_id] = beacon_data # Add this beacon to the complete list of beacons.
        save_to_file(beacon_file, json.dumps(beacons), True) # Save the beacon list to disk.



    elif (selection == "3"): # The user has selected the tools menu.
        clear()
        print("Please select an option.")
        print("0. Exit")
        print("1. Stopwatch")
        print("2. Timer")
        selection = input("Selection: ")
        clear() # Clear the console output after receiving the user's selection.

        if (selection == "0"): # The user has selected to exit the tools menu.
            pass

        elif (selection == "1"): # The user has selected the stopwatch from the tools menu.
            try:
                stopwatch_time = 0 # This variable will be incremented by 1 every second to display the current time.
                input("Press enter to start stopwatch...") # Wait for the user to press enter before starting the stopwatch.
                stopwatch_start_time = round(time.time() * 1000) # Get the current time in milliseconds when the stopwatch is started.
                while True: # Repeat forever until terminated.
                    clear() # Clear the console output.
                    print("Time: " + str(stopwatch_time) + " seconds") # Show the current stopwatch time.
                    time.sleep(1) # Wait 1 second before repeating the loop.
                    stopwatch_time = stopwatch_time + 1 # Increment the stopwatch time by 1 second.
                    
            except KeyboardInterrupt: # Wait for the user to press Control + C, then break the loop and return to the main menu.
                clear() # Clear the console output.
                print("Time: " + str((round(time.time() * 1000) - stopwatch_start_time)/1000) + " seconds") # Show the final stopwatch time after the loop is terminated.
                input("Press enter to continue...") # Wait for the user to press enter before continuing.


        elif (selection == "2"): # The user has selected the timer from the tools menu.
            try:
                timer_length_input = str(input("Timer length: ")).split(":") # Prompt the user to enter a timer length, then split the input at colons.

                timer_length = 0.0 # This is a placeholder variable that will be used to hold the length of the timer in seconds.

                # Parse the length of the timer based on the number of elements in the list derived from the user input.
                if (len(timer_length_input) == 1): # There is only one element in the user input, so just add seconds to the timer.
                    timer_length = timer_length + float(timer_length_input[0]) # Add seconds to the timer.
                elif (len(timer_length_input) == 2): # There are two elements in the user input, so add minutes and seconds to the timer.
                    timer_length = timer_length + (float(timer_length_input[0])*60) # Add minutes to the timer.
                    timer_length = timer_length + float(timer_length_input[1]) # Add seconds to the timer.
                elif (len(timer_length_input) == 3): # There are three elements in the user input, so add hours, minutes, and seconds to the timer.
                    timer_length = timer_length + (float(timer_length_input[0])*3600) # Add hours to the timer.
                    timer_length = timer_length + (float(timer_length_input[1])*60) # Add minutes to the timer.
                    timer_length = timer_length + float(timer_length_input[2]) # Add seconds to the timer.
                elif (len(timer_length_input) == 4): # There are four elements in the user input, so add days, hours, minutes, and seconds to the timer.
                    timer_length = timer_length + (float(timer_length_input[0])*86400) # Add days to the timer.
                    timer_length = timer_length + (float(timer_length_input[1])*3600) # Add hours to the timer.
                    timer_length = timer_length + (float(timer_length_input[2])*60) # Add minutes to the timer.
                    timer_length = timer_length + float(timer_length_input[3]) # Add seconds to the timer.


                timer_length = round(timer_length) # Round the timer length to the nearest second.


                input("Press enter to start timer...") # Wait for the user to press enter before starting the timer.
                while True: # Repeat forever until terminated.
                    clear() # Clear the console output.
                    print("Time: " + str(timer_length) + " seconds") # Show the current timer time.
                    time.sleep(1) # Wait 1 second before repeating the loop.
                    timer_length = timer_length - 1 # Increment the timer down by 1 second.

                    if (timer_length <= 0): # Check to see if the timer is complete by checking to see if the timer length is less than or equal to 0 seconds.
                        break # Terminate the timer loop.

                clear() # Clear the console output.
                print("Timer complete!") # Inform the user that the timer has completed.
                input("Press enter to continue...") # Wait for the user to press enter before continuing.
                    
            except KeyboardInterrupt: # Wait for the user to press Control + C, then break the loop and return to the main menu.
                clear() # Clear the console output.
                print("Timer cancelled") # Inform the user that the timer has been cancelled.
                input("Press enter to continue...") # Wait for the user to press enter before continuing.


    else:
        print("Invalid selection")
        input("Press enter to continue...")
