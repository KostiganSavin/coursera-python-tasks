class Value:
    
    def __init__(self):
        self.value = None

    @staticmethod
    def _count_value(value, commission):
        #print("enter method")
        return value * commission

    def __get__(self, obj, obj_type):
        #print("getting value")
        return self.value

    def __set__(self, obj, value):
        #print("setting value")
        self.value = int(value - self._count_value(value, obj.commission))


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

def _main():
    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)

if __name__ == "__main__":
    _main()