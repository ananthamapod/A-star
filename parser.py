def readMazeFromFile(filename, delimiter):
	data = []

	with open(filename, 'r') as f:
		data = [
			[c for c in r[0]]
			for r in
			filter(
				lambda x: len(x) != 0,
				map(
					lambda x: x.split(delimiter),
					f.read().split('\n')
				)
			)
		]

	return len(data), len(data[0]), data

if __name__ == '__main__':
    a = readDataFromFile('maze.txt', None)
    print len(a)
    for i in a:
        print i
