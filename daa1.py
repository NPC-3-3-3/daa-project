import pygame
import random
from collections import deque

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graph Traversal Visualizer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)

# Node and Edge settings
NODE_RADIUS = 20
EDGE_WIDTH = 2

# Fonts
FONT = pygame.font.SysFont("comicsans", 20)

# Graph class
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.visited = set()

    def add_node(self, x, y):
        self.nodes.append((x, y))
        self.edges[(x, y)] = []

    def add_edge(self, node1, node2):
        self.edges[node1].append(node2)
        self.edges[node2].append(node1)

    def draw(self):
        # Draw edges
        for node, neighbors in self.edges.items():
            for neighbor in neighbors:
                pygame.draw.line(screen, GRAY, node, neighbor, EDGE_WIDTH)

        # Draw nodes
        for node in self.nodes:
            color = GREEN if node in self.visited else BLUE
            pygame.draw.circle(screen, color, node, NODE_RADIUS)
            pygame.draw.circle(screen, BLACK, node, NODE_RADIUS, 2)

    def bfs(self, start_node):
        queue = deque([start_node])
        self.visited = set()
        self.visited.add(start_node)

        while queue:
            current = queue.popleft()
            self.draw()
            pygame.display.update()
            pygame.time.delay(500)

            for neighbor in self.edges[current]:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start_node):
        stack = [start_node]
        self.visited = set()
        self.visited.add(start_node)

        while stack:
            current = stack.pop()
            self.draw()
            pygame.display.update()
            pygame.time.delay(500)

            for neighbor in self.edges[current]:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    stack.append(neighbor)

# Main function
def main():
    running = True
    graph = Graph()
    selected_node = None
    mode = "add_node"  # Modes: add_node, add_edge, bfs, dfs

    while running:
        screen.fill(WHITE)

        # Display instructions
        instructions = FONT.render(
            "Modes: 1-Add Node | 2-Add Edge | 3-BFS | 4-DFS | R-Reset", True, BLACK
        )
        screen.blit(instructions, (10, 10))

        # Draw graph
        graph.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "add_node"
                elif event.key == pygame.K_2:
                    mode = "add_edge"
                elif event.key == pygame.K_3:
                    mode = "bfs"
                elif event.key == pygame.K_4:
                    mode = "dfs"
                elif event.key == pygame.K_r:
                    graph = Graph()
                    selected_node = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if mode == "add_node":
                    graph.add_node(x, y)

                elif mode == "add_edge":
                    for node in graph.nodes:
                        if (x - node[0]) ** 2 + (y - node[1]) ** 2 <= NODE_RADIUS ** 2:
                            if selected_node is None:
                                selected_node = node
                            else:
                                graph.add_edge(selected_node, node)
                                selected_node = None
                            break

                elif mode == "bfs":
                    for node in graph.nodes:
                        if (x - node[0]) ** 2 + (y - node[1]) ** 2 <= NODE_RADIUS ** 2:
                            graph.bfs(node)
                            break

                elif mode == "dfs":
                    for node in graph.nodes:
                        if (x - node[0]) ** 2 + (y - node[1]) ** 2 <= NODE_RADIUS ** 2:
                            graph.dfs(node)
                            break

    pygame.quit()

if __name__ == "__main__":
    main()