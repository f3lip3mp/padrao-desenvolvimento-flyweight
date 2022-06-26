import json
from typing import Dict


class Flyweight():

    def __init__(self, est_compartilhado: str) -> None:
        self._est_compartilhado = est_compartilhado

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._est_compartilhado)
        u = json.dumps(unique_state)
        print(f"Flyweight: Exibindo dados compartilhados: ({s}). E dados únicos: ({u}).", end="")


class FlyweightFactory():
    
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
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

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: Eu tenho {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def adiciona_carro(
    factory: FlyweightFactory, marca: str, modelo: str, cor: str
) -> None:
    print("\n\nClient: Adicionando carro na base de dados.")
    factory.get_flyweight([marca, modelo, cor])


if __name__ == "__main__":

    factory = FlyweightFactory([
        ["Fiat", "Uno", "preto"],
        ["Fiat", "Camaro", "amarelo"],
        ["Nissan", "March", "preto"],
        ["Nissan", "Kicks", "branco"],
        ["Honda", "Civic", "preto"],
    ])

    factory.list_flyweights()

    adiciona_carro(
        factory, "Nissan", "Kicks", "branco")

    adiciona_carro(
        factory, "Honda", "Civic", "preto")

    print("\n")

    factory.list_flyweights()