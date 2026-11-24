"""Bounded checks for the stage-1 hypotheses; not a proof of Collatz."""
import json

def step(n):
    return n // 2 if n % 2 == 0 else 3*n+1

def prefix(n, count):
    out = [n]
    for _ in range(count):
        out.append(step(out[-1]))
    return out

def main():
    for q in range(1, 4097):
        assert prefix(4*q+1, 3)[-1] == 3*q+1 < 4*q+1
    for k in range(1, 513):
        n = 2**(k+1)-1
        path = prefix(n, 2*k)
        assert min(path[1:]) > n
        assert path[::2] == [3**j*2**(k+1-j)-1 for j in range(k+1)]
    witness = prefix(27, 20)
    assert min(witness[1:]) > 27
    print(json.dumps({"odd_residue_examples":4096,"obstruction_family_max_k":512,
                      "twenty_step_witness":witness,"universal_conjecture_verified":False}))

if __name__ == "__main__":
    main()
