import sys

sys.path.append('python-design-patterns')

from collections import defaultdict


class Mediator(object):

    def __init__(self):
        self.signals = defaultdict(list)

    def signal(self, signal_name, *args, **kwargs):
        for handler in self.signals[signal_name]:
            handler(*args, **kwargs)

    def connect(self, signal_name, receiver):
        self.signals[signal_name].append(receiver)

    def disconnect(self, signal_name, receiver):
        try:
            self.signals[signal_name].remove(receiver)
        except ValueError:
            pass
