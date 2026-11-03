"""
Autonomous Robot Grid Pathfinding & Obstacle Avoidance Simulation
Specialization: Artificial Intelligence & Robotics
"""

import heapq

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    # Directions: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

    priority_queue = [(0 + heuristic(start, goal), 0, start, [start])]
    visited = set()

    while priority_queue:
        estimated_total, cost, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for dr, dc in moves:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                # 0 represents free space; 1 represents obstacle
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    heapq.heappush(priority_queue, (cost + 1 + heuristic((nr, nc), goal), cost + 1, (nr, nc), path + [(nr, nc)]))

    return None

if __name__ == "__main__":
    # 0 = Free space, 1 = Static Obstacle
    environment_map = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start_pos = (0, 0)
    goal_pos = (4, 4)

    print("Simulating Autonomous Navigation...")
    path = a_star_search(environment_map, start_pos, goal_pos)

    if path:
        print(f"Optimal Waypoints Found ({len(path)} steps):")
        for step, waypoint in enumerate(path):
            print(f"Step {step}: Robot moved to {waypoint}")
    else:
        print("No viable trajectory found due to obstacles.")