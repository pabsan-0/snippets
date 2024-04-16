import time
class Timer:
    def __init__(self, avg=1):
        self.__tic = None
        self.__tac = None
        self.buffer = [None] * avg

    def tic(self):
        self.__tic = time.time()

    def tac(self):
        self.__tac = time.time()
        self.buffer = self.buffer[1:] + [self.__tac - self.__tic]
        return self.time()

    def time(self):
        buf = [ii for ii in self.buffer if ii is not None]
        return sum(buf) / len(buf)
