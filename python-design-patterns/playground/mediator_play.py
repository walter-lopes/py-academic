import sys
sys.path.append('../../python-design-patterns')

from behavioral.mediator import Mediator


class Dog(object):
    sound = ''

    def set_sound(self, sound):
        self.sound = sound


class Cat(object):
    sound = ''

    def set_sound(self, sound):
        self.sound = sound


dog = Dog()
cat = Cat()

mediator = Mediator() # Create a Mediator object.

mediator.connect('set_dog_sound', dog.set_sound) # Connect the signal 'set_dog_sound' to the dog.set_sound method.
mediator.connect('set_cat_sound', cat.set_sound) # Connect the signal 'set_cat_sound' to the cat.set_sound method.

mediator.connect('set_sound', dog.set_sound) # Also connect the signal 'set_sound' to the dog.set_sound method.
mediator.connect('set_sound', cat.set_sound) # Also connect the signal 'set_sound' to the cat.set_sound method.

mediator.signal('set_sound', 'foo') # Send out the signal 'set_sound'
                                    # with an argument to be passed to the connected methods.
                                    # (Sets dog.sound and cat.sound to 'foo')


assert 'foo' == dog.sound
assert 'foo' == cat.sound

mediator.signal('set_dog_sound', 'woof') # Send out the signal 'set_dog_sound'
                                         # (Sets dog.sound to 'woof')
mediator.signal('set_cat_sound', 'meow') # Send out the signal 'set_cat_sound'
                                         # (Sets cat.sound to 'meow')

assert 'woof' == dog.sound
assert 'meow' == cat.sound

mediator.disconnect('set_sound', dog.set_sound) # Disconnect the method dog.sound from the signal 'set_sound'

mediator.signal('set_sound', 'bar') # Send out the signal 'set_sound'
                                    # (Only sets cat.sound to 'bar' because we disconnected dog.sound)

assert 'woof' == dog.sound
assert 'bar' == cat.sound