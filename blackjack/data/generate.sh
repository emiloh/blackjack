#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution blackjack.py              # Use ../submissions/accepted/js_100.cpp to generate answer files

compile generate_random.py
compile generate_explicit.py

# Generate answers to sample cases
sample 1
sample 2


tc  random1 generate_random 1
tc  random2 generate_random 2
tc  random3 generate_random 3
tc  edge1 generate_explicit 1 "[A,Q,10]"
tc  edge2 generate_explicit 1 "[A,A,A]"
tc  edge3 generate_explicit 1 "[A,A,3]"
tc  edge4 generate_explicit 1 "[K,J,8]"
