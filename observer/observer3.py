"""
Source: https://www.youtube.com/watch?v=87MNuBgeg34

We can have observable that can notify one group of subscribers for one kind of situation.
Notify a different group of subscribers for different kind of situation.
We can have the same subscribers in both groups.
We call these situations events (different kinds of situations) or channels.
This gives us the flexibility of how we notify subscribers.

"""


class Subscriber:
    """ Sample observer. """

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))


class Publisher:
    
    def __init__(self, events):
        """
        We want to provide interface that allows subscribers to register for a specific event that the observable can announce.
        So we modify a publisher to take several events and modify the subscriber attribute to
        map event names to strings to dictionaries that then map subscribers to their callback function
        """
        self.subscribers = {event: dict() for event in events}

    def get_subscribers(self, event):
        """ Helper method. 

        Look up for a given even the map of subscriber to the callback function.
        """
        return self.subscribers[event]

    def register(self, event, who, callback=None):
        """ Change the way we insert the subscriber to our records of the callback."""
        if callback is None:
            # fallback to original method
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        """ We keep the api interface fairly similar."""
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)


if __name__ == '__main__':
    pub = Publisher(['lunch', 'dinner'])

    bob = Subscriber('Bob')
    alice = Subscriber('Alice')
    john = Subscriber('John')

    pub.register("lunch", bob)
    pub.register("dinner", alice)
    pub.register("lunch", john)
    pub.register("dinner", john)

    pub.dispatch("lunch", "It's lunchtime!")
    pub.dispatch("dinner", "Dinner is served")