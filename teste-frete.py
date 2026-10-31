from pedido import Pedido
from estrategia_frete import (
    FreteSedex,
    FretePac,
    FreteTransportadora,
    FreteMotoboy,
    FreteDrone,
)


def main():
    print("*" * 30)
    print("Executando Versão Refatorada")
    print("*" * 30)

    pedido = Pedido(peso_kg=2.5)

    pedido.set_estrategia(FreteSedex())
    frete_sedex = pedido.calcular_frete()
    print(f"Valor do frete SEDEX: R$ {frete_sedex:.2f}")

    pedido.set_estrategia(FretePac())
    frete_pac = pedido.calcular_frete()
    print(f"Valor do frete PAC: R$ {frete_pac:.2f}")

    pedido.set_estrategia(FreteTransportadora())
    frete_transp = pedido.calcular_frete()
    print(f"Valor do frete TRANSPORTADORA: R$ {frete_transp:.2f}")

    pedido.set_estrategia(FreteMotoboy())
    frete_motoboy = pedido.calcular_frete()
    print(f"Valor do frete MOTOBOY: R$ {frete_motoboy:.2f}")

    pedido.set_estrategia(FreteDrone())
    frete_drone = pedido.calcular_frete()
    print(f"Valor do frete DRONE: R$ {frete_drone:.2f}")

    pedido2 = Pedido(peso_kg=10.0)
    pedido2.set_estrategia(FretePac())
    frete_pac = pedido2.calcular_frete()
    print(f"Valor do frete PAC: R$ {frete_pac:.2f}")


if __name__ == "__main__":
    main()
