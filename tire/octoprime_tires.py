from serviceable import Serviceable

class OctoprimeTires(Serviceable):

    def __init__(self, wear_array):
        self.wear_array = wear_array

    def needs_service(self):
        return sum(self.wear_array) >= 3
