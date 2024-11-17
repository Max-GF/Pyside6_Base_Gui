"""
    Help Pop-Up module
"""
import os
from dotenv import load_dotenv
from PySide6.QtWidgets import QMessageBox, QPushButton
from modules.gui.style_sheet import StyleSheets

load_dotenv()
APP_NAME = os.getenv("APP_NAME")

class HelpPopUp:
    """
        Help Pop-Up class with necessary functions
        
    """

    def show_message(self) -> bool:
        """
            Build Help Pop-Up window and show it
            
            Returns:
                QMessageBox.AcceptRole (bool): User choice
        """

        message_box = QMessageBox()
        message_box.setWindowTitle("Help")
        informative_text = f"""
							  <h1 style="display:block; margin-inline:auto; text-align:center; font-weight:bold; font-size:16px;">Bem-vindo!</h1>
							  <div style="text-align: left;">
							  	<p style="line-height: 1.2;">O app <b>"{APP_NAME}"</b> precisa dos seguinte requisitos para funcionar corretamente.</p>
							  	<p style="line-height: 1.2;"> Computador local:
							  		<br>
							  		<b>- ...;</b>
							  		<br>
							  		<b>- ...;</b>
							  		<br>
							  		<b>- ...;</b>
							  	</p>
							  	<p style="line-height: 1.2;"> Exemplo de configurações necessárias:
							  		<br>
							  		<b>- ...;</b>
							  		<br>
							  		<b>- ...;</b>
							  		<br>
							  		<b>- ...;</b>
							  	</p>
							  	<br>
							  	<details>
							  		<p style="line-height: 1.2;">
							  			Se tiver alguma dúvida, por favor, entre em contato com seu coordenador, ou clique no link abaixo.</p>
							  		<a href="https://drive.google.com/file/d/10rOMDplun6ZtTaj7L8Rsse8-HK6D1soz/view?usp=sharing">Tutorial</a>
							  	</details>
							  </div>
							  </div>
							  </div>
							  """
        message_box.setInformativeText(informative_text)
        message_box.setStyleSheet(StyleSheets.privacy_policies_popup)

        agree_button = QPushButton("  OK  ")
        agree_button.setStyleSheet(StyleSheets.ppp_accept_btn)
        message_box.addButton(agree_button, QMessageBox.AcceptRole)

        message_box.exec()
