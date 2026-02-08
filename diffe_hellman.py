alpha = 5
q = 7

xa = 13
xb = 11

ya = pow(alpha, xa) % q
yb = pow(alpha, xb) % q

ka = pow(yb, xa) % q
kb = pow(ya, xb) % q

print(ka, kb)
