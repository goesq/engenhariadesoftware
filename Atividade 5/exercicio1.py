
# Diagrama de Sequência - Exercício 1 Atividade 5

class ECommerceSystem:
    def __init__(self):
        self.cart = []
        self.payment_valid = False
        self.stock_available = True

    def display_homepage(self):
        print("Sistema: Página inicial exibida com opções de produtos.")

    def add_to_cart(self, product):
        print(f"Sistema: Produto '{product}' adicionado ao carrinho.")
        self.cart.append(product)

    def request_payment(self):
        print("Sistema: Solicitação de dados de pagamento enviada.")

    def validate_payment(self, payment_info):
        print("Sistema: Validando pagamento...")
        self.payment_valid = payment_info.get("valid", False)
        return self.payment_valid

    def check_stock(self):
        print("Sistema: Verificando disponibilidade no estoque...")
        return self.stock_available

    def confirm_purchase(self):
        if not self.cart:
            print("Sistema: Carrinho vazio! Não há itens para confirmar.")
            return False
        print("Sistema: Compra confirmada e nota fiscal gerada.")
        return True

    def notify_customer(self):
        print("Sistema: Confirmação de compra enviada ao cliente.")


# Simulando o fluxo principal
def purchase_online():
    system = ECommerceSystem()
    system.display_homepage()

    # Cliente seleciona e adiciona produto
    system.add_to_cart("Notebook")

    # Cliente finaliza compra
    system.request_payment()

    # Cliente informa os dados de pagamento
    payment_info = {"valid": True}
    if system.validate_payment(payment_info):
        if system.check_stock():
            if system.confirm_purchase():
                system.notify_customer()
            else:
                print("Erro: Falha ao confirmar a compra.")
        else:
            print("Erro: Produto indisponível no estoque.")
    else:
        print("Erro: Pagamento recusado.")


# Executar fluxo de compra online
purchase_online()
