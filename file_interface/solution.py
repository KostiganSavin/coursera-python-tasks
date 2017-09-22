from tempfile import gettempdir

class File:
    """Класс реализующий интерфейс для работы с файлами"""

    def __init__(self, file_path):
        self.path = file_path

    def write(self, str_to_write):
        with open(self.path, "w") as f:
            f.write(str_to_write)

    def __add__(self, obj):
        new_obj = File("new_file.txt")
        
        with open(self.path) as first:
            first_file = first.read()
        with open(obj.path) as second:
            second_file = second.read()
        new_obj.write(first_file + "\n" + second_file + "\n")
        return new_obj 

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path) as f:
            return f.readline()

    def __str__(self):
        return f"{self.path}"


first = File("first.txt")
second = File("second.txt")

new_obj = first + second