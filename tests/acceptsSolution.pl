accepts(Q, [], []) :- accepting(Q).

accepts(Q, Tape, Stack) :-
    ([S | _] = Tape; S = epsilon),
    ([T | _] = Stack; T = epsilon),
    transition(Q, S, T, NewTop, NewQ),
    newTape(Tape, S, NewTape),
    newStack(Stack, T, NewTop, NewStack),
    accepts(NewQ, NewTape, NewStack).

newTape(Tape, epsilon, Tape).
newTape([F | R], F, R) :- \+ F = epsilon.

newStack(Stack, epsilon, epsilon, Stack).
newStack(Stack, epsilon, X, [X | Stack]) :- \+ X = epsilon.
newStack([X | R], X, epsilon, R):- \+ X = epsilon.
newStack([X | R], X, Y, [Y | R]) :- \+ X = epsilon, \+ Y = epsilon.
