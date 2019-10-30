#! /usr/bin/env python

import time
import random


class ExternalDependency(object):

    # We don't want to use this external dependency directly in our tests -
    # it is slow and returns non-deterministic results
    def get_number(self):
        time.sleep(10)
        return int(random.random() * 100)


def use_dependency_internally(number):
    dependency = ExternalDependency()
    return number * dependency.get_number()


def use_injected_dependency(dependency, number):
    return number * dependency.get_number()


if __name__ == '__main__':

    print("Demoing version with internal dependency")
    returned_value_1 = use_dependency_internally(2)
    print("Returned value was", returned_value_1)

    print("Demoing versoin with injected dependency")
    injectable_dependency = ExternalDependency()
    returned_value_2 = use_injected_dependency(injectable_dependency, 2)
    print("Returned value was", returned_value_2)
