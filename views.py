# views.py
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QPushButton, QTableWidget, QTableWidgetItem, QHeaderView)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Controle de Estoque e Vendas")
        self.resize(600, 400)

        # Layout Principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Tabela
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Produto", "Preço", "Estoque"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Botões
        self.btn_atualizar = QPushButton("Atualizar Estoque")
        self.layout.addWidget(self.btn_atualizar)