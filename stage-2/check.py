"""Finite cross-checks of exact arithmetic identities, not conjecture proofs."""
import json

def step(n):
    return (3*n+1)//2 if n % 2 else n//2

def records(depth):
    # (residue, multiplier, intercept, final value at the representative)
    states = [(0, 1, 0, 0)]
    for k in range(depth):
        power = 1 << k
        next_states = []
        for a, m, b, y in states:
            for lift in (0, 1):
                z = y + m*lift
                odd = z % 2
                c = a + lift*power
                mm = 3*m if odd else m
                bb = 3*b+power if odd else b
                v = step(z)
                assert mm*c+bb == (power*2)*v
                next_states.append((c, mm, bb, v))
        states = next_states
    return states

def egyptian(n):
    if n%2 == 0:
        return (n//2, n, n)
    if n%3 == 0:
        return (n//3, 2*n, 2*n)
    if n%3 == 2:
        x = (n+1)//3
        return (x, n, n*x)
    if n%4 == 3:
        x = (n+1)//4
        return (x, 2*n*x, 2*n*x)
    return None

def main():
    depth = 14
    rows = records(depth)
    assert len({a for a, _, _, _ in rows}) == 1 << depth
    for a, m, b, y in rows:
        n = a+(1 << depth)*2
        t = n
        for _ in range(depth):
            t=step(t)
        assert t == y+2*m
        assert t*(1 << depth) == m*n+b
    tested = 0
    for n in range(2, 100_001):
        witnesses = egyptian(n)
        if witnesses is None:
            assert n % 12 == 1
            continue
        x,y,z = witnesses
        assert min(x,y,z)>0 and 4*x*y*z == n*(x*y+x*z+y*z)
        tested += 1
    print(json.dumps({"collatz_parity_depth":depth,"collatz_lifts_tested":len(rows),
                      "egyptian_witnesses_tested":tested,"upper_input":100_000,
                      "settlements":0},sort_keys=True))
if __name__ == "__main__":
    main()
