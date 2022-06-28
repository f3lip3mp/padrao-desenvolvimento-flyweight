
def lista_endereco():
    count = len(factory)
    print(f"FlyweightFactory: Eu tenho {count} flyweights:\n")
    print(factory)



def adiciona_endereco( rua: str, bairro: str, num: str):
    factory.append([rua, bairro, num])
    

if __name__ == "__main__":

    factory = ([
        ["Rua Bento Martins", "Centro Histórico", "528"],
        ["Rua Cel. Genuino", "Centro", "152"],
        ["Rua Fernando Machado", "Centro", "897"],
        ["Av. Ipiranga", "Jardim Botanico", "1008"],
        ["Rua dos Andradas", "Centro Histórico", "856"],
    ])

    lista_endereco()

    adiciona_endereco(
        "Rua Bento Martins", "Centro Histórico", "722")

    adiciona_endereco(
        "Rua Fernando Machado", "Centro", "897")

    print("\n")
    lista_endereco()