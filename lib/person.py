#!/usr/bin/env python3

class Person:
    jobs = ["ITC"]
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str and len(name) > 0 and len(name) < 26:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in Person.jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
