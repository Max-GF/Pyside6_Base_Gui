"""
    Internal pages pyside6 module
"""
from PySide6.QtCore import (QMetaObject, QSize, Qt)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget, QStackedWidget,
                               QGridLayout, QTextBrowser,QTableWidget)
from modules.gui.icons_images_path_loader import ImgAndIconsPath
from modules.gui.style_sheet import StyleSheets


class UiPagesWidget():
    """
        Content pages class

    Args:
        object (QStackedWidget): Page Holder variable
    """
    def __init__(self) -> None:
        """TODO
        """
        # Pages:
        self.home : QWidget = ...
        self.page_1 : QWidget = ...
        self.page_2 : QWidget = ...

        # Buttons:
        self.page_1_btn_1 : QPushButton = QPushButton("BOTÃO 1", cursor=Qt.PointingHandCursor)
        self.page_1_btn_3 : QPushButton = QPushButton("BOTÃO 2", cursor=Qt.PointingHandCursor)

        self.page_1_btn_2 : QPushButton = QPushButton("BOTÃO 3", cursor=Qt.PointingHandCursor)
        self.page_1_btn_4 : QPushButton = QPushButton("BOTÃO 4", cursor=Qt.PointingHandCursor)

        self.page_2_btn_1 : QPushButton = QPushButton("BOTÃO 5", cursor=Qt.PointingHandCursor)
        self.page_2_btn_2 : QPushButton = QPushButton("BOTÃO 6", cursor=Qt.PointingHandCursor)
        self.choose_page_2_file : QPushButton = QPushButton(icon=QPixmap(ImgAndIconsPath.folder_btn_icon),
                                                          cursor=Qt.PointingHandCursor)

        # Entries:
        self.login_qline : QLineEdit = QLineEdit()
        self.password_qline : QLineEdit = QLineEdit()

        self.login_qline_page_2 : QLineEdit = QLineEdit()
        self.password_qline_page_2 : QLineEdit = QLineEdit()
        self.page_2_file_path_qline : QLineEdit = QLineEdit()

        # Displays:
        self.terminal_at_app : QTextBrowser = QTextBrowser()
        self.page_2_terminal : QTextBrowser = QTextBrowser()
        self.page_2_table : QTableWidget = QTableWidget()

    def setup_ui(self, pages_widget: QStackedWidget):
        """
            Setup content pages to be used in main function

        Args:
            PagesWidget (QStackedWidget): Page holder
        """
        if not pages_widget.objectName():
            pages_widget.setObjectName("PagesWidget")
        pages_widget.resize(727, 407)
        self.home = self.__home_page()
        pages_widget.addWidget(self.home)
        self.page_1 = self.__page_1_example()
        pages_widget.addWidget(self.page_1)
        self.page_2 = self.__page_2_example()
        pages_widget.addWidget(self.page_2)
        pages_widget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(pages_widget)

    def __home_page(self) -> QWidget:
        """
                              HOME PAGE
        ◸——————————————————————————————————————————————————◹
        |                        ↑                          |
        |                    TOP SPACER                     |
        |                        ↓                          |
        |                    ◸———————◹                     |
        |  ← LEFT SPACER →   |  LOGO  |   ← RIGHT SPACER →  |
        |                    ◺———————◿                     |
        |                        ↑                          |
        |                    BOT SPACER                     |
        |                        ↓                          |
        ◺——————————————————————————————————————————————————◿

        Returns:
            QWidget: Page Widget
        """

        home = QWidget()
        home_layout_v = QVBoxLayout(home)

        home_frame = QFrame(home)
        home_frame.setFrameShape(QFrame.StyledPanel)
        home_frame.setFrameShadow(QFrame.Raised)
        home_frame_layout = QVBoxLayout(home_frame)

        top_logo_spacer = QSpacerItem(20, 1000, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        home_frame_layout.addItem(top_logo_spacer)

        logo_holder = QWidget(home_frame)
        logo_holder_layout = QHBoxLayout(logo_holder)
        lef_logo_spacer = QSpacerItem(1000, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        logo_holder_layout.addItem(lef_logo_spacer)

        logo = QLabel(logo_holder)
        logo.setEnabled(True)
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(logo.sizePolicy().hasHeightForWidth())
        logo.setSizePolicy(size_policy)
        logo.setMinimumSize(QSize(1, 1))
        logo.setTextFormat(Qt.AutoText)
        logo.setPixmap(QPixmap(ImgAndIconsPath.home_image))
        logo.setScaledContents(True)
        logo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        logo_holder_layout.addWidget(logo, 0, Qt.AlignRight|Qt.AlignVCenter)

        rig_logo_spacer = QSpacerItem(1000, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        logo_holder_layout.addItem(rig_logo_spacer)

        home_frame_layout.addWidget(logo_holder, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        bot_logo_spacer = QSpacerItem(20, 1000, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        home_frame_layout.addItem(bot_logo_spacer)

        home_layout_v.addWidget(home_frame)

        return home

    def __page_1_example(self) -> QWidget:
        """
                            PAGE 1
        ◸———————————————————————————————————————————————◹
        |   ◸——◹ ◸——◹ ◸——◹ ◸——◹ ◸——◹ ◸——◹ ◸——◹    |
        |   ◺——◿ ◺——◿ ◺——◿ ◺——◿ ◺——◿ ◺——◿ ◺——◿    |
        |------------------------------------------------|
        |Login []               ◸———————————————◹       |
        |Senha []               |  Report infos  |       |
        |                       ◺———————————————◿       |
        ◺———————————————————————————————————————————————◿

        Returns:
            QWidget: Page Widget
        """
        # Criando a página
        page_1_example : QWidget = QWidget()
        page_1_example.setStyleSheet(StyleSheets.pages)
        page_1_example_layout : QVBoxLayout = QVBoxLayout(page_1_example) # Definindo o layout da página
        page_1_example_frame : QFrame = QFrame(page_1_example) # Definindo o frame onde as coisas da página serão alocadas
        page_1_example_frame.setFrameShape(QFrame.StyledPanel)
        page_1_example_frame.setFrameShadow(QFrame.Raised)
        page_1_example_frame_layout : QVBoxLayout = QVBoxLayout(page_1_example_frame)

        # Definindo a parte superior da página, onde ficará a grade de botões das funções
        top_funcs_frame : QFrame = QFrame(page_1_example_frame)
        top_funcs_frame_layout : QGridLayout = QGridLayout(top_funcs_frame)


        # Distribuindo os botões na parte superior da página (botão, linha, coluna)
        top_funcs_frame_layout.addWidget(self.page_1_btn_1, 0, 1)
        top_funcs_frame_layout.addWidget(self.page_1_btn_2, 0, 2)
        top_funcs_frame_layout.addWidget(self.page_1_btn_3, 1, 1)
        top_funcs_frame_layout.addWidget(self.page_1_btn_4, 1, 2)

        # Definindo a parte inferior da página, onde ficarão as entradas necessárias (login e senha), assim como os textos de saídas
        bot_entries_frame : QFrame = QFrame(page_1_example_frame)
        bot_entries_frame_layout : QHBoxLayout = QHBoxLayout(bot_entries_frame)

        # Criando o local das entradas de login e senha
        user_and_password_frame : QFrame = QFrame(page_1_example_frame)
        user_and_password_frame_layout = QVBoxLayout(user_and_password_frame)
        user_and_password_frame_layout.setAlignment(Qt.AlignTop)
        user_and_password_frame_layout.addWidget(QLabel("Login"))
        self.login_qline.setPlaceholderText("Usuário...")
        self.login_qline.setMaximumWidth(200)
        user_and_password_frame_layout.addWidget(self.login_qline)

        user_and_password_frame_layout.addWidget(QLabel("Senha"))
        self.password_qline.setPlaceholderText("Senha...")
        self.password_qline.setMaximumWidth(200)
        user_and_password_frame_layout.addWidget(self.password_qline)

        bot_entries_frame_layout.addWidget(user_and_password_frame)

        terminal_frame : QFrame = QFrame()
        terminal_frame_layout : QVBoxLayout = QVBoxLayout(terminal_frame)
        terminal_frame_layout.addWidget(QLabel("Logs"))
        terminal_frame_layout.addWidget(self.terminal_at_app)
        bot_entries_frame_layout.addWidget(terminal_frame)

        # Adicionando o a parte superior e inferior da página ao frame interno
        page_1_example_frame_layout.addWidget(top_funcs_frame)
        page_1_example_frame_layout.addWidget(bot_entries_frame)

        # Adicionando o frame interno ao layout da página
        page_1_example_layout.addWidget(page_1_example_frame)

        return page_1_example

    def __page_2_example(self) -> QWidget:
        """
                            PAGE 2
        ◸———————————————————————————————————————————————◹
        |   ◸——◹ ◸——◹ ◸——◹ ◸——◹ ◸——◹ ◸——◹ ◸——◹    |
        |   ◺——◿ ◺——◿ ◺——◿ ◺——◿ ◺——◿ ◺——◿ ◺——◿    |
        |------------------------------------------------|
        |Login []               ◸———————————————◹       |
        |Senha []               |  Report infos  |       |
        |                       ◺———————————————◿       |
        ◺———————————————————————————————————————————————◿

        Returns:
            QWidget: Page Widget
        """

        # Criando a base da página e seu layout
        page_2_example : QWidget = QWidget()
        page_2_example.setStyleSheet(StyleSheets.pages)
        page_2_example_layout : QHBoxLayout = QHBoxLayout(page_2_example)

        # Montando o frame do terminal
        page_2_terminal_frame : QFrame = QFrame()
        page_2_terminal_frame_layout : QVBoxLayout = QVBoxLayout(page_2_terminal_frame)
        page_2_terminal_frame_layout.addWidget(QLabel("Logs"))
        page_2_terminal_frame_layout.addWidget(self.page_2_terminal)

        # Montando o frame esquerdo
        page_2_lef_frame : QFrame = QFrame()
        page_2_lef_frame.setMaximumWidth(400)
        # page_2_lef_frame.setContentsMargins(0,0,0,0)
        page_2_lef_frame_layout : QVBoxLayout = QVBoxLayout(page_2_lef_frame)
        page_2_lef_frame_layout.setContentsMargins(0,0,0,0)


        # Criando um frame para adicionar os botões de movimentações
        page_2_btns_frame : QFrame = QFrame()
        page_2_btns_frame_layout : QHBoxLayout = QHBoxLayout(page_2_btns_frame)
        page_2_btns_frame_layout.addWidget(self.page_2_btn_1)
        page_2_btns_frame_layout.addWidget(self.page_2_btn_2)

        # Criando e adicionando o conjunto do login + senha ao frame superior
        up_lef_frame : QFrame = QFrame()
        up_lef_frame_layout : QVBoxLayout = QVBoxLayout(up_lef_frame)
        up_lef_frame_layout.setContentsMargins(0,0,0,0)

        login_password_frame : QFrame = QFrame()
        login_password_frame_layout : QHBoxLayout = QHBoxLayout(login_password_frame)

        login_frame : QFrame = QFrame()
        login_frame_layout : QVBoxLayout = QVBoxLayout(login_frame)
        login_frame_layout.setContentsMargins(0,0,0,0)
        login_frame_layout.setAlignment(Qt.AlignTop)

        login_frame_layout.addWidget(QLabel("Login"))
        self.login_qline_page_2.setPlaceholderText("Usuário...")
        self.login_qline_page_2.setMaximumWidth(200)
        self.login_qline_page_2.setMinimumHeight(25)
        login_frame_layout.addWidget(self.login_qline_page_2)

        password_frame : QFrame = QFrame()
        password_frame_layout : QVBoxLayout = QVBoxLayout(password_frame)
        password_frame_layout.setContentsMargins(0,0,0,0)
        password_frame_layout.setAlignment(Qt.AlignTop)

        self.password_qline_page_2.setPlaceholderText("Senha...")
        self.password_qline_page_2.setMaximumWidth(200)
        self.password_qline_page_2.setMinimumHeight(25)
        password_frame_layout.addWidget(QLabel("Senha"))
        password_frame_layout.addWidget(self.password_qline_page_2)

        login_password_frame_layout.addWidget(login_frame)
        login_password_frame_layout.addWidget(password_frame)

        up_lef_frame_layout.addWidget(login_password_frame)
        up_lef_frame_layout.addWidget(page_2_btns_frame)

        # Criando e adicionando as opções de entrada de arquivo
        rig_frame : QFrame = QFrame()
        rig_frame_layout : QVBoxLayout = QVBoxLayout(rig_frame)
        rig_frame_layout.addWidget(QLabel("Arquivo..."))

        btn_plus_qline_frame : QFrame = QFrame()
        btn_plus_qline_frame_layout : QHBoxLayout = QHBoxLayout(btn_plus_qline_frame)
        btn_plus_qline_frame_layout.setContentsMargins(0,0,0,0)
        self.page_2_file_path_qline.setPlaceholderText("Por favor, escolha um arquivo...")
        self.page_2_file_path_qline.setMinimumHeight(25)

        btn_plus_qline_frame_layout.addWidget(self.choose_page_2_file)
        btn_plus_qline_frame_layout.addWidget(self.page_2_file_path_qline)

        rig_frame_layout.addWidget(btn_plus_qline_frame)
        rig_frame_layout.addWidget(self.page_2_table)

        page_2_lef_frame_layout.addWidget(up_lef_frame)
        page_2_lef_frame_layout.addWidget(page_2_terminal_frame)
        page_2_example_layout.addWidget(page_2_lef_frame)
        page_2_example_layout.addWidget(rig_frame)

        return page_2_example
