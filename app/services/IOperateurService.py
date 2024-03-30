from abc import ABC, abstractmethod
from typing import List
from models import Operateur

class IOperateurService(ABC):

    @abstractmethod
    def retrieve_all_operateurs(self) -> List[Operateur.Operateur]:
        pass

    @abstractmethod
    def add_operateur(self, operateur: Operateur) -> Operateur:
        pass

    @abstractmethod
    def delete_operateur(self, operateur_id: int) -> None:
        pass

    @abstractmethod
    def update_operateur(self, operateur: Operateur) -> Operateur:
        pass

    @abstractmethod
    def retrieve_operateur(self, operateur_id: int) -> Operateur:
        pass
