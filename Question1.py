class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        hasVisited = []
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dest = (destination[0], destination[1])

        def rollFrom(position):
            newStops = []
            for d in dirs:
                newX = position[0]
                newY = position[1]
                while (True):  # rolling
                    newPossibleX = newX + d[0]
                    newPossibleY = newY + d[1]
                    if (newPossibleX >= 0 and newPossibleX < len(maze)) and (
                            newPossibleY >= 0 and newPossibleY < len(maze[0])) and (
                            maze[newPossibleX][newPossibleY] != 1):
                        newX = newPossibleX
                        newY = newPossibleY
                        continue
                    else:
                        break
                newStop = (newX, newY)
                if newStop == dest:
                    return True
                newStops.append(newStop)

            hasVisited.append(position)

            for newStop in newStops:
                if newStop not in hasVisited:
                    if rollFrom(newStop):
                        return True
            return False

        startPos = (start[0], start[1])
        return rollFrom(startPos)


s = Solution()
print(s.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4]))
