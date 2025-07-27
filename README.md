## Yuno Learner
Simple application that outputs an audio file when a letter is clicked.

Goal of the app is to learn how each letter of the Alphabet sounds.

## Requirements
The system needs follwoing dependencies in order to work.

    python3
    pip
    pygame
    dearpygui

## Usage
To use this Application, one should add the 26 inidividual audio files under assets/audios.
For each letter of the alphabet, an individual file must be added.

Files must have the extension .ogg.
File names must be the uppercase letter of the alphabet, followed by the extension. Examples:

    - A.ogg
    - B.ogg
    - P.ogg
    - X.ogg

These files must be added to a /assets/audios folder.

This Application does NOT come with the required audio files.

## Compatibily issues
Please note that this app has not been extensively tested.
The original version was written in Linux, so it should work semi-reliably here.

On Windows, there is an issue regarding the size of the fonts, which causes the App to crash without errors.

It has not been tested for MacOS at all, but there are some potential issues, for example regarding rhe fetch of the screen size

## Fonts

This app uses the [Liberation Sans](https://github.com/liberationfonts/liberation-fonts) typeface, which is licensed under the [SIL Open Font License, Version 1.1](https://scripts.sil.org/OFL).

The font files and license are included in `assets/fonts/` for convenience.

