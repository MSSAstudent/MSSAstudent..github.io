#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab08, exercise5, Employee Class

from Person import Person

class Employee(Person):
    def __init__(self, name, address, age, job_skills, yrw):
        super().__init__(name, address, age)

        self._job_skills = job_skills
        self._yrw = yrw

    def get_job_skills(self):
        return self._job_skills
    def set_job_skills(self, job_skills):
        self._job_skills = job_skills

    def get_yrw(self):
        return self._yrw
    def set_yrw(self, yrw):
        self._yrw = yrw

    def to_string(self):
        return super().to_string() + " Job skills: " + self._job_skills + \
               " Years of experiance: " + str(self._yrw)
