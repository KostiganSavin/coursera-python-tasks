import csv

class CarBase:

    car_type = None

    def __init__(self, brand, photo_filename, carrying):
        self.brand = brand
        self.photo_filename = photo_filename
        self.carrying = carrying


class Car(CarBase):

    def __init__(self, brand, photo_filename, carrying, passenger_seats_count):
        super().__init__(brand, photo_filename, carrying)
        self.car_type = car
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):

    def __init__(self, brand, photo_filename, carrying, body_whl):
        super().__init__(brand, photo_filename, carrying)
        self.car_type = truck
        pass


class SpecialMachine(CarBase):
    
    def __init__(self, brand, photo_filename, carrying, extra):
        super().__init__(brand, photo_filename, carrying)
        self.car_type = spec_machine
        self.extra = extra
        

def get_car_list(csv_filename):
    car_list = []
    return car_list


def _main():
    with open("coursera_week3_cars.csv", "r", encoding="utf-8") as csv_fd:
        reader = csv.reader(csv_fd, delimiter=";")
        next(reader)
        for row in reader:
            print(row)


if __name__ == "__main__":
    _main()
