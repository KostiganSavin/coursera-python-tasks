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
        body_dimensions = body_whl.split("x")
        # print(body_dimensions)
        try:
            self.body_width = float(body_dimensions[0])
            self.body_heigth = float(body_dimensions[1])
            self.body_length = float(body_dimensions[2])
        except ValueError:
            self.body_width = 0.0
            self.body_height = 0.0
            self.body_length = 0.0
        
    def get_body_volue(self):
        return self.body_width * self.body_height * self.body_length  


class SpecialMachine(CarBase):
    
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying, car_type="extra")
        self.extra = extra
        

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, "r", encoding="utf-8") as csv_fd:
        reader = csv.reader(csv_fd, delimiter=";")
        next(reader)
        for row in reader:
            if len(row) != 0:
                try:
                    if row[0] == "car":
                        car = Car(row[1], row[3], row[5], row[2])
                        car_list.append(car)
                    elif row[0] == "truck":
                        truck = Truck(row[1], row[3], row[5], row[4])
                        car_list.append(truck)
                    elif row[0] == "spec_machine":
                        spec_machine = SpecialMachine(row[1], row[3], row[5], row[6])
                        car_list.append(spec_machine)
                except IndexError:
                    continue
            # print(row)
    return car_list


def _main():
    print(get_car_list("coursera_week3_cars.csv"))

if __name__ == "__main__":
    _main()
