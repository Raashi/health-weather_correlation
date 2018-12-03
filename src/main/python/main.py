from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import sys

import logic


class ExampleApp(QMainWindow, logic.Main):
    def __init__(self):
        # noinspection PyArgumentList
        super().__init__()
        # создание виджетов в MainForm (если что переопределить в logic.Main)
        self.setupUi(self)
        # старт (собстно show)
        logic.Main.start(self)


class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):                              # 2. Implement run()
        window = ExampleApp()
        window.setWindowTitle("Health-weather correlation")
        # window.resize(250, 150)
        window.show()
        return self.app.exec_()                 # 3. End run() with this line


if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)

# https://tproger.ru/translations/python-gui-pyqt/
# pyuic5 path/to/design.ui -o output/path/to/design.py
