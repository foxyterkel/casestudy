from abc import abstractmethod


class BaseWriter:

    @abstractmethod
    def write(self, data_frame):
        pass
