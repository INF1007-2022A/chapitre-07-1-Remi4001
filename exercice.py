#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from chapitre6 import frequence

# Définissez vos fonction ici


def calculer_volume_masse(a, b, c, masse_volumique) -> tuple:
    volume = 4/3 * math.pi * a * b * c
    return volume, volume * masse_volumique


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(calculer_volume_masse(1, 2, 3, 2))
    print(calculer_volume_masse(3/(4*math.pi), 1, 1, 15.25))
    print((lambda string: sorted(frequence(string),
          key=frequence(string).__getitem__)[-1])("test"))

    pass
