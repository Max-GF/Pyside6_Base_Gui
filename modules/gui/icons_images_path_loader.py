"""
    Window images and icons paths
"""
import os
from dotenv import load_dotenv
load_dotenv()

class ImgAndIconsPath:
    """ 
        Class that hold all images and icons paths
    """
    # TOP BAR
    minimize_icon : str = os.getenv("MINIMIZE_ICON_PATH")
    maximize_icon : str = os.getenv("MAXIMIZE_ICON_PATH")
    close_icon : str = os.getenv("CLOSE_ICON_PATH")
    question_mark : str = os.getenv("HELP_ICON_PATH")
    logo_image : str = os.getenv("TITLE_ICON_PATH")

    # SIDE BAR
    expand_sidebar : str = os.getenv("EXPAND_SIDEBAR_ICON_PATH")
    home_btn : str = os.getenv("HOME_BUTTON_ICON_PATH")
    page_1_btn : str = os.getenv("PAGE_1_BUTTON_ICON_PATH")
    page_2_btn : str = os.getenv("PAGE_2_BUTTON_ICON_PATH")
    privacy : str = os.getenv("PRIVACY_POLICIES_ICON_PATH")

    # HOME
    home_image : str = os.getenv("HOME_LOGO_PATH")

    # PAGE's
    folder_btn_icon : str = os.getenv("FOLDER_BUTTON_ICON_PATH")

    # BOTTON BAR
    resize_button : str = os.getenv("RESIZE_BUTTON_ICON_PATH")
