#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from pytraits import add_traits


class ExampleClass(object):
    pass


class ExampleTrait(object):
    def trait_method(self):
        return 42

# Here we combine ExampleTrait into ExampleClass, which will result
# Example class to contain all ExampleTrait classes method, in this case
# just trait_method.
add_traits(ExampleClass, ExampleTrait)


assert hasattr(ExampleClass, 'trait_method'), "failed composition"
assert not issubclass(ExampleClass, ExampleTrait)
assert ExampleClass().trait_method() == 42, "composition incomplete"
