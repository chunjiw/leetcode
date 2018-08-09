import wallsAndGates

if __name__ == "__main__":
  sol = wallsAndGates.Solution()
  rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
  sol.wallsAndGates(rooms)
  for room in rooms:
    print room