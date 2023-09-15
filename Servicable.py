class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass