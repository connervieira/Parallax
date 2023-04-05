# beacons.py
# This script contains functions concerning the handling of beacons.

# Copyright (C) 2023 V0LT - Conner Vieira 

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License along with this program (LICENSE)
# If not, see https://www.gnu.org/licenses/ to read the license agreement.


import os # Required to interact with certain operating system functions
import json # Required to process JSON data

parallax_root_directory = str(os.path.dirname(os.path.realpath(__file__))) # This variable determines the folder path of the root Parallax directory, containing all the program's support files. This should usually automatically recognize itself, but it if it doesn't, you can change it manually.
config = json.load(open(parallax_root_directory + "/config.json")) # Load the configuration database from config.json

import utils # Import the utils.py script.
get_distance = utils.get_distance # Load the function to get the distance between to global positions.
display_notice = utils.display_notice  # Load the function used to display notices, warnings, and errors.

import math



def get_nearby_beacons(current_location, beacons):
    current_lon = current_location[0]
    current_lat = current_location[1]
    current_alt = current_location[3]

    for beacon in beacons:
        distance = get_distance(current_lat, current_lon, beacon["location"]["lat"], beacon["location"]["lon"])
        if (config["beacons"]["distances"]["consider_altitude"] == True):
            altitude_difference = current_alt - beacon["location"]["alt"]
            distance = math.sqrt(distance**2 + altitude_difference**2) # TODO: Verify that this works as expected.

    # TODO: Return list of nearby beacons.
