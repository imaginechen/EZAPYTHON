from typing import List

def update(a: List[int]) -> None:
    list_temp = a.copy()
    list_temp[2] = 3


if __name__ == "__main__":
    list1 = [12,65,43]
    print(list1[-1])