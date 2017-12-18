# encoding: utf-8
import heapq
import numpy as np


class Dijkstra(object):
    def __init__(self, vertices):
        self.vertices = vertices  # 邻接矩阵
        self.dist = {}  # 相聚起始点的距离
        self.unVisited = []  # 准备访问点
        self.d = np.full((len(vertices), len(vertices)), float("inf"))  # 两点之间的距离

    def init_unvisited(self, start):
        self.dist.clear()
        self.unVisited = []  # 清空历史数据
        for v in self.vertices:
            temp = Node(v)
            if temp.nodeID == start:
                temp.set_dist(0)
                self.dist[start] = 0  # 设置起始点
            heapq.heappush(self.unVisited, temp)

    def search(self, start, end):
        self.init_unvisited(start)
        while len(self.unVisited) > 0:  # 如果准备访问列表不为空
            top = heapq.heappop(self.unVisited)  # 弹出最小距离点
            if top.nodeID == end:
                return top
            neighbors = self.get_neighbors(top.nodeID)  # 获取该点邻接点
            for neighbor in neighbors:
                alt = top.dist + neighbors[neighbor]
                if neighbor in self.dist:
                    if alt < self.dist[neighbor]:
                        self.dist[neighbor] = alt
                        self.update_node(top, neighbor, alt)
                else:
                    self.dist[neighbor] = alt
                    self.update_node(top, neighbor, alt)
        return None

    def update_node(self, current, next_id, dist):
        index = 0
        for i in range(0, len(self.unVisited)):
            if self.unVisited[i].nodeID == next_id:
                self.unVisited[i].set_prev(current)
                self.unVisited[i].set_dist(dist)
                index = i
                break
        heapq._siftdown(self.unVisited, 0, index)

    def go_all(self):
        # print "maxINT:" + str(sys.maxint)
        for i in range(0, len(self.d)):
            for j in range(0, len(self.d[i])):
                temp = self.search(i, j)
                if temp is not None:
                    # print temp.dist
                    self.d[i][j] = temp.dist
                    self.d[j][i] = temp.dist

    def get_dist(self, i, j):
        if self.d[i][j] != float("inf"):
            return self.d[i][j]
        else:
            temp = self.search(i, j)
            if temp is not None:
                self.d[i][j] = temp.dist
                self.d[j][i] = temp.dist
                return temp.dist
            else:
                return float("inf")

    def get_neighbors(self, node_id):
        # 返回邻接字典
        return self.vertices[node_id]

    def print_graph(self):
        for it in self.vertices:
            print(it, self.vertices.get(it))


class Node(object):
    def __init__(self, node_id):
        self.nodeID = node_id  # ID
        self.prev = None  # 前一个节点
        self.dist = float("inf")  # 距离起始点的距离

    def __lt__(self, other):
        return self.dist < other.dist

    def __le__(self, other):
        return self.dist <= other.dist

    def __eq__(self, other):
        return self.dist == other.dist

    def __ge__(self, other):
        return self.dist >= other.dist

    def __gt__(self, other):
        return self.dist > other.dist

    def set_prev(self, prev):
        self.prev = prev

    def set_dist(self, dist):
        self.dist = dist

    def str_with_indent(self, indent):
        s1 = "<ID: {}>\n".format(self.nodeID)
        if self.prev is not None:
            s2 = "\t<prev: {}>\n".format(self.prev.str_with_indent(indent + 1))
        else:
            s2 = "<prev: None>\n"
        s3 = "<distance: {}>".format(self.dist)
        for i in range(0, indent):
            s2 = "\t" + s2
            s3 = "\t" + s3
        return s1 + s2 + s3

    def __str__(self):
        return self.str_with_indent(0)

    def __repr__(self):
        return str(self)


def get_path(node):
    out = []
    out.append(node.nodeID)
    if node.prev is not None:
        out.extend(get_path(node.prev))
    return out


def list2dict(graph):
    out = {}
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != float('inf'):
                if i not in out:
                    out[i] = {}
                out[i][j] = graph[i][j]
    return out


def dijkstra(graph, src):
    # 判断图是否为空，如果为空直接退出
    if graph is None:
        return None
    graph_dict = list2dict(graph_list)

    nodes = [i for i in range(len(graph))]
    dist_detail = []
    map = Dijkstra(graph_dict)
    map.print_graph()
    for i in nodes:
        dist_detail.append(map.search(src, i))

    distance = {}
    path = {}
    forwarding_table = {}
    for i in dist_detail:
        distance[i.nodeID] = i.dist

    for i in dist_detail:
        path[i.nodeID] = get_path(i)[::-1]

    for i in path:
        if len(path[i]) > 1:
            forwarding_table[i] = path[i][1]
        else:
            forwarding_table[i] = None

    return distance, path, forwarding_table


if __name__ == '__main__':
    graph_list = [[0, 7, float('inf'), 3, 3, 2],
                  [7, 0, 5, float('inf'), 1, 2],
                  [float('inf'), 5, 0, 6, float('inf'), 3],
                  [3, float('inf'), 6, 0, float('inf'), 1],
                  [3, 1, float('inf'), float('inf'), 0, float('inf')],
                  [2, 2, 3, 1, float('inf'), 0]]

    distance, path, forwarding_table = dijkstra(graph_list, 3)  # 查找从源点3开始到其他节点的最短路径
    print(distance)
    print(path)
    print(forwarding_table)
