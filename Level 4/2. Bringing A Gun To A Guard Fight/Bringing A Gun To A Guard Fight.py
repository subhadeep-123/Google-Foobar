import math


def mirror_atlas(node, dimensions, distance):
    node_mirrored = []
    for i in range(len(node)):
        points = []
        for j in range(-(distance//dimensions[i])-1, (distance//dimensions[i]+2)):
            points.append(get_mirror(j, node[i], dimensions[i]))
        node_mirrored.append(points)
    return node_mirrored


def get_mirror(mirror, coordinates, dimensions):
    res = coordinates
    mirror_rotation = [2*coordinates, 2*(dimensions-coordinates)]
    if(mirror < 0):
        for i in range(mirror, 0):
            res -= mirror_rotation[(i+1) % 2]
    else:
        for i in range(mirror, 0, -1):
            res += mirror_rotation[i % 2]
    return res


def solution(dimensions, your_position, guard_position, distance):
    mirrored = [mirror_atlas(your_position, dimensions,
                             distance), mirror_atlas(guard_position, dimensions, distance)]
    res = set()
    angles_dist = {}
    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                beam = math.atan2((your_position[1]-k), (your_position[0]-j))
                l = math.sqrt((your_position[0]-j)
                              ** 2 + (your_position[1]-k)**2)
                if [j, k] != your_position and distance >= l:
                    if((beam in angles_dist and angles_dist[beam] > l) or beam not in angles_dist):
                        if i == 0:
                            angles_dist[beam] = l
                        else:
                            angles_dist[beam] = l
                            res.add(beam)
    return len(res)


# _-_-_-_-_-_-_-_-_-_-_-_-TEST--CASES-_-_-_-_-_-_-_-_-_-_-_-_
if __name__ == "__main__":
    tests = [
        [
            [3, 2],
            [1, 1],
            [2, 1],
            400
        ],
    ]

    results = [0 for x in range(len(tests))]
    answers = [6, 16, 935, 2789, 2000000000, 23, 256, 141031256]
    timingsSum = [0 for x in range(len(tests))]
    testRuns = 10

    for j in range(1, testRuns + 1):
        print("Testing round: " + str(j))
        for i in range(len(tests)):
            results[i] = solution(tests[i][0], tests[i][1],
                                  tests[i][2], tests[i][3])

    for i, t in enumerate(timingsSum):
        print("Test " + str(i + 1) + " runtime: " + str(t/testRuns))
