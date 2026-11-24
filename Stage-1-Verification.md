# Stage 1 verification status: not settled

The executable finite evidence passed under Python 3 (run `python3 check_collatz.py`; compare to stage-1-evidence.json). No complete Lean check or axiom audit succeeded. The packaged WASM runner timed out importing Init across several bounded trials; the official native download did not connect in this environment. The .lean file is an unchecked draft. The paper argument for the obstruction is in the checkpoint; the draft checks a finite instance of it, not yet the general obstruction. Do not present this as a Lean-verified proof.

Next independent verification action: use an official pinned Lean 4 distribution and run `lean CollatzStage1.lean` in a clean directory with no LEAN_PATH overrides. Fix any elaboration failures; capture exit status, lean --version and both #print axioms reports. A successful auxiliary check still leaves the Collatz claim open. Set up the exact-statement certificate checker and enumerate both polarities only once certificate construction and axiom audit are grounded.

SHA-256:
ceea15fd800ba18fec74b77e55d56905ecd0137013e8f93e84879ac20226c746  CollatzStage1.lean
63d350556f84e38600418119e7071acf748c062c1bdabed6539729ba0c9eb023  check_collatz.py
c7bcce899c8cd3a49948af9f88cdbd326c1bb59c863b09e5dc12cb3afa51dbfb  stage-1-evidence.json
