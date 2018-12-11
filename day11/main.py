class FuelMatrixParser:
    def getTopLeftCellCoordWithHigherSum(self, matrix, squareSize = 3):
        hi = {'coordinates': (0, 0), 'sum': 0}
        rows = matrix.rows

        for i in range(matrix.size):
            for j in range(matrix.size):
                if not self.__cellExist(i + squareSize, j, rows) or not self.__cellExist(i, j + squareSize, rows):
                    continue
                
                currentSum = 0
                for a in range(i, i + squareSize + 1):
                    for b in range(j, j + squareSize + 1):
                        currentSum += rows[a][b]

                if currentSum > hi['sum']:
                    hi['coordinates'] = (j + 1, i + 1)
                    hi['sum'] = currentSum

        return hi['coordinates']

    
    def __cellExist(self, i, j, matrix):
        try:
            matrix[i][j]
            return True
        except:
            return False

class FuelMatrix:
    def __init__(self, serialNumber, size = 300):
        self.rows = self.__generate(serialNumber, size)
        self.size = size
    
    def __generate(self, serialNumber, size):
        initial = [[0]* size for i in range(size)]
        for i in range(size):
            for j in range(size):
                initial[i][j] = self.__computeCellPower(i, j, serialNumber)
        
        return initial

    def __computeCellPower(self, i, j, serialNumber):
        x = j + 1
        y = i + 1

        rackId = x + 10
        tmp = ((rackId * y) + serialNumber) * rackId
        tmp = str(tmp)

        return int(tmp[-3]) - 5


def main():
    fuelMatrix = FuelMatrix(42)
    parser = FuelMatrixParser()

    print(parser.getTopLeftCellCoordWithHigherSum(fuelMatrix))

main()