from Pixley.pixley import *

class PacMan(Pixley):
    def __init__(self, neopixels):
        super(PacMan, self).__init__(neopixels)

    # def run(self):
    #     seq = self.sequence()
    #     for pair in seq[:-1]:
    #         self.light_all((63, 0, 0))
    #         self.light(pair, (255, 0, 0))
    #         self.show()
    #
    #     seq.reverse()
    #     for pair in seq[:-1]:
    #         self.light_all((63, 0, 0))
    #         self.light(pair, (255, 0, 0))
    #         self.show()

    def sequence(self):
        on = list(range(16, 32))
        off = []
        seq = [
            {
                "on": on[:],
                "off": off[:]
            }
        ]

        for i in range(4):
            off.append(on.pop(0))
            off.append(on.pop(-1))
            seq.append({
                "on": on[:],
                "off": sorted(off[:])
            })

        return seq
