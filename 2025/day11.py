
# depth first search
def find_all_paths(graph, start, end, path=[]):
    # add current node to path
    path = path + [start]
    # end
    if start == end:
        print(path)
        return [path]
    # no start
    if start not in graph:
        return []
    # new paths
    paths = []
    for output in graph[start]:
        if output not in path:
            newpaths = find_all_paths(graph, output, end, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths

# graph/dict
devices = {}

with open("input11.txt") as f:
    for line in f.readlines():
        line = line.split()
        devices[line[0][:-1]] = line[1:]

# paths1 = find_all_paths(devices, 'you', 'out')

# PART 2

# svr -> fft
paths_fft = find_all_paths(devices, 'svr', 'fft')
print(" -> svr\n", paths_fft)

# svr -> fft/dac
paths_fft_dac = []
for path in paths_fft:
    if 'dac' not in path:
        # svr -> fft -> dac
        paths_dac = find_all_paths(devices, 'fft', 'dac', path)
        paths_fft_dac += paths_dac
    else:
        # svr -> dac -> fft
        paths_fft_dac += path
print("svr -> fft/dac\n", paths_fft_dac)

# svr -> dac&fft -> out
final_paths = []
for path in paths_fft_dac:
    if 'out' not in path:
        final_paths += find_all_paths(devices, path[-1], 'out', path)

print("svr -> dac/fft -> out\n", final_paths)
print(len(final_paths))