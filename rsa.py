import math

# Hard-coded primes
p = 61
q = 53

# Step 1: Compute n and φ(n)
n = p * q
phi = (p - 1) * (q - 1)

# Step 2: Choose e (1 < e < phi, gcd(e, phi) = 1)
e = 17
assert math.gcd(e, phi) == 1

# Step 3: Compute d (modular inverse of e mod φ)
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

d = mod_inverse(e, phi)

# Output keys
print("Public Key  (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
