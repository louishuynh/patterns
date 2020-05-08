"""
Create a very general adapter class for any minion.
"""


class Elf:
    def __init__(self):
        self.name = 'Orlando'

    def nall_nin(self):
        print('Elf says: Calling the Overlord...')


class Dwarf:
    def estver_narho(self):
        print('Dwarf says: Calling the Overlord...')


class Human:
    def ring_mig(self):
        print('Human says: Calling the Overlord...')


class MinionAdapter:
    __initialised = False

    def __init__(self, minion, **adapted_methods):
        """ adaptered_methods is a dict mapping of new name to old name """
        self.minion = minion
        
        for key, value in adapted_methods.items(): 
            func = getattr(self.minion, value)  # get function from actual minion
            self.__setattr__(key, func)   # and set on the adapter

        self.__initialised = True

    def __getattr__(self, attr):
        """ Attributes not in Adapter are delegated to the minion."""
        # You can get and set any attribute still on minion and not on Adapter.
        return getattr(self.minion, attr)

    def __setattr__(self, key, value):
        """ Set attributes normally during initialisation."""
        if not self.__initialised:
            super().__setattr__(key, value)
        else:
            """ Set attribute on minion after initialisation."""
            setattr(self.minion, key, value)


if __name__ == '__main__':
    minion_adapters = [
        MinionAdapter(Elf(), call_me='nall_nin'),
        MinionAdapter(Dwarf(), call_me='estver_narho'),
        MinionAdapter(Human(), call_me='ring_mig'),        
    ]

    for adapter in minion_adapters:
        adapter.call_me()
        
    elf_adapter = minion_adapters[0]
    print('')
    print(f'Name from Adapter: {elf_adapter.name}')
    print(f'Name from Minion: {elf_adapter.minion.name}')

    elf_adapter.name = 'Bloom'

    print('')
    print(f'Name from Adapter: {elf_adapter.name}')
    print(f'Name from Minion: {elf_adapter.minion.name}')