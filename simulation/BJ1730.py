N=int(input())
move=input()

board=[['' for i in range(N)] for j in range(N)]


D='1'
U='2'
R='3'
L='4'

row=0
col=0
for i in range(len(move)):
    if move[i]=='D' and row<N-1:
        board[row][col]+=D
        board[row+1][col]+=D
        row+=1
    elif move[i]=='U' and row>0:
        board[row][col]+=U
        board[row-1][col]+=D
        row-=1
    elif move[i]=='R' and col<N-1:
        board[row][col]+=R
        board[row][col+1]+=R
        col+=1
    elif move[i]=='L' and col>0:
        board[row][col]+=L
        board[row][col-1]+=L
        col-=1


for i in range(N):
    for j in range(N):
        if board[i][j]=='':
            board[i][j]='.'
        elif (D in board[i][j] or U in board[i][j]) and not(R in board[i][j] or L in board[i][j]):
            board[i][j]='|'
        elif not(D in board[i][j] or U in board[i][j]) and (R in board[i][j] or L in board[i][j]):
            board[i][j]='-'
        else:
            board[i][j]='+'



result=['']*N


for i in range(N):
    for j in range(N):
        result[i]+=board[i][j]
    print(result[i])
