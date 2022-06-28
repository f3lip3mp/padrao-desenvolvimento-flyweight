import json
from typing import Dict


class Flyweight():

    def __init__(self, est_compartilhado: str) -> None:
        self._est_compartilhado = est_compartilhado

    def operation(self, est_unico: str) -> None:
        s = json.dumps(self._est_compartilhado)
        u = json.dumps(est_unico)
        print(f"Flyweight: Exibindo dados compartilhados: ({s}). E dados únicos: ({u}).", end="")


class FlyweightFactory():
    
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, flyweight_inicial: Dict) -> None:
        for state in flyweight_inicial:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:

        return "_".join(sorted(state))

    def get_flyweight(self, est_compartilhado: Dict) -> Flyweight:
        
        #Retorna um Flyweight existente com o estado dado ou cria um novo.

        key = self.get_key(est_compartilhado)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Não foi possível encontrar o flyweight, criando um novo...")
            self._flyweights[key] = Flyweight(est_compartilhado)
        else:
            print("FlyweightFactory: Reutilizando um flyweight existente...")

        return self._flyweights[key]

    def lista_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: Eu tenho {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def adiciona_endereco(
    factory: FlyweightFactory, rua: str, bairro: str, num: str
) -> None:
    print("\n\nClient: Adicionando endereco na base de dados.")
    factory.get_flyweight([rua, bairro, num])
    # O código do cliente armazena ou calcula o estado extrínseco e passa aos métodos do flyweight.

if __name__ == "__main__":

    factory = FlyweightFactory([
        ["Rua Bento Martins", "Centro Histórico", "528"],
        ["Rua Cel. Genuino", "Centro", "152"],
        ["Rua Fernando Machado", "Centro", "897"],
        ["Av. Ipiranga", "Jardim Botanico", "1008"],
        ["Rua dos Andradas", "Centro Histórico", "856"],
    ])

    factory.list_flyweights()

    adiciona_endereco(
        factory, "Rua Bento Martins", "Centro Histórico", "722")

    adiciona_endereco(
        factory, "Rua Fernando Machado", "Centro", "897")

    print("\n")

    factory.list_flyweights()