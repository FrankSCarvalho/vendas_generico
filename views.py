from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QTableWidget, QTableWidgetItem, 
                             QHeaderView, QDialog, QFormLayout, QLineEdit, 
                             QDoubleSpinBox, QSpinBox, QDialogButtonBox, QComboBox)

class ProdutoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cadastrar Novo Produto")
        layout = QFormLayout(self)

        self.nome = QLineEdit()
        self.preco = QDoubleSpinBox(maximum=99999.99)
        self.estoque = QSpinBox(maximum=1000)

        layout.addRow("Nome do Produto:", self.nome)
        layout.addRow("Preço (R$):", self.preco)
        layout.addRow("Estoque Inicial:", self.estoque)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addRow(self.buttons)

    def get_data(self):
        return self.nome.text(), self.preco.value(), self.estoque.value()

class VendaDialog(QDialog):
    def __init__(self, produtos, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Realizar Venda")
        layout = QFormLayout(self)

        self.cb_produtos = QComboBox()
        for p in produtos:
            self.cb_produtos.addItem(p.nome, p)

        self.quantidade = QSpinBox(minimum=1, maximum=100)

        layout.addRow("Selecionar Produto:", self.cb_produtos)
        layout.addRow("Quantidade:", self.quantidade)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addRow(self.buttons)

    def get_data(self):
        return self.cb_produtos.currentData(), self.quantidade.value()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Vendas e Estoque")
        self.resize(800, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Tabela de Estoque
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Produto", "Preço", "Estoque"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Botões de Ação
        self.btn_layout = QHBoxLayout()
        self.btn_novo_produto = QPushButton("Novo Produto")
        self.btn_venda = QPushButton("Realizar Venda")
        self.btn_atualizar = QPushButton("Atualizar Tabela")
        
        self.btn_layout.addWidget(self.btn_novo_produto)
        self.btn_layout.addWidget(self.btn_venda)
        self.btn_layout.addWidget(self.btn_atualizar)
        
        self.layout.addLayout(self.btn_layout)