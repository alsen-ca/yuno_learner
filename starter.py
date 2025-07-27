import pygame
import os
import dearpygui.dearpygui as dpg
from helpers import get_screen_size

pygame.mixer.init()

class Starter:
    def __init__(self):
        self.trainer = LetterTrainer()
        self.ui = LettersUI(self.trainer)



class LetterTrainer:
    def __init__(self):
        self.letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.index = 0

    def current_letter(self):
        return self.letters[self.index]

    def next_letter(self):
        self.index = (self.index + 1) % len(self.letters)

    def previous_letter(self):
        self.index = (self.index - 1) % len(self.letters)

    def play_sound(self):
        letter = self.current_letter()
        file_path = os.path.join("./assets/audios", f"{letter}.ogg")
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        else:
            print(f"Missing audio: {file_path}")


class LettersUI:
    def __init__(self, trainer):
        self.trainer = trainer
        self.letter_text_id = None

    def update_letter_display(self):
        current = self.trainer.current_letter()
        if self.letter_text_id:
            dpg.configure_item(self.letter_text_id, label=current)

    def start_app(self, font):
        dpg.delete_item("start_window")
        self.create_main_ui(font)

    def create_main_ui(self, font):
        screen_width, screen_height = get_screen_size()

        with dpg.window(tag="main_ui", width=screen_width, height=screen_height, pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True,
            no_scrollbar=True, no_collapse=True):
            dpg.add_spacer(height=screen_height * 0.04)
            
            with dpg.group(horizontal=True):
                btn_prev = dpg.add_button(label="<", callback=self.previous_letter, width=screen_width * 0.15, height=screen_height * 0.9)
                dpg.bind_item_font(btn_prev, font)
                dpg.add_spacer(width=screen_width * 0.02)
                

                self.letter_text_id = dpg.add_button(label=self.trainer.current_letter(), callback=self.play_sound,
                                                    width=screen_width * 0.66, height=screen_height * 0.9)
                dpg.bind_item_font(self.letter_text_id, font)

                dpg.add_spacer(width=screen_width * 0.02)
                btn_next = dpg.add_button(label=">", callback=self.next_letter, width=screen_width * 0.15, height=screen_height * 0.9)
                dpg.bind_item_font(btn_next, font)
            




    def play_sound(self, sender, app_data=None, user_data=None):
        self.trainer.play_sound()

    def next_letter(self):
        self.trainer.next_letter()
        self.update_letter_display()

    def previous_letter(self):
        self.trainer.previous_letter()
        self.update_letter_display()