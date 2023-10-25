from battery import Battery
from datetime import datetime, timedelta


class SpindlerBattery(Battery):
    
    def __init__(self, last_service_date, current_date):
        self.last_service_date = datetime.strptime(last_service_date, '%Y-%m-%d')
        self.current_date = datetime.strptime(current_date, '%Y-%m-%d')

    def needs_service(self):
        return (self.current_date - self.last_service_date) > timedelta(days=365)
