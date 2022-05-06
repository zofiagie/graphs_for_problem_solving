from graph import Graph
from dijkstras_shortest_path import dijkstras_shortest_path_algorithm


class MissionariesAndCannibals(Graph):
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0
        self.queue = []

    def start_and_bfs(self):
        self.add_vertex((3, 3, 1))
        self.queue.append((3, 3, 1))
        while self.queue:
            temp = self.queue.pop(0)
            self.add_possible_options(temp)
            if (0, 0, 0) in self.queue:                 # when a solution is found
                self.queue = []

    def add_possible_options(self, temp):
        if temp[2] == 1:                                        # boat on the left side of the river
            if (temp[0] - 1) >= 0 and (temp[1] - 1) >= 0:       # the missionary and the cannibal cross a river
                if temp[0] - 1 >= temp[1] - 1 or temp[0] - 1 == 0:
                    if 3 - (temp[0] - 1) >= 3 - (temp[1] - 1) or 3 - (temp[0] - 1) == 0:
                        if (temp[0] - 1, temp[1] - 1, 0) not in self.vert_list.keys():
                            self.add_edge(temp, (temp[0] - 1, temp[1] - 1, 0))
                            self.queue.append((temp[0] - 1, temp[1] - 1, 0))

            if (temp[0] - 2) >= 0:                             # two missionaries cross a river
                if temp[0] - 2 >= temp[1] or temp[0] - 2 == 0:
                    if 3 - (temp[0] - 2) >= 3 - temp[1] or 3 - (temp[0] - 2) == 0:
                        if (temp[0] - 2, temp[1], 0) not in self.vert_list.keys():
                            self.add_edge(temp, (temp[0] - 2, temp[1], 0))
                            self.queue.append((temp[0] - 2, temp[1], 0))

            if (temp[1] - 2) >= 0:                            # two cannibals cross a river
                if temp[0] >= temp[1] - 2 or temp[0] == 0:
                    if 3 - temp[0] >= 3 - (temp[1] - 2) or 3 - temp[0] == 0:
                        if (temp[0], temp[1] - 2, 0) not in self.vert_list.keys():
                            self.add_edge(temp, (temp[0], temp[1] - 2, 0))
                            self.queue.append((temp[0], temp[1] - 2, 0))

            if (temp[0] - 1) >= 0:                            # the missionary crosses a river
                if temp[0] - 1 >= temp[1] or temp[0] - 1 == 0:
                    if 3 - (temp[0] - 1) >= 3 - temp[1] or 3 - (temp[0] - 1) == 0:
                        if (temp[0] - 1, temp[1], 0) not in self.vert_list.keys():
                            self.add_edge(temp, (temp[0] - 1, temp[1], 0))
                            self.queue.append((temp[0] - 1, temp[1], 0))

            if (temp[1] - 1) >= 0:                            # the cannibal crosses a river
                if temp[0] >= temp[1] - 1 or temp[0] == 0:
                    if 3 - temp[0] >= 3 - (temp[1] - 1) or 3 - temp[0] == 0:
                        if (temp[0], temp[1] - 1, 0) not in self.vert_list.keys():
                            self.add_edge(temp, (temp[0], temp[1] - 1, 0))
                            self.queue.append((temp[0], temp[1] - 1, 0))

        else:                                                # boat on the right side of the river
            if (temp[0] + 1) <= 3 and (temp[1] + 1) <= 3:    # the missionary and the cannibal cross a river
                if temp[0] + 1 >= temp[1] + 1:
                    if 3 - (temp[0] + 1) >= 3 - (temp[1] + 1) or 3 - (temp[0] + 1) == 0:
                        if (temp[0] + 1, temp[1] + 1, 1) not in self.vert_list.keys():
                            self.add_edge(temp, (temp[0] + 1, temp[1] + 1, 1))
                            self.queue.append((temp[0] + 1, temp[1] + 1, 1))

            if (temp[0] + 2) <= 3:                             # two missionaries cross a river
                if temp[0] + 2 >= temp[1]:
                    if 3 - (temp[0] + 2) >= 3 - temp[1] or 3 - (temp[0] + 2) == 0:
                        if (temp[0] + 2, temp[1], 1) not in self.vert_list.keys():
                            self.add_edge(temp, (temp[0] + 2, temp[1], 1))
                            self.queue.append((temp[0] + 2, temp[1], 1))

            if (temp[1] + 2) <= 3:                            # two cannibals cross a river
                if temp[0] >= temp[1] + 2 or temp[0] == 0:
                    if 3 - temp[0] >= 3 - (temp[1] + 2) or 3 - temp[0] == 0:
                        if (temp[0], temp[1] + 2, 1) not in self.vert_list.keys():
                            self.add_edge(temp, (temp[0], temp[1] + 2, 1))
                            self.queue.append((temp[0], temp[1] + 2, 1))

            if (temp[0] + 1) <= 3:                            # the missionary crosses a river
                if temp[0] + 1 >= temp[1]:
                    if 3 - (temp[0] + 1) >= 3 - temp[1] or 3 - (temp[0] + 1) == 0:
                        if (temp[0] + 1, temp[1], 1) not in self.vert_list.keys():
                            self.add_edge(temp, (temp[0] + 1, temp[1], 1))
                            self.queue.append((temp[0] + 1, temp[1], 1))

            if (temp[1] + 1) <= 3:                            # the cannibal crosses a river
                if temp[0] >= temp[1] + 1 or temp[0] == 0:
                    if 3 - temp[0] >= 3 - (temp[1] + 1) or 3 - temp[0] == 0:
                        if (temp[0], temp[1] + 1, 1) not in self.vert_list.keys():
                            self.add_edge(temp, (temp[0], temp[1] + 1, 1))
                            self.queue.append((temp[0], temp[1] + 1, 1))


def solving_problem():
    """
    A function that solves the problem of missionaries and cannibals
    :return: a list with successive moves in the form of tuples, where:
             - tuple[0] - number of missionaries on the left side of the river
             - tuple[1] - number of cannibals on the left side of the river
             - tuple[2] - the side of the river on which the boat is located (1-left, 0-right)
    """
    missionaries_and_cannibals = MissionariesAndCannibals()
    missionaries_and_cannibals.start_and_bfs()
    if (0, 0, 0) in dijkstras_shortest_path_algorithm(missionaries_and_cannibals, (3, 3, 1)).keys():
        solution = dijkstras_shortest_path_algorithm(missionaries_and_cannibals, (3, 3, 1))[(0, 0, 0)]
    else:
        raise ValueError('impossible to solve')
    return solution


if __name__ == '__main__':
    print(solving_problem())