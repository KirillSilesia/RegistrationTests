import random

def generate_nip():
    weights = [6,5,7,2,3,4,5,6,7]
    while True:
        first9 = [random.randint(0,9) for _ in range(9)]
        checksum = sum(d * w for d, w in zip(first9, weights)) % 11
        if checksum !=10:
            return "".join(map(str, first9)) + str(checksum)