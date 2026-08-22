from __future__ import annotations

from sympy import Symbol, simplify

x = Symbol("x")
expr = (x + 0) - x
reduced = simplify(expr)

print("Expression:", expr)
print("Simplified:", reduced)
print("Pass:", reduced == 0)
