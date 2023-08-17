import dearpygui.dearpygui as dpg
import globalVars as gVars

def get_ClientsTable():
    with dpg.window(label="Список клиентов", width=gVars.window_width/1.5, height=gVars.window_height, no_collapse=True):
        with dpg.menu_bar():
             dpg.add_menu_item(label="Добавить строку", callback=addrowtotable)
        with dpg.table(header_row=True, tag="test"):
            dpg.add_table_column(label="Дата", tag="date")
            dpg.add_table_column(label="Номер ПК", tag="pc")
            dpg.add_table_column(label="Оплата", tag="price")
            dpg.add_table_column(label="Админ", tag="admin")

def addrowtotable():
    for i in range(0, 4):
                with dpg.table_row(tag="test_row"):
                    for j in range(0, 4):
                        dpg.add_text(f"Row{i} Column{j}")