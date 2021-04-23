import abc
import inspect


class Loader(abc.ABC):
    @abc.abstractmethod
    def load(self):
        pass


def get_loaders():
    from .dummy import DummyLoader
    from .structured import CsvLoader

    for cls in locals().values():
        if inspect.isclass(cls) and issubclass(cls, Loader) and cls != Loader:
            yield cls
