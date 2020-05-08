"""
Exploits fact that Python treats function as first class objects.
Gives us more flexibility because method no longer needs to be consistent.
Therefore subscriber can register even without the right interface. 

"""


class SubscriberOne:
    """ One type of subscriber with update method. """

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))


class SubscriberTwo:
    """ Another type of subscriber with receive method. """

    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print('{} got message "{}"'.format(self.name, message))



class Publisher:
    
    def __init__(self):
        # Now subscribers is a dict instead of a set
        self.subscribers = dict()

    def register(self, who, callback=None):
        """         
        When the subscriber invokes the register method we want to provide
        a function argument. We want the observer to have a callback function
        invoked or called when the notification goes out. 
        That is the channel or mechanism by which the subscriber is notified. 
        """
        if callback is None:
            # fallback to original method
            callback = getattr(who, 'update')
        self.subscribers[who] = callback

    def unregister(self, who):
        del self.subscribers[who]

    def dispatch(self, message):
        for subscriber, callback in self.subscribers.items():
            callback(message)


if __name__ == '__main__':
    pub = Publisher()

    bob = SubscriberOne('Bob')
    alice = SubscriberTwo('Alice')
    john = SubscriberOne('John')

    pub.register(bob, bob.update)
    pub.register(alice, alice.receive)
    pub.register(john)

    pub.dispatch("It's lunchtime!")
    pub.unregister(john)
    pub.dispatch("Time for dinner")