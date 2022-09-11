def countComponents(n, edges):

    parents = [i for i in range(n)]
    rank = [1] * n

    # find function finds a node
    def find(n1):
        res = n1
        while res != parents[res]:
            parents[res] = parents[parents[res]]
            res = parents[res]
        return res

    # union function merges a node and a subsection
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            # there is no union to be made
            return 0

        if rank[p2] > rank[p1]:
            parents[p1] = p2
            rank[p2] += rank[p1]
        else:
            parents[p2] = p1
            rank[p1] += rank[p2]
        return 1

    res = n
    for n1, n2 in edges:
        res -= union(n1,n2)
    return res