import os
import json


def test1():
    print(os.getenv("MI_VARIABLE"))


def test2():
    my_list = ["Hola", "Holass", "Chauy"]
    with open("test_data.json", "w") as file:
        json.dump(my_list, file)


if __name__ == "__main__":
    test2()
