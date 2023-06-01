 #!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise5, Student Class

from Person10 import Person
from CustomExceptions import InvalidUnits

class Student(Person):
    def __init__(self, name, address, age, major, unit_comp):
        super().__init__(name, address, age)

        self._major = major
        self.set_unit_comp(unit_comp)

    def get_major(self):
        return self._major
    def set_major(self, major):
        self._major = major

    def get_unit_comp(self):
        return self._unit_comp
    def set_unit_comp(self, unit_comp):
        
        if unit_comp >= 0 and unit_comp <= 200:
            self._unit_comp = unit_comp
        else:
            raise InvalidUnits
        self._unit_comp = unit_comp

    def to_string(self):
        return super().to_string() + " College Major: " + self._major + \
               " College units complted: " + str(self._unit_comp)
