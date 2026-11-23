from base_ride import Ride

class StandardRide(Ride):
    def __init__(self, distance_km):
        super().__init__(distance_km)
        self.__base_fare = 5.00
    def calculate_fare(self):
        return self.__base_fare + (self.distance_km * 1.50)
    def start_ride(self):
        print(f"Starting standard ride for {self.distance_km} km.")
    def complete_ride(self):
        print(f"Completing standard ride for {self.distance_km} km. Total fare: ${self.calculate_fare():.2f}")
