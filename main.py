import dearpygui.dearpygui as dpg
import globalVars as gVars
import clientsTable as cTable

def main():
    dpg.create_context()
    dpg.create_viewport(title="FAKEDOWNBOYS", width=gVars.window_width, height=gVars.window_height, resizable=False)
    dpg.setup_dearpygui()
    gVars.setFont()

    with dpg.window(label="Impact Interface", width=dpg.get_viewport_width(), height=dpg.get_viewport_height(), no_collapse=True, no_close=True, no_resize=True, no_move=True, no_bring_to_front_on_focus=True):
        with dpg.menu_bar():
            with dpg.menu(label="Главная"):
                dpg.add_menu_item(label="Клиенты", callback=cTable.get_ClientsTable)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()