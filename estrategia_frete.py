from abc import ABC, abstractmethod


class EstrategiaFrete(ABC):

    @abstractmethod
    def calcular(self, pedido) -> float:
        pass


class FreteSedex(EstrategiaFrete):

    def calcular(self, pedido) -> float:
        print("Calculando frete para: SEDEX")
        return 10.0 + (pedido.peso_kg * 1.5)


class FretePac(EstrategiaFrete):

    def calcular(self, pedido) -> float:
        print("Calculando frete para: PAC")
        return 5.0 + (pedido.peso_kg * 1.0)


class FreteTransportadora(EstrategiaFrete):

    def calcular(self, pedido) -> float:
        print("Calculando frete para: TRANSPORTADORA")
        return 20.0 + (pedido.peso_kg * 3.0)


class FreteMotoboy(EstrategiaFrete):

    def calcular(self, pedido) -> float:
        print("Calculando frete para: MOTOBOY")
        return 15.0


class FreteDrone(EstrategiaFrete):

    def calcular(self, pedido) -> float:
        print("Calculando frete para: DRONE")
        return 25.0
