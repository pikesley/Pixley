from Pixley.pixley import *

class KnightRider(Pixley):
    def __init__(self, neopixels):
        super(KnightRider, self).__init__(neopixels)

    def run(self):
        seq = self.sequence()
        for pair in seq[:-1]:
            self.light(pair, (255, 0, 0))
            self.show()
            time.sleep(0.01)
            self.light_all((63, 0, 0))

        seq.reverse()
        for pair in seq[:-1]:
            self.light(pair, (255, 0, 0))
            self.show()
            time.sleep(0.01)
            self.light_all((63, 0, 0))


    def sequence(self):
        offset = 4
        count = self.neopixels.n

        tops = []
        for i in range(count / 4):
            tops.append(i + offset)

        bottoms = []
        for i in range(count / 4, 0, -1):
            v = i - offset - 1
            if v < 0:
                v = (count / 2) + v
            bottoms.append(v)

        for i in range(count / 4):
            tops.append(i + offset + (count / 2))

        for i in range(count / 4, 0, -1):
            v = (i - offset - 1) + count / 2
            if v < count / 2:
                v = (count / 2) + v
            bottoms.append(v)

        seq = []
        for i in range(count / 2):
            seq.append([int(tops[i]), int(bottoms[i])])

        return seq
