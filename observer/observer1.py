"""
Illustrates simple implementation of observer pattern.
"""


class Subscriber:
    """ Observer. """

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))


class Publisher:
    """ Observable. 
    
    Allows subscribers or observers to register and unregister.
    Dispatches messages to all registered subscribers.
    """
    
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


if __name__ == '__main__':
    pub = Publisher()

    bob = Subscriber('Bob')
    alice = Subscriber('Alice')
    john = Subscriber('John')

    pub.register(bob)
    pub.register(alice)
    pub.register(john)

    pub.dispatch("It's lunchtime!")
    pub.unregister(john)
    pub.dispatch("Time for dinner")