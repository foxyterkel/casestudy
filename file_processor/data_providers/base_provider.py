from abc import abstractmethod


class BaseProvider:

    @abstractmethod
    def provide(self):
        pass
