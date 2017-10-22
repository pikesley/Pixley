from Pixley.pixley import *

class PacMan(Pixley):
    def __init__(self, neopixels):
        super(PacMan, self).__init__(neopixels)

    def run(self):
        yellow = (127, 255, 0)
        blank = (0, 0, 0)

        seq = self.sequence()
        for set in seq:
            self.light(set['on'], yellow)
            self.light(set['off'], blank)
            self.show()
            time.sleep(0.05)

        seq.reverse()
        for set in seq:
            self.light(set['on'], yellow)
            self.light(set['off'], blank)
            self.show()
            time.sleep(0.05)

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
            for j in range(2):
                off.append(on.pop(4 - i))
            seq.append({
                "on": on[:],
                "off": sorted(off[:])
            })

        return seq
