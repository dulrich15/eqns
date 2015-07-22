#!/usr/bin/python

from sympy import latex
from sympy import solve
from sympy import symbols

from sympy import Eq
from sympy import Rational

P, V, n, R, T = symbols('P V n R T')

igl = Eq(P * V, n * R * T)

values = {
    R : 8.3144621,
    T : 273,
    P : 101300,
    n : 1
}

answers = solve(igl.subs(values),V)
answer = answers[0]

print ""
print "The ideal gas law is ",latex(igl)
print ""
print "Where the gas constant R is {} in SI units".format(values[R])
print "Standard temperature is {} Kelvin, or 0 degrees Celsius".format(values[T])
print "Standard pressure is {} pascals, or 1 atm".format(values[P])
print ""
print "So, at standard temperature and pressure, one mole of an ideal gas"
print " occupies {} cubic meters of volume".format(answer)
print ""
