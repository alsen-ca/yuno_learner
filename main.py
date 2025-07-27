import starter
import dearpygui.dearpygui as dpg
from helpers import get_screen_size

screen_width, screen_height = get_screen_size()    



class MainMenu:
    def __init__(self):
        dpg.create_context()
        with dpg.font_registry():
            font_normal = dpg.add_font("assets/fonts/LiberationSans-Bold.ttf", 100)
            font_big = dpg.add_font("assets/fonts/LiberationSans-Bold.ttf", 500)
        
        self.starter = starter.Starter()

        with dpg.window(tag="start_window", label="Welcome", no_title_bar=True, no_move=True, no_resize=True):
            btn = dpg.add_button(label="Start", width=600, height=100, callback=lambda: self.starter.ui.start_app(font_big))
            dpg.bind_item_font(btn, font_normal)



def main():
    MainMenu()

    dpg.create_viewport(title="Alphabet Sounds", width=100, height=100)
    dpg.setup_dearpygui()
    dpg.show_viewport()

    dpg.set_viewport_width(screen_width)
    dpg.set_viewport_height(screen_height)
    dpg.set_viewport_pos((0, 0))

    dpg.configure_item("start_window", width=screen_width, height=screen_height)

    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
