from tire import Tire

class OctoprimeTire(Tire):
    def needs_service(self, tire_wear: list[float]) -> bool:
        return sum(tire_wear) >= 3.0