bfs([Goal|_],Goal,[Goal]).
bfs([Node|Rest],Goal,[Node|Path]):-
    findall(X,edge(Node,X),Neighbors),
    append(Rest,Neighbors,Queue),
    bfs(Queue,Goal,Path).
edge(a,b).
edge(a,c).
edge(b,d).
edge(c,d).
edge(c,e).

