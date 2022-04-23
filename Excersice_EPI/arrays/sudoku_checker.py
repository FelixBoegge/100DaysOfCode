def check_sudoku(A):
    def has_dulicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))
    dim = len(A)
    if any(has_dulicate([A[i][j] for j in range(dim)]) or has_dulicate([A[j][i] for j in range(dim)]) for i in range(dim)):
        return False
    region_size = int(dim**(1/2))
    return all(not has_dulicate([
        A[a][b]
        for a in range(region_size * I, region_size * (I+1))
        for b in range(region_size * J, region_size * (J+1))
    ]) for I in range(region_size) for J in range(region_size))


A = [[5,3,0,0,7,0,0,0,0], [6,0,0,1,9,5,0,0,0], [0,9,8,0,0,0,0,6,0], [8,0,0,0,6,0,0,0,3], [4,0,0,8,0,3,0,0,1], [7,0,0,0,2,0,0,0,6], [0,6,0,0,0,0,2,8,0], [0,0,0,4,1,9,0,0,5], [0,0,0,0,8,0,0,7,9]]
print(check_sudoku(A))


 #  dim = len(A)
 #   row_sets = [[0] for i in range(dim)]
#    col_sets = [[0] for i in range(dim)]
   # sub_sets = [[0] for i in range(dim)]
  #  for i in range(len(A)):
 #       for j in range(len(A[i])):
#            if A[i][j] != 0:
         #       if A[i][j] in row_sets[i]:
        #            return "invalid"
       #         else:
      #              row_sets[i].append(A[i][j])
     #           if A[i][j] in col_sets[j]:
    #                return "invalid"
   #             else:
  #                  col_sets[j].append(A[i][j])
 #               if A[i][j] in sub_sets[(i//3)*(j//3)]
#    return "valid"
