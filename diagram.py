class Prato:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_info(self):
        print(f"Prato: {self.nome} | Preço: R$ {self.preco:.2f}")


class Pedido:
    def __init__(self, num_pedido):
        self.num_pedido = num_pedido
        self.pratos = []

    def add_prato(self, prato):
        self.pratos.append(prato)

    def rem_prato(self, prato):
        self.pratos.remove(prato)

    def calcular_total(self):
        return sum(prato.preco for prato in self.pratos)

    def mostrar_info(self):
        print(f"Pedido nº: {self.num_pedido}")
        for prato in self.pratos:
            prato.mostrar_info()
        print(f"Total: R$ {self.calcular_total():.2f}")


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

    def add_pedido(self, pedido):
        self.pedidos.append(pedido)

    def rem_pedido(self, pedido):
        self.pedidos.remove(pedido)

    def listar_pedidos(self):
        print(f"Pedidos do Cliente {self.nome}:")
        for pedido in self.pedidos:
            pedido.mostrar_info()
            print()


# Exemplo de uso
if __name__ == "__main__":
    cliente = Cliente("Maria")

    pedido1 = Pedido(1)
    pedido1.add_prato(Prato("Pizza Margherita", 29.90))
    pedido1.add_prato(Prato("Cerveja", 7.50))

    pedido2 = Pedido(2)
    pedido2.add_prato(Prato("Espaguete à Bolonhesa", 34.50))
    pedido2.add_prato(Prato("Torta de Limão", 12.00))

    cliente.add_pedido(pedido1)
    cliente.add_pedido(pedido2)

    cliente.listar_pedidos()
class Veiculo:
    def __init__(self, placa, marca, tipo):
        self.placa = placa
        self.marca = marca
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Veículo: {self.tipo} | Placa: {self.placa} | Marca: {self.marca}")


class Carro(Veiculo):
    def __init__(self, placa, marca, num_portas):
        super().__init__(placa, marca, "Carro")
        self.num_portas = num_portas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de portas: {self.num_portas}")


class Caminhao(Veiculo):
    def __init__(self, placa, marca, capacidade_carga):
        super().__init__(placa, marca, "Caminhão")
        self.capacidade_carga = capacidade_carga

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidade de carga: {self.capacidade_carga} kg")


class Motorista:
    def __init__(self, nome):
        self.nome = nome
        self.veiculos = []

    def add_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def rem_veiculo(self, veiculo):
        self.veiculos.remove(veiculo)

    def listar_veiculos(self):
        print(f"Veículos do motorista {self.nome}:")
        for veiculo in self.veiculos:
            veiculo.mostrar_info()


# Exemplo de uso
if __name__ == "__main__":
    motorista = Motorista("João")

    carro = Carro("ABC-1234", "Fusca", 2)
    caminhao = Caminhao("XYZ-5678", "Volvo", 10000.0)

    motorista.add_veiculo(carro)
    motorista.add_veiculo(caminhao)

    motorista.listar_veiculos()
