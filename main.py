# main.py
import sys
from PySide6.QtWidgets import QApplication
from views import MainWindow
from controllers import EstoqueController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    view = MainWindow()
    controller = EstoqueController(view)
    
    view.show()
    sys.exit(app.exec())