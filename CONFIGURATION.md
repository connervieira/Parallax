# Configuration

This document describes the configuration values found `config.json`.


## General Configuration

This section of configuration values will effect Parallax's general operation.

- `active_config_refresh`
    - This setting determines whether or not Parallax will refresh the configuration file every cycle.
    - Activating this setting can easily cause fatal errors, so it should only be used for testing.
- `gps_demo_mode`
    - This setting is used to supply Parallax with fake GPS data for sake of demonstration purposes.
    - To use this feature, simply set `enabled` to `true`, then set each GPS variable to any value you want. Parallax will use this fake information whenever it would otherwise poll the GPS for information.
- `refresh_delay`
    - This setting determines how long Parallax will wait between refreshes in seconds. Generally, 1 second is appropriate, but you can increase or decrease the delay to improve precision, or save processing power.


## Display Configuration

This section of configuration values effect Parallax's visual displays.

- `displays`
    - This configuration value allows the user to turn on and off each information display individually.
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
- `large_critical_display`
    - This setting allows the user to determine whether or not they want critical messages to be shown in large ASCII font.
    - This can be useful to allow the user to quickly see critically important information at a glance, such as an imminent threat that requires immediate action.
- `shape_alerts`
    - This setting allows the user to turn on and off Parallax's "shape alerts", which are large ASCII shapes displayed when important events occur.
    - Shape alerts take up a lot of space on screen, but make it easy for the driver to understand a situation simply using their peripheral vision.
- `ascii_art_header`
    - This configuration value determines whether or not Parallax will display a large title header upon start-up.
    - This this setting is set to `false`, Parallax will instead display a small, since line title.
- `custom_startup_message`
    - This setting defines a string that will be displayed the Parallax title upon start-up.
- `notices`
    - This configuration value contains all of the different levels of notices Parallax can show the user when issues are encountered. Level 1 indicates basic notices, level 2 indicates warnings, and level 3 indicates errors.
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
