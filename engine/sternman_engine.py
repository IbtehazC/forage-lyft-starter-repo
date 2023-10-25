from engine import Engine

class SternmanEngine(Engine):

    def __init__(self, last_service_mileage: int, current_mileage: int, warning_light_on: bool):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on or self.current_mileage - self.last_service_mileage > 12000
