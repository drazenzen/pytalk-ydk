#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

a = range(100)
b = range(50)
c = range(20)

out = sorted(set(itertools.chain(filter(lambda i: i % 3 == 0, a), filter(lambda i: i % 4 == 0, b), map(lambda i: i - 40, c))))
print(out)


# KISS
# Keep all numbers divisible by 3
a = list(filter(lambda i: i % 3 == 0, a))
# Keep all numbers divisible by 4
b = list(filter(lambda i: i % 4 == 0, b))
# Reduce all numbers by 40
c = list(map(lambda i: i - 40, c))
# Sort and merge together a, b and c and remove all duplicates
out = sorted(set(itertools.chain(a, b, c)))
print(out)
