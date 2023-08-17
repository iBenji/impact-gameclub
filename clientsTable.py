import dearpygui.dearpygui as dpg
import globalVars as gVars

cTable_window = None

dpg.create_context()
def get_ClientsTable():
    # cTable_window check to fix "alias" issue!
    global cTable_window
    if cTable_window is not None:
        dpg.delete_item(cTable_window)
        cTable_window = None

    with dpg.window(label="Список клиентов", width=gVars.window_width/1.5, height=gVars.window_height-60, no_collapse=True, no_resize=True) as cTable_window:
        with dpg.menu_bar():
            dpg.add_menu_item(label="Добавить строку", callback=addrowtotable)
        with dpg.table(header_row=True, tag="cTable"):
            dpg.add_table_column(label="Дата", id="date", width_stretch=True)
            dpg.add_table_column(label="Номер ПК", id="pc", width_stretch=True)
            dpg.add_table_column(label="Оплата", id="price", width_stretch=True)
            dpg.add_table_column(label="Админ", id="admin", width_stretch=True)


def addrowtotable():
    for i in range(0, 1):
                with dpg.table_row(parent="cTable"):
                    for j in range(0, 4):
                        dpg.add_input_text(width=200)
dpg.destroy_context()