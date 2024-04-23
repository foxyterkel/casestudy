from abc import abstractmethod


class BaseProcessor:

    @abstractmethod
    def process(self, file_object):
        pass
