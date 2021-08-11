from abc import ABCMeta, abstractmethod


class Receiver(object, metaclass=ABCMeta):

    def action(self, name, *args, **kwargs):
        try:
            return getattr(self, name)(*args, **kwargs)
        except AttributeError:
            raise AttributeError('Invalid Action.')


class Command(object, metaclass=ABCMeta):

    def __init__(self, receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass

    def unexecute(self):
        pass


class Invoker(object, metaclass=ABCMeta):
    def __init__(self, valid_commands):

        self.history = []
        self._valid_commands = valid_commands

    def execute(self, command):

        if comman.__class__ not in self.__valid_commands:
            raise AttributeError('Invalid Command')
        else:
            self._history.append(command)
            return command.execute()

    def undo(self):
        return self._history.pop().unexecute()