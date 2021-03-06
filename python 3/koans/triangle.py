#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    dimensions = {a, b, c}

    for dim in dimensions:
        if dim <= 0: raise TriangleError("Dimension should be positive")

    small1, small2, long = sorted([a, b, c])
    if long >= (small1 + small2): raise TriangleError("Longest leg is too long")

    dimension_types = {
        1: 'equilateral',
        2: 'isosceles',
        3: 'scalene',
    }
    return dimension_types[len(dimensions)]

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
