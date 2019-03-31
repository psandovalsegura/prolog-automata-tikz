#
# Script to convert prolog automata to tikz code
#

import argparse
import re

BOILERPLATE_start = "% Author: Till Tantau\n \
% Source: The PGF/TikZ manual\n \
\\documentclass{article}\n \
\\usepackage{pgf}\n \
\\usepackage{tikz}\n \
\\usetikzlibrary{arrows,automata}\n \
\\usepackage[latin1]{inputenc}\n \
\\begin{document}\n \
\\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=2.8cm, semithick]\n \
    \\tikzstyle{every state}=[fill=red,draw=none,text=white]\n \
    \\node[initial,state] (A0)                    {$q_0$};\n"

BOILERPLATE_end = "\\end{tikzpicture}\n \
\\end{document}"

accept_re = r"accepting\((\w*)\)."
transition_re = r"transition\((\w*), (\w*), (\w*)\)."

STATES = [] # Strings
EDGES = []  # Tuples 
STATES_TO_TIKZSTATE = {}

def insertState(statename):
    if statename not in STATES:
        STATES.append(statename)

def getStatesAndTransitions(f):
    for line in f.readlines():
        matched_accept = re.match(accept_re, line)
        if matched_accept:
            groups = matched_accept.groups()
            state = groups[0]
            insertState(state)

        matched_transition = re.match(transition_re, line)
        if matched_transition:
            groups = matched_transition.groups()
            state1, symbol, state2 = groups
            insertState(state1)
            insertState(state2)
            EDGES.append((state1, symbol, state2))

    # Remove q0 state (always assumed to be the start state)
    STATES.remove("q0")
    STATES_TO_TIKZSTATE["q0"] = "A0"

def getTikzNodeCode():
    c = ""
    for i, state in enumerate(STATES):
        tikz_state = f"A{i+1}"
        if i == 0:
            c += f"\\node[state]         ({tikz_state})[right of=A0] {{${state}$}};\n"
        else:
            c += f"\\node[state]         ({tikz_state})[right of=A{i}] {{${state}$}};\n"
    return c

def main():
    parser = argparse.ArgumentParser(description='Convert prolog code to tikz')
    parser.add_argument('prolog_file', type=argparse.FileType('r'),
                                       help='Prolog file with automata definition')
    parser.add_argument('output_filename', help='Output filename')
    args = parser.parse_args()

    getStatesAndTransitions(args.prolog_file)
    print(STATES)

    tikzNodeCode = getTikzNodeCode()

    print(tikzNodeCode)

    with open(args.output_filename, "w") as f:
        print(BOILERPLATE_start + tikzNodeCode + BOILERPLATE_end, file=f)

if __name__ == '__main__':
    main()