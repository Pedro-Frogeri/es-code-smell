from estrategia_frete import EstrategiaFrete


class Pedido:

    def __init__(self, peso_kg: float):
        self._peso_kg = peso_kg
        self.estrategia: EstrategiaFrete = None

    def set_estrategia(self, estrategia: EstrategiaFrete):
        self.estrategia = estrategia

    def calcular_frete(self) -> float:
        return self.estrategia.calcular(self)

    @property
    def peso_kg(self) -> float:
        return self._peso_kg
