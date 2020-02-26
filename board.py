from random import randint
import time

def findMax(board, N, M, i, j, num, visited):

  global curr_max
  global debug_flag

  myMax = 0
  newNum = num*10 + board[i][j]
  visited.add((i,j))

  if newNum >= 1000:
    if curr_max < newNum:
      curr_max = newNum
      #print("Returning ", newNum)
      #print(visited)

    visited.remove((i,j))
    return newNum

  
  if debug_flag: print("State ", i, " ", j, " " , num, " " , visited)

  #Visit adjacent cells
  if i > 0 and (i-1,j) not in visited:
    myMax = max(myMax, findMax(board, N, M, i-1, j, newNum, visited))
  if i < N - 1 and (i+1,j) not in visited:
    myMax = max(myMax, findMax(board, N, M, i+1, j, newNum, visited))

  if j > 0 and (i,j-1) not in visited:
    myMax = max(myMax, findMax(board, N, M, i, j-1, newNum, visited))
  if j < M-1 and (i,j+1) not in visited:
    myMax = max(myMax, findMax(board, N, M, i, j+1, newNum, visited))

  visited.remove((i,j))

  return myMax

def findNumber(board):
  N = len(board)
  M = len(board[0])

  if debug_flag: print("N:", N, " M:", M)
  if debug_flag: print("State  i   j   num   visited")

  maxNum = 0

  for i in range(0,N):
    for j in range(0,M):
      if board[i][j] != 0:
        maxNum = max(maxNum, findMax(board, N, M, i, j, 0, set()))
  
  return maxNum

def test(board, ans=0):
  x = findNumber(board)

  if debug_flag:
    print("Board")
    for row in board:
      print(row)

  print("Biggest four digit num is :", x)
  if x == ans:
    print("TEST IS OK!")
  elif ans != 0:
    print("WRONG!, SHOULD BE ", ans)


if __name__ == "__main__":

  debug_flag = False
  curr_max = 0
  #print("\nTEST 1")
  #test([[1, 2, 3, 4]], 4321)

  #print("\nTEST 2")
  #test([[1, 2, 3, 4], [5,6,7,8]], 8765)

  #print("\nTEST 3")
  #test([[9, 0, 1, 2, 4], [5,3,9,7,2], [3,8,6,0,3]], 9724)

  print("\nTEST 4 10x10")
  N = 10
  M = 10
  board = [[randint(0,9) for x in range(0,N)] for y in range(0,M)]
  start = time.perf_counter()
  test(board, 0)
  end = time.perf_counter()
  print("Elapsed time (sec) ", end-start)

  print("\nTEST 5 100x100")
  N = 100
  M = 100
  board = [[randint(0,9) for x in range(0,N)] for y in range(0,M)]
  start = time.perf_counter()
  test(board, 0)
  end = time.perf_counter()
  print("Elapsed time (sec) ", end-start)

  print("\nTEST 6 1000x1000")
  N = 1000
  M = 1000
  board = [[randint(0,9) for x in range(0,N)] for y in range(0,M)]
  start = time.perf_counter()
  test(board, 0)
  end = time.perf_counter()
  print("Elapsed time (sec) ", end-start)







