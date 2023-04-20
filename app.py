import sys
from PyQt5.QtWidgets import QApplication
from View.ventana_login import Main_login


app = QApplication(sys.argv)
window = Main_login()
window.show()


sys.exit(app.exec_())
