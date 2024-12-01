# https://youtu.be/33d4-al29AA
# https://replit.com/@pedrovilarinhog/pedroAndradePI?v=1
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def exibir_dados(self):
        return f"Nome: {self.__nome}, Idade: {self.__idade}, CPF: {self.__cpf}"


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, cargo, salario):
        super().__init__(nome, idade, cpf)
        self.__cargo = cargo
        self.__salario = salario

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def exibir_dados(self):
        dados_pessoa = super().exibir_dados()
        return f"{dados_pessoa}, Cargo: {self.__cargo}, Salário: R${self.__salario:.2f}"


class Hospede(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)
        self.__reservas = []

    def adicionar_reserva(self, reserva):
        self.__reservas.append(reserva)

    def listar_reservas(self):
        return [reserva.exibir_dados() for reserva in self.__reservas]

    def exibir_dados(self):
        dados_pessoa = super().exibir_dados()
        return f"{dados_pessoa}, Reservas: {len(self.__reservas)}"


class Quarto:
    def __init__(self, numero, tipo, preco):
        self.__numero = numero
        self.__tipo = tipo
        self.__preco = preco
        self.__disponivel = True

    def get_numero(self):
        return self.__numero

    def get_tipo(self):
        return self.__tipo

    def get_preco(self):
        return self.__preco

    def is_disponivel(self):
        return self.__disponivel

    def reservar(self):
        self.__disponivel = False

    def liberar(self):
        self.__disponivel = True

    def exibir_dados(self):
        status = "Disponível" if self.__disponivel else "Reservado"
        return f"Quarto {self.__numero}: Tipo {self.__tipo}, Preço R${self.__preco:.2f}, Status: {status}"


class Reserva:
    def __init__(self, hospede, quarto, data_checkin, data_checkout):
        self.__hospede = hospede
        self.__quarto = quarto
        self.__data_checkin = data_checkin
        self.__data_checkout = data_checkout

    def get_quarto(self):
        return self.__quarto

    def exibir_dados(self):
        return (f"Reserva de {self.__hospede.get_nome()} no quarto {self.__quarto.get_numero()}, "
                f"Check-in: {self.__data_checkin}, Check-out: {self.__data_checkout}")


class Hotel:
    def __init__(self, nome):
        self.__nome = nome
        self.__quartos = []
        self.__reservas = []
        self.__funcionarios = []

    def adicionar_quarto(self, quarto):
        self.__quartos.append(quarto)

    def adicionar_funcionario(self, funcionario):
        self.__funcionarios.append(funcionario)

    def listar_quartos_disponiveis(self):
        return [quarto for quarto in self.__quartos if quarto.is_disponivel()]

    def realizar_reserva(self, hospede, numero_quarto, data_checkin, data_checkout):
        for quarto in self.__quartos:
            if quarto.get_numero() == numero_quarto and quarto.is_disponivel():
                reserva = Reserva(hospede, quarto, data_checkin, data_checkout)
                self.__reservas.append(reserva)
                hospede.adicionar_reserva(reserva)
                quarto.reservar()
                return reserva
        return None

    def listar_reservas(self):
        return [reserva.exibir_dados() for reserva in self.__reservas]

    def exibir_dados_funcionarios(self):
        return [funcionario.exibir_dados() for funcionario in self.__funcionarios]


def main():
    hotel = Hotel("Hotel dos Sonhos")
    

    quarto1 = Quarto(101, "Solteiro", 150.00)
    quarto2 = Quarto(102, "Casal", 200.00)
    quarto3 = Quarto(201, "Luxo", 350.00)

    hotel.adicionar_quarto(quarto1)
    hotel.adicionar_quarto(quarto2)
    hotel.adicionar_quarto(quarto3)

    funcionario1 = Funcionario("Ana Costa", 30, "123.456.789-00", "Recepcionista", 2500.00)
    funcionario2 = Funcionario("Paulo Silva", 45, "987.654.321-00", "Gerente", 5000.00)

    hotel.adicionar_funcionario(funcionario1)
    hotel.adicionar_funcionario(funcionario2)

    hospede1 = Hospede("Carlos Souza", 35, "456.123.789-00")
    hospede2 = Hospede("Fernanda Lima", 28, "789.456.123-00")

    reserva1 = hotel.realizar_reserva(hospede1, 101, "2024-11-20", "2024-11-25")
    reserva2 = hotel.realizar_reserva(hospede2, 102, "2024-11-22", "2024-11-27")

    print("Quartos disponíveis após reservas:")
    for quarto in hotel.listar_quartos_disponiveis():
        print(quarto.exibir_dados())

    print("\nReservas realizadas:")
    for reserva in hotel.listar_reservas():
        print(reserva)

    print("\nFuncionários do hotel:")
    for funcionario in hotel.exibir_dados_funcionarios():
        print(funcionario)


if __name__ == "__main__":
    main()
