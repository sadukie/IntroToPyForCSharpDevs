import abc

class CastMember(abc.ABC):
    """Cast member of a circus"""
    def __init__(self,name):
        self.name = name

    @abc.abstractmethod
    def move(self):
        pass