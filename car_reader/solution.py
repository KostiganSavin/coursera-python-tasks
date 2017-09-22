import csv
import os

class CarBase:

    def __init__(self, brand, photo_file_name, carrying, car_type=None):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]

    def __str__(self):
        return f"{self.car_type} - {self.brand}"

    def __repr__(self):
        return f"{self.car_type} - {self.brand}"
    
class Car(CarBase):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying, car_type="car")
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying, car_type="truck")
        if body_whl:
            try:
                body_dimensions = body_whl.split("x")
                self.body_width = float(body_dimensions[0])
                self.body_height = float(body_dimensions[1])
                self.body_length = float(body_dimensions[2])
            except ValueError:
                raise
        else:
            self.body_width = 0.0
            self.body_height = 0.0
            self.body_length = 0.0


    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length  


class SpecialMachine(CarBase):
    
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying, car_type="spec_machine")
        self.extra = extra      


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, encoding="utf-8") as csv_fd:
        reader = csv.DictReader(csv_fd, delimiter=";")
        for row in reader:
            if not (row["car_type"] and row["brand"] and row["photo_file_name"]
                    and row["carrying"]):
                continue
            try:
                if row["car_type"] == "car":
                    car = Car(brand = row["brand"], 
                            photo_file_name= row["photo_file_name"], 
                            carrying = row["carrying"], 
                            passenger_seats_count = row["passenger_seats_count"])
                if row["car_type"] == "truck":
                    car = Truck(brand = row["brand"], 
                                photo_file_name= row["photo_file_name"], 
                                carrying = row["carrying"],
                                body_whl = row["body_whl"])

                if row["car_type"] == "spec_machine":
                    car = SpecialMachine(brand = row["brand"], 
                                                photo_file_name= row["photo_file_name"],
                                                carrying = row["carrying"],
                                                extra = row["extra"])
                car_list.append(car)
            except ValueError:
                continue
        return car_list
                

def _main():
    print(get_car_list("coursera_week3_cars.csv"))


if __name__ == "__main__":
    _main()
