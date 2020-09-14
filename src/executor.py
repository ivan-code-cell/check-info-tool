from check_info import CheckInfo
from gui_application import Application, Menu
check_info = CheckInfo()
app = Application(check_info)
app.add_menu(Menu)
app.mainloop()