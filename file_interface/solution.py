from tempfile import gettempdir
import os

class File:
    """Класс реализующий интерфейс для работы с файлами"""

    def __init__(self, file_path):
        self.path = file_path
        self.position = None
        
    def write(self, str_to_write):
        with open(self.path, "w") as f:
            f.write(str_to_write)

    def __add__(self, obj):
       
        new_obj = File(os.path.join(gettempdir(),"new_file.txt"))

        try:
            with open(self.path) as first:
                first_file = first.read()
        except FileNotFoundError:
            first_file = ""
        try:
            with open(obj.path) as second:
                second_file = second.read()
        except FileNotFoundError:
            second_file = ""

        new_obj.write(first_file + "\n" + second_file + "\n")
        return new_obj 

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path) as f:
            if not self.position:
                f.seek(0)
            else:
                f.seek(self.position)
            line = f.readline().rstrip()
            self.position = f.tell()
            if line:
                return line
            else:
                raise StopIteration

    def __str__(self):
        return f"{self.path}"


# first = File("first.txt")
# second = File("second.txt")

# new_obj = first + second

# for line in File("text.txt"):
#    print(line)