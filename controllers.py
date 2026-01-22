from models import db, Produto, Venda
from views import ProdutoDialog, VendaDialog
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

class EstoqueController:
    def __init__(self, view):
        self.view = view
        # Conectando os eventos dos botões
        self.view.btn_novo_produto.clicked.connect(self.abrir_cadastro_produto)
        self.view.btn_venda.clicked.connect(self.abrir_venda)
        self.view.btn_atualizar.clicked.connect(self.carregar_dados)
        
        # Carregar dados iniciais
        self.carregar_dados()

    def carregar_dados(self):
        produtos = Produto.select()
        self.view.table.setRowCount(0)
        
        for p in produtos:
            row = self.view.table.rowCount()
            self.view.table.insertRow(row)
            self.view.table.setItem(row, 0, QTableWidgetItem(p.nome))
            self.view.table.setItem(row, 1, QTableWidgetItem(f"R$ {p.preco:.2f}"))
            self.view.table.setItem(row, 2, QTableWidgetItem(str(p.estoque)))

    def abrir_cadastro_produto(self):
        dialog = ProdutoDialog(self.view)
        if dialog.exec():
            nome, preco, estoque = dialog.get_data()
            if nome:
                Produto.create(nome=nome, preco=preco, estoque=estoque)
                self.carregar_dados()
                QMessageBox.information(self.view, "Sucesso", "Produto cadastrado!")

    def abrir_venda(self):
        produtos = Produto.select()
        if not produtos.exists():
            QMessageBox.warning(self.view, "Erro", "Não há produtos cadastrados!")
            return

        dialog = VendaDialog(produtos, self.view)
        if dialog.exec():
            produto_selecionado, qtd = dialog.get_data()
            
            # Verificação de estoque
            if produto_selecionado.estoque >= qtd:
                with db.atomic():
                    # Registra a venda
                    Venda.create(produto=produto_selecionado, quantidade=qtd)
                    # Atualiza o estoque do objeto e salva no banco
                    produto_selecionado.estoque -= qtd
                    produto_selecionado.save()
                
                self.carregar_dados()
                QMessageBox.information(self.view, "Sucesso", "Venda realizada com sucesso!")
            else:
                QMessageBox.critical(self.view, "Erro", f"Estoque insuficiente! Disponível: {produto_selecionado.estoque}")