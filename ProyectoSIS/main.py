from PySide2.QtWidgets import QApplication
#from qt_material import apply_stylesheet
from mainwindow import MainWindow
import sys
app = QApplication()
window = MainWindow()
#apply_stylesheet(app, theme='dark_teal.xml')
window.show()
sys.exit(app.exec_())


