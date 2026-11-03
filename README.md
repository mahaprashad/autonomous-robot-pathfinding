# Autonomous Robot Pathfinding & Obstacle Navigation

## Specialization
Artificial Intelligence & Autonomous Robotics

## Overview
This project simulates an autonomous mobile robot navigating a discretized 2D environment containing static barriers and obstacles. It implements the **A* (A-Star) search algorithm** utilizing Manhattan distance heuristics to compute collision-free, minimal-cost trajectory paths from a starting dock to target coordinates.

## Features
- **Heuristic Navigation:** Calculates optimal waypoints dynamically.
- **Collision Checking:** Detects and routes around non-traversable grid cells.
- **Zero External Dependencies:** Built with native Python data structures (`heapq`) for lightweight embedded deployment.

## Installation & Execution

### Prerequisites
- Python 3.8 or higher

### Running the Simulation
1. Clone the repository:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/autonomous-robot-pathfinding.git
