"""
    Window Style Sheet
"""
# from icons_images_path import ImgAndIconsPath
from modules.gui.icons_images_path_loader import ImgAndIconsPath

class StyleSheets:
    """
        DataClass that hold all style variables
    """
    main_window : str = """background-color: #000000;"""
    side_bar : str = """background-color: #000000;"""
    side_bar_button = """
    QPushButton {
            background-color: #000000;
            color: white;
            border: none;
            border-top-left-radius: 15px;
            border-bottom-left-radius: 15px;
            padding: 10px;
            text-align: left;
            width: 500px;
            height: 20px;
        }
        QPushButton:hover {
            background-color: #0C3E7B;
        }
        QPushButton:checked {
                background-color: #002D5D;
            }
        """
    content : str = """background-color: #FFFFFF;"""
    header_footnote : str = """background-color: #000000;
    font: 700 7pt 'Segoe UI';
    color: #FFFFFF;"""
    page_holder : str = """background-color: #C5C5C5;"""
    title_bar : str = """background-color: #000000;"""
    title_bar_button : str = """
    QPushButton {
            background-color: #000000;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            max-width: 10px;
            max-height: 30px;
        }
        QPushButton:hover {
            background-color: #0C3E7B;
            }
        """
    resize_button = f"""
        QSizeGrip {{
        image: url({ImgAndIconsPath.resize_button});
        width: 15px;
        height: 15px;
    }}
            """
    # QFrame {
    #     border: 1px solid #3e3e3e;
    # }
    pages : str = """
    
    QWidget {
        background-color: #1e1e1e;
        color: #d4d4d4;
    }

    QMenuBar {
        background-color: #2d2d2d;
        color: #d4d4d4;
    }

    QMenuBar::item {
        background-color: #2d2d2d;
        color: #d4d4d4;
    }

    QMenuBar::item::selected {
        background-color: #3e3e3e;
    }

    QMenu {
        background-color: #2d2d2d;
        color: #d4d4d4;
    }

    QMenu::item::selected {
        background-color: #3e3e3e;
    }

    QToolBar {
        background-color: #2d2d2d;
        border: 1px solid #3e3e3e;
    }

    QToolButton {
        background-color: #2d2d2d;
        color: #d4d4d4;
    }

    QToolButton::hover {
        background-color: #3e3e3e;
    }

    QPushButton {
        background-color: #3e3e3e;
        color: #d4d4d4;
        border: 1px solid #3e3e3e;
        padding: 5px;
        border-radius: 8px;
    }

    QPushButton::hover {
        background-color: #0C3E7B;
    }

    QPushButton::pressed {
        background-color: #3e3e3e;
        border: 1px solid #0C3E7B;
    }

    QLineEdit, QTextEdit, QPlainTextEdit {
        background-color: #252526;
        color: #d4d4d4;
        border: 1px solid #3e3e3e;
        border-radius: 4px;
        
    }
    QTableWidget {
        background-color: #252526;
        color: #d4d4d4;
        border: 1px solid #3e3e3e;
        padding: 2px;
        border-radius: 6px;
    }

    QComboBox {
        background-color: #2d2d2d;
        color: #d4d4d4;
        border: 1px solid #3e3e3e;
    }

    QComboBox QAbstractItemView {
        background-color: #2d2d2d;
        color: #d4d4d4;
        selection-background-color: #3e3e3e;
    }

    QHeaderView::section {
        background-color: #2d2d2d;
        color: #d4d4d4;
        border: 1px solid #3e3e3e;
        padding: 5px;
    }

    QTableView {
        background-color: #1e1e1e;
        color: #d4d4d4;
        border: 1px solid #3e3e3e;
        gridline-color: #3e3e3e;
    }

    QTreeView {
        background-color: #1e1e1e;
        color: #d4d4d4;
        border: 1px solid #3e3e3e;
        gridline-color: #3e3e3e;
    }

    QListView {
        background-color: #1e1e1e;
        color: #d4d4d4;
        border: 1px solid #3e3e3e;
    }

    QScrollBar:horizontal {
        border: 1px solid #2d2d2d;
        background: #2d2d2d;
        height: 15px;
        margin: 0px 20px 0 20px;
    }

    QScrollBar::handle:horizontal {
        background: #3e3e3e;
        min-width: 20px;
    }

    QScrollBar::add-line:horizontal {
        border: 1px solid #3e3e3e;
        background: #2d2d2d;
        width: 20px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }

    QScrollBar::sub-line:horizontal {
        border: 1px solid #3e3e3e;
        background: #2d2d2d;
        width: 20px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }

    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
        border: 1px solid #3e3e3e;
        width: 3px;
        height: 3px;
        background: white;
    }

    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
        background: none;
    }

    QScrollBar:vertical {
        border: 1px solid #2d2d2d;
        background: #2d2d2d;
        width: 15px;
        margin: 20px 0 20px 0;
    }

    QScrollBar::handle:vertical {
        background: #3e3e3e;
        min-height: 20px;
    }

    QScrollBar::add-line:vertical {
        border: 1px solid #3e3e3e;
        background: #2d2d2d;
        height: 20px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }

    QScrollBar::sub-line:vertical {
        border: 1px solid #3e3e3e;
        background: #2d2d2d;
        height: 20px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        border: 1px solid #3e3e3e;
        width: 3px;
        height: 3px;
        background: white;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }

    QStatusBar {
        background-color: #2d2d2d;
        color: #d4d4d4;
        border-top: 1px solid #3e3e3e;
    }

    QTabWidget::pane {
        border: 1px solid #3e3e3e;
    }

    QTabBar::tab {
        background-color: #2d2d2d;
        color: #d4d4d4;
        border: 1px solid #3e3e3e;
        padding: 5px;
    }

    QTabBar::tab:selected {
        background-color: #3e3e3e;
    }

    QTabBar::tab:hover {
        background-color: #505050;
    }

    QGroupBox {
        border: 1px solid #3e3e3e;
        margin-top: 10px;
    }

    QGroupBox::title {
        color: #d4d4d4;
        subcontrol-origin: margin;
        subcontrol-position: top left;
        padding: 0 3px;
    }

    QToolTip {
        background-color: #2d2d2d;
        color: #d4d4d4;
        border: 1px solid #3e3e3e;
        padding: 5px;
    }
    QLabel {
            color: #FFFFFF;
            font-weight: bold;
    }
    """

    show_error : str = """
        QMessageBox {
            background-color: #000000;
            font-size: 14px;
        }
        QMessageBox QLabel {
            color: #FFFFFF;
            margin: 10px 10px 10px 20px;  
        }
        QPushButton {
        background-color: #3e3e3e;
        color: #d4d4d4;
        border: 1px solid #3e3e3e;
        min-width: 35px;
        padding: 5px;
        border-radius: 8px;
        }

        QPushButton::hover {
            background-color: #0C3E7B;
        }

        QPushButton::pressed {
            background-color: #3e3e3e;
            border: 1px solid #0C3E7B;
        }
    """
    privacy_policies_popup : str = """
        QMessageBox {
            background-color: #000000;
            font-size: 14px;
        }
        QMessageBox QLabel {
            color: #FFFFFF;
            margin: 10px 10px 10px 20px;  
        }
    """

    ppp_accept_btn : str = """
            QMessageBox QPushButton {
            background-color: #0E8231;
            color: white;
            padding: 5px 10px;
            border: none;
            border-radius: 5px;
            }
            QMessageBox QPushButton:hover {
                background-color: #0a5c23;
            }"""
    ppp_denied_btn : str = """
            QMessageBox QPushButton {
            background-color: #c70202;
            color: white;
            padding: 5px 10px;
            border: none;
            border-radius: 5px;
            }
            QMessageBox QPushButton:hover {
                background-color: #9e0000;
            }"""
