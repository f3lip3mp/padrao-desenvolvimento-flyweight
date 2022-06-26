
def list_cars():
    count = len(factory)
    print(f"FlyweightFactory: Eu tenho {count} flyweights:\n")
    print(factory)



def add_car_to_police_database( marca: str, modelo: str, cor: str):
    factory.append([marca, modelo, cor])
    

if __name__ == "__main__":

    factory = ([
        ["Fiat", "Uno", "preto"],
        ["Fiat", "Camaro", "amarelo"],
        ["Nissan", "March", "preto"],
        ["Nissan", "Kicks", "branco"],
        ["Honda", "Civic", "preto"],
    ])

    list_cars()

    add_car_to_police_database(
        "Nissan", "Kicks", "branco")

    add_car_to_police_database(
        "Honda", "Civic", "preto")

    print("\n")
    list_cars()