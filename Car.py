from engine import Engine
from battery import Battery
from tire import Tire

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self, tire_wear: list[float]) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service(tire_wear)