"""
Create a very general adapter class for any minion.
"""


class Elf:
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
        self.minion = minion
        
        for key, value in adapted_methods.items():
            func = getattr(self.minion, value)  # get function from actual minion
            self.__setattr__(key, func)   # and set on the adapter

        self.__initialised = True

    def __getattr__(self, attr):
        """ Attributes not in Adapter are delegated to the minion."""
        return getattr(self.minion, attr)

    def __setattr




class DwarfAdapter:
    def __init__(self, dwarf):
        self.dwarf = dwarf

    def call_me(self):
        self.dwarf.estver_narho()


class HumanAdapter:
    def __init__(self, human):
        self.human = human

    def call_me(self):
        self.human.ring_mig()







if __name__ == '__main__':
    minions = [
        ElfAdapter(Elf()), 
        DwarfAdapter(Dwarf()), 
        HumanAdapter(Human())
        ]

    for minion in minions:
        minion.call_me()