def tsp(cities, paths, dist):
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

# don't touch below this line


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

def verify_tsp(paths, dist, actual_path):
    print(paths,dist,actual_path)
    sum = 0
    for p in range(1,len(paths)):
        sum += paths[actual_path[p-1]][actual_path[p]]
        print(paths[actual_path[p-1]][actual_path[p]])
        print(p, paths[actual_path[p-1]], paths[p], sum)
    if sum < dist:
        return True
    return False

print(tsp([0, 1, 2, 3],
        [
            [0, 988, 523, 497],
            [988, 0, 414, 940],
            [523, 414, 0, 802],
            [497, 940, 802, 0],
        ],
        1060))

print(verify_tsp([
            [0, 988, 523, 497],
            [988, 0, 414, 940],
            [523, 414, 0, 802],
            [497, 940, 802, 0],
        ],1060,
        [1, 0, 2, 3]))
