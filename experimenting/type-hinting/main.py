from typing import List

def main():
    print("--- Playing with type hinting ---")

    # List
    x : List[int] = []

    # list
    x: list[int] = []
    x = list[int]()
    print(type(x)) # <class 'list'>
    print(list[int] == list) # False
    print(list[int] == list[int]) # True

    # origin
    print(list[int]) # list[int]
    t = list[int]
    print(t.__origin__) # <class 'list'>
    print(t.__args__) # (<class 'int'>,)

if __name__ == "__main__":
    main()
