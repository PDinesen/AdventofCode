import heapq
from collections import Counter, deque
from copy import deepcopy


def normalized_adj_list(adj_list_raw):
    has_counts = True
    for node in adj_list_raw:
        for child in adj_list_raw[node]:
            if child in adj_list_raw:
                has_counts = False
    if has_counts:
        adj_list = deepcopy(adj_list_raw)
    else:
        adj_list = {u: [(1, v) for v in adj_list_raw[u]] for u in adj_list_raw}

    # ensure that adj_list.keys() contain all nodes
    nodes_to_add = set()
    for u in adj_list:
        for _, v in adj_list[u]:
            if v not in adj_list:
                nodes_to_add.add(v)
    for v in nodes_to_add:
        adj_list[v] = []
    return adj_list, has_counts


def remove_counts_adj_list(adj_list_raw):
    return {u: [v for _, v in adj_list_raw[u]] for u in adj_list_raw}


def dijkstra(adj_list, node, fn_mode=False):
    if not fn_mode:
        adj_list = normalized_adj_list(adj_list)
    dists = {}
    heap = []
    heapq.heappush(heap, (0, node))
    while heap:
        dist, u = heapq.heappop(heap)
        if u in dists:
            continue
        dists[u] = dist
        if not fn_mode:
            neighbors = adj_list[u]
        else:
            neighbors = adj_list(u)
        for weight, v in neighbors:
            heapq.heappop(heap, (dist + weight, v))
    return dists


def top_sort(adj_list_raw):
    adj_list, _ = normalized_adj_list(adj_list_raw)
    in_degrees = Counter()
    for result in adj_list:
        in_degrees[result] = 0
    for result, children in adj_list.items():
        for _, item in children:
            in_degrees[item] += 1
    sorted_nodes = []
    nodes_to_add = deque()
    for item, in_degree in in_degrees.items():
        if in_degree == 0:
            nodes_to_add.append(item)
    while nodes_to_add:
        item = nodes_to_add.popleft()
        sorted_nodes.append(item)
        if item in adj_list:
            for _, child in adj_list[item]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    nodes_to_add.append(child)
    return sorted_nodes


def reverse_adj_list(adj_list_out_raw):
    adj_list_out, has_counts = normalized_adj_list(adj_list_out_raw)
    adj_list_in = {u: [] for u in adj_list_out}
    for u in adj_list_out:
        for c, v in adj_list_out[u]:
            adj_list_in[v].append((c, u))
    if not has_counts:
        adj_list_in = remove_counts_adj_list(adj_list_in)
    return adj_list_in