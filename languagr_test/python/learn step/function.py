
import sys

def func():
    print("This a example of function")

class MyClass:
    def __init__(self, data):
        print("class __init__ call")
        self.data = data
        print(self.data)

    def __call__(self, data):
        print("__call__ call")
        self.data *= data
        print(self.data)
        return data


if __name__ == "__main__":
    print(sys.argv)
    print("main")
    func()
    p = MyClass(3)
    print(p(5))

