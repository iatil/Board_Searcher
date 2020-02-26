from random import randint
import time

def findMax(board, N, M, i, j, num, visited, curr_max=0, debug_flag=False):
  #Add new digit, log as visited
  newNum = num*10 + board[i][j]
  visited.add((i,j))

  #If new number is already smaller than current max number, cut the search
  if newNum >= 1000:
    if curr_max < newNum:
      curr_max = newNum
      #print("Returning ", newNum)
      #print(visited)

    visited.remove((i,j))
    return newNum
  elif newNum >= 100:
    if curr_max // 10 > newNum:
      #Cut the search, we are already smaller
      visited.remove((i,j))
      return 0
  elif newNum >= 10:
    if curr_max // 100 > newNum:
      #Cut the search, we are already smaller
      visited.remove((i,j))
      return 0
  else:
    if curr_max // 1000 > newNum:
      #Cut the search, we are already smaller
      visited.remove((i,j))
      return 0

  
  if debug_flag: print("State ", i, " ", j, " " , num, " " , visited)

  #Visit adjacent cells if they are not visited
  if i > 0 and (i-1,j) not in visited:
    curr_max = max(curr_max, findMax(board, N, M, i-1, j, newNum, visited, curr_max))
  if i < N - 1 and (i+1,j) not in visited:
    curr_max = max(curr_max, findMax(board, N, M, i+1, j, newNum, visited, curr_max))

  if j > 0 and (i,j-1) not in visited:
    curr_max = max(curr_max, findMax(board, N, M, i, j-1, newNum, visited, curr_max))
  if j < M-1 and (i,j+1) not in visited:
    curr_max = max(curr_max, findMax(board, N, M, i, j+1, newNum, visited, curr_max))

  visited.remove((i,j))

  return curr_max

def findNumber(board, debug_flag=False):

  N = len(board)
  M = len(board[0])

  if debug_flag: print("N:", N, " M:", M)
  if debug_flag: print("State  i   j   num   visited")

  maxNum = 0
  #Start searching at each cell, keep max
  for i in range(0,N):
    for j in range(0,M):
      if board[i][j] != 0:
        maxNum = max(maxNum, findMax(board, N, M, i, j, 0, set(), maxNum))
  
  return maxNum

def test(board, ans=0, debug_flag=False):
   
  x = findNumber(board, debug_flag)
  if debug_flag:
    print("Board")
    for row in board:
      print(row)

  print("Biggest four digit num is :", x)
  if x == ans:
    print("TEST IS OK!")
  elif ans != 0:
    print("WRONG!, SHOULD BE ", ans)

def run_tests():
  #Run correctness tests first
  debug_flag = False
  print("\n====CORRECTNESS TESTS====")
  print("\nTEST 1")
  test([[1, 2, 3, 4]], 4321, debug_flag)

  print("\nTEST 2")
  test([[1, 2, 3, 4], [5,6,7,8]], 8765, debug_flag)

  print("\nTEST 3")
  test([[9, 0, 1, 2, 4], [5,3,9,7,2], [3,8,6,0,3]], 9724, debug_flag)

  #Run performance tests
  print("\n====PERFORMANCE TESTS====")
  print("\nTEST 4 10x10 Board")
  N = 10
  M = 10
  board = [[randint(0,9) for x in range(0,N)] for y in range(0,M)] #we can also use numpy if available
  start = time.perf_counter()
  test(board, 0, debug_flag)
  end = time.perf_counter()
  print("Elapsed time (sec) ", end-start)

  print("\nTEST 5 100x100 Board")
  N = 100
  M = 100
  board = [[randint(0,9) for x in range(0,N)] for y in range(0,M)] #we can also use numpy if available
  start = time.perf_counter()
  test(board, 0, debug_flag)
  end = time.perf_counter()
  print("Elapsed time (sec) ", end-start)

  print("\nTEST 6 1000x1000 Board")
  N = 1000
  M = 1000
  board = [[randint(0,9) for x in range(0,N)] for y in range(0,M)] #we can also use numpy if available
  start = time.perf_counter()
  test(board, 0, debug_flag)
  end = time.perf_counter()
  print("Elapsed time (sec) ", end-start)

  #Average time complexity is o(N^2)

if __name__ == "__main__":
  run_tests()






