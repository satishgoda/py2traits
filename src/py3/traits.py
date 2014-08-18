#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
'''
   Copyright 2014 Teppo Perä

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''


from .trait_factory import TraitSource


class Traits(object):
    """
    Collection class for traits.
    """
    def __init__(self, traits):
        self._traits = [TraitSource(trait) for trait in traits]

    def __iter__(self):
        for trait in self._traits:
            try:
                for part in trait:
                    yield part
            except TypeError:
                yield trait
