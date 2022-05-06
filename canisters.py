from graph import Graph
from dijkstras_shortest_path import dijkstras_shortest_path_algorithm


class Canisters(Graph):
    def __init__(self, first, second, target):
        self.vert_list = {}
        self.num_vertices = 0
        self.queue = []
        self.first = first
        self.second = second
        if target <= first or target <= second:
            self.target = target
        else:
            raise ValueError('both canisters smaller than the target')

    def start_and_bfs(self):
        self.add_vertex((0, 0))
        for i in [(0, self.second), (self.first, 0), (self.first, self.second)]:
            self.queue.append(i)
            self.add_edge((0, 0), i)
        while self.queue:
            temp = self.queue.pop(0)
            self.add_possible_options(temp)
            if (0, self.target) in self.queue or (self.target, 0) in self.queue:
                self.queue = []

    def add_possible_options(self, temp):
        if (0, temp[1]) not in self.vert_list.keys():
            self.add_edge(temp, (0, temp[1]))
            self.queue.append((0, temp[1]))

        if (temp[0], 0) not in self.vert_list.keys():
            self.add_edge(temp, (temp[0], 0))
            self.queue.append((temp[0], 0))

        if (temp[0], self.second) not in self.vert_list.keys():
            self.add_edge(temp, (temp[0], self.second))
            self.queue.append((temp[0], self.second))

        if (self.first, temp[1]) not in self.vert_list.keys():
            self.add_edge(temp, (self.first, temp[1]))
            self.queue.append((self.first, temp[1]))

        if temp[0] + temp[1] >= self.first:
            if (self.first, temp[1] - (self.first - temp[0])) not in self.vert_list.keys():
                self.add_edge(temp, (self.first, temp[1] - (self.first - temp[0])))
                self.queue.append((self.first, temp[1] - (self.first - temp[0])))
        else:
            if (temp[0] + temp[1], 0) not in self.vert_list.keys():
                self.add_edge(temp, (temp[0] + temp[1], 0))
                self.queue.append((temp[0] + temp[1], 0))

        if temp[0] + temp[1] >= self.second:
            if (temp[0] - (self.second - temp[1]), self.second) not in self.vert_list.keys():
                self.add_edge(temp, (temp[0] - (self.second - temp[1]), self.second))
                self.queue.append((temp[0] - (self.second - temp[1]), self.second))
        else:
            if (0, temp[0] + temp[1]) not in self.vert_list.keys():
                self.add_edge(temp, (0, temp[0] + temp[1]))
                self.queue.append((0, temp[0] + temp[1]))


def solving_problem(first, second, target):
    """
    A function for measuring a given amount of water using two canisters with different capacity.
    :argument: first - capacity of the first canister,
                second - capacity of the second canister,
                target - amount of water to be measured
    :return: a list with successive moves in the form of tuples, where:
             - tuple[0] - amount of water in first canister
             - tuple[1] - amount of water in second canister
    """
    canisters = Canisters(first, second, target)
    canisters.start_and_bfs()
    if (0, canisters.target) in dijkstras_shortest_path_algorithm(canisters, (0, 0)).keys():
        solution = dijkstras_shortest_path_algorithm(canisters, (0, 0))[(0, canisters.target)]
    elif (canisters.target, 0) in dijkstras_shortest_path_algorithm(canisters, (0, 0)).keys():
        solution = dijkstras_shortest_path_algorithm(canisters, (0, 0))[(canisters.target, 0)]
    else:
        raise ValueError('impossible to solve')
    return solution


if __name__ == '__main__':
    print(solving_problem(59, 13, 5))