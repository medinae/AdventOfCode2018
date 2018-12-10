import time

class Transitions:
    def __init__(self, points):
        self.points = points
        self.count = len(points)
    
    def next(self):
        for point in self.points:
            point.move()

class Point:
    def __init__(self, posX, posY, velX, velY):
        self.posX = posX
        self.posY = posY
        self.velX = velX
        self.velY = velY
    
    def move(self):
        self.posX += self.velX
        self.posY += self.velY

def getTransitionsFromFile(fileName):
    points = []

    with open(fileName) as f:
        for line in f:
            lineContent = line.strip()
            exploded = lineContent.replace("<", ",").replace(">", ",").split(",")
            points.append(Point(
                int(exploded[1]),
                int(exploded[2]),
                int(exploded[4]),
                int(exploded[5])
            ))
    
    return Transitions(points)

def getStatsFromTransitions(transitions):
    minY = maxY = minX = maxX = 0
    starsIndexPairs = {}

    for point in transitions.points:
        if minY > point.posY:
            minY = point.posY
        if maxY < point.posY:
            maxY = point.posY
        if minX > point.posX:
            minX = point.posX
        if maxX < point.posX:
            maxX = point.posX  

        starsIndexPairs[(point.posX, point.posY)] = True
    
    return {'minY': minY, 'maxY': maxY, 'minX': minX, 'maxX': maxX, 'starsCoordinates': starsIndexPairs}

def main():
    transitions = getTransitionsFromFile('day10/input_test.txt')
    c = 0
    transitionEvolutionLimit = 6

    while c <= transitionEvolutionLimit :
        time.sleep(1)
        c += 1

        stats = getStatsFromTransitions(transitions)
        minY = stats['minY']
        minX = stats['minX']
        maxY = stats['maxY']
        maxX = stats['maxX']
        starsCoordinates = stats['starsCoordinates']

        for y in range(minY, maxY + 1):
            for x in range(minX, maxX + 1):
                if (x,y) in starsCoordinates:
                    print('#', end='')
                else:
                    print('.', end='')
        
            print('')
        
        transitions.next()
        
        print('')

main()