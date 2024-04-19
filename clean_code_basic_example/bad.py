class MicroZoo:

    def __init__(self):
        self.v = 0
        self.b = 0


def main(stream):
    zoo = MicroZoo()
    for v, b in stream:
        zoo.v += v
        zoo.b += b
    if zoo.v > 1000 and zoo.b < 1000 or zoo.v < 1000 and zoo.b > 1000 or zoo.v > 1000 and zoo.b < 1000:
        print('There are a lot of virus or bacteria in this patient')
    else:
        print('Patient is fine')
