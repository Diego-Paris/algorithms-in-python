"""
Python doesn't support method overloading
but we can use default function arguments
"""

class Test():

    def __init__(self, a, b=2, c=3) -> None:
        self.a = a
        self.b = b
        self.c = c

    def print_values(self):
        print(self.a)
        print(self.b)
        print(self.c)
        


def main():
    print("--- method overloading testing ---")

    test1 = Test()
    test1.print_values()




if __name__ == "__main__":
    main()