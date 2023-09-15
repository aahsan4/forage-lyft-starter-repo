from abc import ABC, abstractmethod
from datetime import date

class Tire(ABC):
    @abstractmethod
    def needs_service(self, tire_wear: list[float]) -> bool:
        pass