# Configuration

This document describes the configuration values found `config.json`.


## General Configuration

This section of configuration values will effect Parallax's general operation.

- `working_directory` is a string that sets the absolute path of the working directory.
    - The working directory is where Parallax stores information while it runs.
- `gps` contains settings for configuring GPS functionality.
    - `provider` is a string that determines which GPS provider Parallax will use to fetch location information.
        - This value can only be set to one of the following values:
            - `"gpsd"` for GPSD.
            - `"termux"` for Termux API location provider (`termux-location`).
    - `demo_mode` is used to supply Parallax with fake GPS data for sake of demonstration purposes.
        - To use this feature, simply set `enabled` to `true`, then set each GPS variable to any value you want. Parallax will use this fake information whenever it would otherwise poll the GPS for information.
- `refresh_delay` is a decimal number that determines how long Parallax will wait between refreshes in seconds. Generally, 1 second is appropriate, but you can increase or decrease the delay to improve precision, or save processing power.
- `startup_time` is a decimal number that determines how long Parallax will wait after showing the startup logo, in seconds.
    - Increasing this value will allow the Parallax header to remain visible for longer.
    - Decreasing this value will allow Parallax to start up quicker.


## Beacon Configuration

This section of configuration values effect the behavior of beacons.

- `file_name` is a string that determines the file name the Parallax will use for the file that holds the beacon database.
    - This file should be a `.json` file.
- `author` is a string that sets the author of each beacon when it is created.
    - When this value is left blank, the user will be prompted to enter the author's name each time they create a beacon.
- `distances` contains configuration values regarding distances to beacons.
    - `thresholds` contain values that set distance thresholds for various events.
        - `alert` is a decimal number sets the distance (in miles) to beacons where a notification will be displayed while the information display is active.
        - `critical` is a decimal number that set the distance (in miles) to a beacon, where Parallax considers the beacon to be visited.
    - `consider_altitude` is a boolean value that determines whether altitude will be considered when calculating distance.
        - Under normal circumstances, this won't have much of an effect on alert behavior, since the GPS location will usually be at a similar altitude to the altitude of the beacon. As such, this should usually be set to `false` to reduce the unpredictable effects of GPS jitter.
        - The altitude calculation does not account for the curvature of the planet.
            - Take for example, a plane flying towards a target that is 200 miles away, but at the same altitude as the plane. In reality, the target will be lower than the plane, relative to the pilot, since the Earth curves down and away from them. Parallax does not account for this, since it makes more intuitive sense to conduct calculations assuming the target is directly ahead.
            - Across shorter distances, this characteristic doesn't make a meaningful impcat on the accuracy of distance calculations.


## Display Configuration

This section of configuration values effect Parallax's visual displays.

- `displays` contains configuration values that allow the user to turn on and off each information display individually.
    - This allows the user to control what information they can see while driving.
    - `time` can be toggled on and off.
    - `date` can be toggled on and off.
    - `speed` has several configuration values.
        - `small_display` toggles the small, single line speed text display on and off.
        - `large_display` toggles the large, ASCII font speed display on and off
        - `decimal_places` determines how many decimal places will be displayed in both speed display types.
        - `unit` determines the unit of speed that Parallax will use.
            - "kph" for kilometers-per-hour
            - "mph" for miles-per-hour
            - "mps" for meters-per-second
            - "knot" for knots
            - "fps" for feet-per-second
    - `location` can be toggled on and off.
    - `altitude` can be toggled on and off.
    - `heading` has several configuration values.
        - `degrees` determines whether or not the current heading will be displayed in degrees off north. When both `degrees` and `direction` are enabled, the degrees will be displayed in parenthesis after the cardinal direction.
        - `direction` determines whether or not the current heading will be displayed as a cardinal direction, such as 'N', 'SW', or 'E'.
    - `satellites` can be toggled on and off.
- `ascii_art_header` is a boolean value that determines whether or not Parallax will display a large title header upon start-up.
    - This this setting is set to `false`, Parallax will instead display a small, single-line title.
- `custom_startup_message` is a string that defines a string that will be displayed the Parallax title upon start-up.
- `notices` contains all of the different levels of notices Parallax can show the user when issues are encountered. Level 1 indicates basic notices, level 2 indicates warnings, and level 3 indicates errors.
    - Each notice level has the following configuration values:
        - `wait_for_input` indicates whether Parallax should pause, and prompt the user to press enter to continue. This can be useful to allow the user to read the message at their own pace before continuing, but it can lead to situations where the user doesn't notice the message while driving, and Parallax remains paused.
        - `delay` indicates how long, in seconds, Parallax should allow the message to be read before continuing. This delay is only used when `wait_for_input` is disabled.


## Audio Configuration

This section of configuration values effect Parallax's audio functionality.

- `sounds`
    This configuration value determines all of the sounds that Parallax is capable of using.
    - Each sound has a `path`, `repeat`, and `delay` defined.
        - The `path` defines the file path of the sound file.
            - This file path can be relative to the Parallax directory, or an absolute path.
        - The `repeat` setting defines how many times the sound file is played each time the sound is triggered.
            - When `repeat` is set to zero for a particular sound, that sould will be disabled.
        - The `delay` setting defines how long code execution will be paused to allow the sound effect time to play.
            - It's important to note that this delay does not include the time spent playing the audio file. Therefore, a 0.5 second audio file with a 1 second delay will only leave 0.5 seconds of delay after the sound has finished playing.
