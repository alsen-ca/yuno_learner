## Yuno Learner
Simple application that outputs an audio file when a letter is clicked.

Goal of the app is to learn how each letter of the Alphabet sounds.

## Requirements
The system needs follwoing dependencies in order to work.

    python3
    pip
    pygame
    dearpygui

The instructions differ sepending on Operating system, but for Windows, this overall, simple guide, should suffice:

    1. Install python: https://www.python.org/downloads/windows/
    2. Confirm that python and pip are installed in the cmd
        python3 -v
        pip -v
    3. Install pygame
        pip install pygame
    4. Install dearpygui
        pip install dearpygui


## Installation
I would recommend cloning the repository.
If using Windows, then using [Git Bash](https://git-scm.com/downloads) is a good option.

1. Open Git Bash and go to the path were the app should be installed.
For example

    cd Documents/

2. Clone the repository

    git clone https://github.com/alsen-ca/yuno_learner.git


## Usage
### Add audio files
To use this Application, one should add the 26 inidividual audio files for each letter of the Alphabet under the location assets/audios.
If the audios folder does not exist, then it should be created.
For each letter of the alphabet, an individual file must be added.

Files must have the extension .ogg
File names must be named with the uppercase letter of the character, followed by the extension. Examples:

    - A.ogg
    - B.ogg
    - P.ogg
    - X.ogg


This Application does NOT come with the required audio files.
User must add them themselves.

### Starting the application
Assuming, during the 'Installation' steps, one cloned the Repository in the 'Documents/' path, then a folder '/Documents/yuno_learner' should have been created.

1. We open the same Git Bash terminal as before

2. We go to the 'yuno_learner' folder

    cd yuno_learner

3. We start the application
For Windows:

    python main.py

For Linux:

    python3 main.py

## Compatibility issues
Please note that this app has not been extensively tested.
The original version was written in Linux, so it should work semi-reliably there, at least for Fedora.

On Windows, there is an issue regarding the size of the fonts, which causes the App to crash without errors.
To fix it, change the value of font_big = dpg.add_font("assets/fonts/LiberationSans-Bold.ttf", 500)

to:

    font_big = dpg.add_font("assets/fonts/LiberationSans-Bold.ttf", 400)

That should be enough, but I am not sure whence the error comes from, maybe it isnt even a problem on the OS level, but rather the size of the screen.
If that should not have solved it, then one can decrease the size further and try it again.

It has not been tested for MacOS at all, but there are some potential issues, for example regarding the fetching of the screen size

## Fonts

This app uses the [Liberation Sans](https://github.com/liberationfonts/liberation-fonts) typeface, which is licensed under the [SIL Open Font License, Version 1.1](https://scripts.sil.org/OFL).

The font files and license are included in `assets/fonts/` for convenience.

