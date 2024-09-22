"""
In cadrul acestui fisier implementam interfata abstracta GradinitaABC cu 2 metode abstracte
"""

from abc import ABC, abstractmethod


class GradinitaABC(ABC):

    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        pass
