import sys
from PySide6.QtWidgets import QApplication
from views import MainWindow
from controllers import EstoqueController

def main():
    app = QApplication(sys.argv)
    
    # Instancia a View
    window = MainWindow()
    
    # Instancia o Controller passando a View
    controller = EstoqueController(window)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()