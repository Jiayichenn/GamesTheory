# Author: Jiayi (Jay) Chen

P = 0  # position 0-10
M = 0  # move 1, 2
V = 'W'  # value W, L, T(does not exist), Undecide
W = set([])  # 1, 2, 4, 5, 7, 8, 10
L = set([])  # 0, 3, 6, 9
U = set([])


def DoMove(p, m):
    # return the next position
    if (m != 1 and m != 2 or p < m):
        print("Bad move!")
        return p
    return p - m


def GenerateMoves(p):
    # return a list of moves
    if (p >= 3):
        return [1, 2, 3]
    if (p >= 2):
        return [1, 2]
    if (p == 1):
        return [1]
    else:
        return []  # no move


def Primitive(f_p):
    for p in range(f_p + 1):
        wining = False
        losing = True
        #np.subtract(p, listOfMoves)
        for m in GenerateMoves(p):
            next_p = DoMove(p, m)  # after enemy make his move
            if (next_p in L):
                wining = True
                break
            if (next_p not in W):
                losing = False
        if wining:
            W.add(p)
        elif losing:
            L.add(p)
    if f_p in W:
        return 'W'
    if f_p in L:
        return 'L'
    return "Undecide"


def Solve(p):
    print(Primitive(p))

Solve(15)
Solve(10)
Solve(9)
Solve(8)
Solve(7)
Solve(6)
Solve(5)
Solve(4)
Solve(3)
Solve(2)
Solve(1)
Solve(0)
