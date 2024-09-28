sudokuTable = [                                    #example sudoku(difficult)
              [0,0,6,5,0,0,0,0,0],
              [7,0,5,0,0,2,3,0,0],
              [0,3,0,0,0,0,0,8,0],
              [0,5,0,0,9,6,0,7,0],
              [1,0,4,0,0,0,0,0,8],
              [0,0,0,8,2,0,0,0,0],
              [0,2,0,0,0,0,0,9,0],
              [0,0,7,2,0,0,4,0,0],
              [0,0,0,0,0,7,5,0,0]
              ]


def solve(subo):
    find = empty_place(subo)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(subo,i,(row,col)):
            subo[row][col] = i

            if solve(subo):
                return True

            subo[row][col] = 0
    return False

def valid(subo,num,pos):
    for i in range(len(subo[0])):
        if subo[pos[0]][i] == num and pos[1] != i:
            return False

    for j in range(len(subo)):
        if subo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if subo[i][j] == num and (i,j) != pos:
                return False

    return True


def show_table(subo):            #subo : SUdoku BOard
    for i in range(len(subo)):
        if i % 3 == 0 and i !=0:
            print("- - - - - - - - - - - - - - - -")
        for j in range(len(subo[0])):
            if j % 3 == 0:
                print("|",end=" ")
            if j == 8:
                print(subo[i][j])
            else:
                print(str(subo[i][j]) + " ",end=" ")

def empty_place(subo):
    for i in range(len(subo)):
        for j in range(len(subo[0])):
            if subo[i][j] == 0:
                return (i,j)



show_table(sudokuTable)
solve(sudokuTable)
print("******************")
show_table(sudokuTable)