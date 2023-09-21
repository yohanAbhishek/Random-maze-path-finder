import model.dfs as dfs
import model.a_star as a_star

# This method runs the DFS algorithm once
def run_dfs():
    print("<-- DFS - >")
    dfs.executeSearch()
    print(f"Visited nodes: {dfs.getVisited()}")
    print(f"Final path: {dfs.getPath()}")
    print(f"Time: {dfs.getTime()}")


# This method runs the A* algorithm once
def run_a_star():
    print("<-- A* - >")
    a_star.executeSearch()
    print(f"Visited nodes: {a_star.getVisitedNodes()}")
    print(f"Final path: {a_star.getShortestPath()}")
    print(f"Time: {a_star.getTime()}")


# Generate 3 random mazes, and run the A* and DFS search
for i in range(3):
    print(f"\n\n-- Test run number {i+1} --\n\n")
    run_dfs()
    run_a_star()
