N=int(input())
board=[]
for i in range(N):
    board.append(list(input()))


def count():
    max_row=-100000000
    row=1
    max_col=-100000000
    col=1
    length=0
    for i in range(N):
        row=1
        col=1
        for j in range(N-1):
            if board[i][j]==board[i][j+1]:
                row+=1
                max_row=max(max_row,row)
            else:
                row=1

            
            if board[j][i]==board[j+1][i]:
                col+=1
                max_col=max(max_col, col)
            else:
                col=1
        if row==N:
            max_row=row

        if col==N:
            max_col=col
   
    length=max(max_col,max_row)
    return length


rlength=0
max_rlength=-100000000
clength=0
max_clength=-100000000
for i in range(N):
    for j in range(N-1):
        if board[i][j]!=board[i][j+1]:
            board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
            rlength=count()
            max_rlength=max(max_rlength,rlength)
            board[i][j],board[i][j+1]=board[i][j+1],board[i][j]

        if board[j][i]!=board[j+1][i]:
            board[j][i],board[j+1][i]=board[j+1][i],board[j][i]
            clength=count()
            max_clength=max(max_clength,clength)
            board[j][i],board[j+1][i]=board[j+1][i],board[j][i]

print(max(max_rlength,max_clength))