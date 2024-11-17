"""TODO
"""
import sys
import os
from dotenv import load_dotenv

from PySide6.QtWidgets import (QApplication, QFileDialog, QLineEdit,
                               QTableWidgetItem, QMessageBox)
from PySide6.QtGui import QIcon
from PySide6.QtCore import QThread, QObject, Signal
import pandas as pd

from modules.gui.main_window import UiMainWindow
from modules.gui.style_sheet import StyleSheets
from modules.gui.privacy_policies import PrivacyPolicies
basedir = os.path.dirname(__file__)
load_dotenv()

TASKBAR_ICON = os.getenv("TASKBAR_ICON_PATH")

try:
    from ctypes import windll  # Only exists on Windows.
    MYAPPID = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(MYAPPID)
except ImportError:
    pass

class BaseGuiApp:

    """
        Main class that compile all functions and ui contents
    """
    def __init__(self) -> None:
        """
            Class environment variables
        """
        self.app : QApplication = QApplication(sys.argv) # App base
        self.app.setWindowIcon(QIcon(TASKBAR_ICON)) # Set app icon
        self.window : UiMainWindow = UiMainWindow()
        self.thread : QThread = ...
        self.worker : ThreadWorker = ...

    def __get_file_path(self, line_edit_update : QLineEdit) -> None:
        """
            Read a (xlsx or xls) file 
            provided in file field on page 2,
            then send infos to table field.

        Args:
            line_edit_update (QLineEdit): File path field hook
        """
        file_path = QFileDialog.getOpenFileName(caption="Selecione um arquivo", filter="Excel Files (*.xlsx *.xls)")
        aux_df : pd.DataFrame = pd.read_excel(file_path[0],engine='openpyxl')
        if not aux_df.empty:
            self.window.pages.page_2_table.setRowCount(aux_df.shape[0])
            self.window.pages.page_2_table.setColumnCount(aux_df.shape[1])
            self.window.pages.page_2_table.setHorizontalHeaderLabels(aux_df.columns)

            for row_idx, row in aux_df.iterrows():
                for col_num, value in enumerate(row):
                    self.window.pages.page_2_table.setItem(row_idx, col_num, QTableWidgetItem(str(value)))
        line_edit_update.setText(file_path[0])

    def __login_and_password(self) -> tuple:
        """
            Check login and password fields on page 1

        Returns:
            tuple: Literal(login,password) or (None,None)
        """
        login : str = self.window.pages.login_qline.text()
        if not login or login == "":
            self.__show_alert(text="O campo de \"Login\" precisa ser preenchido")
            return (None, None)
        password : str = self.window.pages.password_qline.text()
        if not password or password == "":
            self.__show_alert(text="O campo de \"Senha\" precisa ser preenchido")
            return (None, None)
        return (login,password)

    def __login_and_password_page_2(self) -> tuple:
        """
            Check login and password fields on page 2

        Returns:
            tuple: Literal(login,password) or (None,None)
        """
        login : str = self.window.pages.login_qline_page_2.text()
        if not login or login == "":
            self.__show_alert(text="O campo de \"Login\" precisa ser preenchido")
            return (None, None)
        password : str = self.window.pages.password_qline_page_2.text()
        if not password or password == "":
            self.__show_alert(text="O campo de \"Senha\" precisa ser preenchido")
            return (None, None)
        return (login,password)

    def __run_example_function(self) -> None:
        """
            Trigger to execute a example
            function on Worker QThread
        """
        self.thread : QThread = QThread()
        self.worker : ThreadWorker = ThreadWorker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(lambda : self.worker.do_function(print,
                                    "Botão 5 foi apertado, mas executou em outro Thread"))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def __content_buttons_conections(self) -> None:
        """
            Set buttons connections
        """
        self.window.pages.page_1_btn_1.clicked.connect(lambda : print('Botão 1 foi apertado'))
        self.window.pages.page_1_btn_2.clicked.connect(lambda : print('Botão 2 foi apertado'))
        self.window.pages.page_1_btn_3.clicked.connect(lambda : print('Botão 3 foi apertado'))
        self.window.pages.page_1_btn_4.clicked.connect(lambda : print('Botão 4 foi apertado'))
        self.window.pages.page_2_btn_1.clicked.connect(self.__run_example_function)
        self.window.pages.page_2_btn_2.clicked.connect(lambda : print('Botão 6 foi apertado'))
        self.window.pages.choose_page_2_file.clicked.connect(lambda : self.__get_file_path(self.window.pages.page_2_file_path_qline))

    def __show_alert(self, text : str) -> None:
        """
            Alert trigger

        Args:
            text (str): Alert text
        """
        msg_box = QMessageBox()
        msg_box.setStyleSheet(StyleSheets.show_error)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Alerta")
        msg_box.setText(text)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def run_ui(self) -> None:
        """
            Run ui window
        """
        self.__content_buttons_conections()
        print('\r\033[34m\tPrivacy Policies\033[0m', end= '', flush=True)
        if PrivacyPolicies().show_message():
            self.window.show()
            sys.exit(self.app.exec())

class ThreadWorker(QObject):
    """
        Class that represents the thread
        executing functions in parallel to the GUI
    """
    finished : Signal = Signal()
    def do_function(self, function, *args, **kwargs) -> None:
        """
            Just one function executor on a different QThread

        Args:
            function (any): Function to be executed, and its args
        """
        function(*args, **kwargs)
        self.finished.emit()

if __name__ == "__main__":
    print('\033[7m\033[1mSTARTING THE APP (ง •_•)ง\033[0m\033[0m')
    main_app = BaseGuiApp()
    main_app.run_ui()
