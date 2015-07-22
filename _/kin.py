#!/usr/bin/python

from sympy import latex
from sympy import solve
from sympy import symbols

from sympy import Eq
from sympy import Rational

a, d, t, v, v0 = symbols('a d t v v0')

kin1 = Eq(d, v0 * t + Rational(1,2) * a * t**2)
kin2 = Eq(v, v0 + a * t)

print ""
print "The basic equations for one-dimensional motion are:"
print ""
print "    {}".format(latex(kin1))
print "    {}".format(latex(kin2))
print ""
print "How long does it take an object released from rest to fall five meters?"
print ""

values = dict()
values[d] = -5
values[v0] = 0
values[a] = -9.81

print "The parameters for this problem are:"
print ""
for param, value in values.iteritems():
    print "    {} = {}".format(param, value)
print ""

answers = solve(kin1.subs(values),t)
if answers[0] > 0:
    answer = answers[0]
else:
    answer = answers[1]

print "Therefore the time involved is {} seconds.".format(answer)
print ""

values[t] = answer

answers = solve(kin2.subs(values),v)
answer = answers[0]

print "And its final speed is {} m/s.".format(answer)
print ""
