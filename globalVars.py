import dearpygui.dearpygui as dpg

#. Размеры окна
def windowSize():
    width = 800
    height = width
    return width, height

window_width, window_height = windowSize()

#. Шрифт
def setFont():
    with dpg.font_registry():
        with dpg.font(f'fonts/YsabeauSC-Regular.ttf', 18, tag="Default font"):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    dpg.bind_font("Default font")
    return 0