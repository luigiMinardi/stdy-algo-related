def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

def tsp_lane(cities, paths, dist):
    perms = permutations(cities)
    for perm in perms:
        total_dist = 0
        for i in range(1, len(perm)):
            total_dist += paths[perm[i - 1]][perm[i]]
        if total_dist < dist:
            return True
    return False

def tsp_mine(cities, paths, dist):
    all_paths = [permutations(p) for p in paths]
    for p in all_paths:
        sum = 0
        for v in p:
            if sum > dist:
                continue
            sum = 0
            for i in range(len(v)):
                sum += v[i]
            print(sum)
            if sum < dist:
                return True
    return False

