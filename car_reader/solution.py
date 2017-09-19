import csv

class CarBase:
   
    def __init__(self, brand, photo_filename, carrying):
        pass 

class Car(CarBase):

    def __init__(self, brand, photo_filename, carrying, passenger_seats_count):
        pass

class Truck(CarBase):

    def __init__(self, brand, photo_filename, carrying, body_whl):
        pass

class SpecialMachine(CarBase):
    
    def __init__(self, brand, photo_filename, carrying, extra):
        pass
        

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
