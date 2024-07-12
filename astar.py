from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def astar(fillmatrix:list[list], start_pos:tuple[int,int], end_pos:tuple[int,int]):

    grid = Grid(matrix=fillmatrix)
    start_node = grid.node(start_pos[0], start_pos[1]) if start_pos else None
    if start_pos and end_pos:
        end_node = grid.node(end_pos[0], end_pos[1]) if end_pos else None
        finder = AStarFinder(diagonal_movement=4)
        path, _ = finder.find_path(start_node, end_node, grid)
        return path
def pathtoarrofblocks(path:list[Grid.node]):
    return [(node.x, node.y) for node in path]
