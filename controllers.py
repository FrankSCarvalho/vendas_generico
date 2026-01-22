# controllers.py
from models import Produto

class EstoqueController:
    def __init__(self, view):
        self.view = view
        # Conecta o clique do botão a uma função
        self.view.btn_atualizar.clicked.connect(self.carregar_dados)

    def carregar_dados(self):
        produtos = Produto.select()
        self.view.table.setRowCount(0)
        
        for p in produtos:
            row = self.view.table.rowCount()
            self.view.table.insertRow(row)
            self.view.table.setItem(row, 0, QTableWidgetItem(p.nome))
            self.view.table.setItem(row, 1, QTableWidgetItem(f"R$ {p.preco:.2f}"))
            self.view.table.setItem(row, 2, QTableWidgetItem(str(p.estoque)))