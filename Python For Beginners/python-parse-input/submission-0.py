from typing import List

def read_integers() -> List[int]:
    result = []
    for x in input().split(","):
        result.append(int(x))
    return result

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
