"""
    Privacy policies start window module
"""
import os
from dotenv import load_dotenv
from PySide6.QtWidgets import QMessageBox, QPushButton
from PySide6.QtCore import Qt
from modules.gui.style_sheet import StyleSheets

load_dotenv()
APP_NAME = os.getenv("APP_NAME")
class PrivacyPolicies:
    """
        Privacy policies class with necessary functions
        
    """

    def show_message(self) -> bool:
        """
            Build Privacy policies window and show it
            
            Returns:
                QMessageBox.AcceptRole (bool): User choice
        """
        # QApplication([])

        message_box = QMessageBox()
        message_box.setWindowTitle("Políticas de privacidade")
        informative_text = f"""
							  <h1 style="display:block; margin-inline:auto; text-align:center; font-weight:bold; font-size:16px;">Bem-vindo!</h1>
							  <div style="text-align: left;">
							  	<p style="line-height: 1.2;">O app <b>"{APP_NAME}"</b> precisa ter acesso aos seus dados.</p>
							  	<p style="line-height: 1.2;"> Quando o acesso for permitido, o app poderá:
							  		<br>
							  		<b>- ...;</b>
							  		<br>
							  		<b>- ...;</b>
							  		<br>
							  		<b>- ...;</b>
							  	</p>
							  
							  	<p style="line-height: 1.2;">
							  		Além disso, é importante ressaltar que a escolha dos dados de entrada e saída é exclusivamente do usuário que
							  		está
							  		executando esta aplicação. Portanto, qualquer análise ou resultado obtido deve ser cuidadosamente revisado e
							  		validado pelo usuário responsável antes de tomar qualquer ação ou conclusão.
							  		Sendo assim, utilize esta ferramenta com cautela e sempre verifique a precisão e a adequação dos resultados por
							  		conta própria.
							  	</p>
							  	<br>
							  	<strong>Aviso de Isenção de Responsabilidade:</strong>
							  	<p style="line-height: 1.2;"> Esta aplicação e seus criadores não assumem qualquer responsabilidade pelos dados
							  		sendo analisados nem pelas decisões tomadas com base neles.</p>
							  	<details>
							  		<p style="line-height: 1.2;">Ao concordar com esta declaração, você poderá prosseguir e utilizar o app
							  			normalmente.
							  			Se tiver alguma dúvida ou preocupação sobre o processamento de suas informações, por favor, entre em contato
							  			com seu coordenador, ou clique no link abaixo.</p>
							  		<a href="https://drive.google.com/file/d/1ntLpeYqyjzt8sC4fuiI9_A2HQpJ77QZi/view">Saiba mais</a>
							  	</details>
							  </div>
							  <h4 style="font-weight:bold; text-align:left; justify-content:left;">Concorda com os termos? </h4>
							  </div>
							  </div>
							  """
        message_box.setInformativeText(informative_text)
        message_box.setStyleSheet(StyleSheets.privacy_policies_popup)

        agree_button = QPushButton("  Concordo  ",cursor=Qt.PointingHandCursor)
        agree_button.setStyleSheet(StyleSheets.ppp_accept_btn)
        disagree_button = QPushButton(" Não concordo ",cursor=Qt.PointingHandCursor)
        disagree_button.setStyleSheet(StyleSheets.ppp_denied_btn)
        message_box.addButton(agree_button, QMessageBox.AcceptRole)
        message_box.addButton(disagree_button, QMessageBox.RejectRole)
        message_box.exec()

        if message_box.clickedButton() == agree_button:
            print("\r\033[34m\tPrivacy Policies\033[0m -> \033[32mUser agreed.\033[0m")
            return True

        print("\r\033[34m\tPrivacy Policies\033[0m -> \033[31mUser did not agree.\033[0m")
        return False
