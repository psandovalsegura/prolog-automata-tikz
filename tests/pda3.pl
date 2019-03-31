% PDA for the language twice as many 0's as 1's in any order

accepting(qhappy).

% transition(state, tape, top of stack, new top of stack, newState).

transition(q0, epsilon, epsilon, $, q1).
transition(q1, 0, $, $, q4).
transition(q4, epsilon, epsilon, s1, q1).
transition(q1, 0, d, epsilon, q1).
transition(q1, 0, s1, s2, q1).
transition(q1, 0, s2, s2, q2).
transition(q2, epsilon, epsilon, s1, q1).
transition(q1, 1, $, $, q3).
transition(q3, epsilon, epsilon, d, q5).
transition(q5, epsilon, epsilon, d, q1).
transition(q1, 1, d, d, q3).
transition(q1, 1, s1, d, q1).
transition(q1, 1, s2, epsilon, q1).
transition(q1, epsilon, $, epsilon, qhappy).
