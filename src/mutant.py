from data_access import get_human_count, get_mutant_count, insert_human, insert_mutant
import time

ratio = {
    "count_mutant_dna": 0,
    "count_human_dna": 0,
    "ratio": 0
}

MAX_SIZE = 6
BASES = ["A","T","C","G"]

def isSafe(i, j) -> bool:
    if( i >= 0 and i < MAX_SIZE and j >=0 and j < MAX_SIZE):
        return True
    else:
        return False
  
def moveRight(matrix, i, j, repeated):
    if repeated == 4: return True
    if isSafe(i, j+1) and matrix[i][j+1] == matrix[i][j]:
        return moveRight(matrix, i, j+1, repeated + 1)
    else:
        return False
        
def moveDownRight(matrix, i, j, repeated):
    if repeated == 4: return True
    if isSafe(i+1, j+1) and matrix[i+1][j+1] == matrix[i][j]:
        return moveDownRight(matrix, i+1, j+1, repeated + 1)
    else:
        return False
        
def moveDown(matrix, i, j, repeated):
    if repeated == 4: return True
    if isSafe(i+1, j) and matrix[i+1][j] == matrix[i][j]:
        return moveDown(matrix, i+1, j, repeated + 1)
    else:
        return False
        
def moveDownLeft(matrix, i, j, repeated):
    if repeated == 4: return True
    if (isSafe(i+1, j-1)) and (matrix[i+1][j-1] == matrix[i][j]):
        return moveDownLeft(matrix, i+1, j-1, repeated + 1)
    else:
        return False
        
def firstGen(matrix):
    for i in range(MAX_SIZE):
        for j in range(MAX_SIZE):
            if (moveRight(matrix, i, j, 1)
                or moveDownRight(matrix, i, j, 1)
                or moveDown(matrix, i, j, 1)
                or moveDownLeft(matrix, i, j, 1)):
                return secondGen(matrix, i, j+1, matrix[i][j])
    return False

def secondGen(matrix, i, j, firstBase):
    while i < MAX_SIZE:
        while j < MAX_SIZE:
            if matrix[i][j] != firstBase:
                if (moveRight(matrix, i, j, 1)
                    or moveDownRight(matrix, i, j, 1)
                    or moveDown(matrix, i, j, 1)
                    or moveDownLeft(matrix, i, j, 1)):
                    return True
            j += 1
        i += 1
        j = 0
    return False

def isMutant(data):
    if data:
        matrix = []
        global MAX_SIZE
        MAX_SIZE = len(data["dna"])
        for string in data["dna"]:
            col = []
            for letter in string:
                col.append(letter)
            matrix.append(col)
        return firstGen(matrix)
    else:
        return False

def saveMutant(json):
    insert_mutant(json)
    return True

def saveHuman(json):
    insert_human(json)
    return True

## TEST on ratio_worker cannot be tested since its a worker
def ratio_worker(): # pragma: no cover
    global ratio
    while True:
        time.sleep(5)
        ratio = calculate_adn_ratio()

## TEST on calculate_adn_ratio depends on database actual data
def calculate_adn_ratio(): # pragma: no cover
    humans = get_human_count()
    mutants = get_mutant_count()

    if humans != 0:
        json = {
            "count_mutant_dna": mutants,
            "count_human_dna": humans,
            "ratio": mutants/humans
        }
    else:
        json = {
            "count_mutant_dna": mutants,
            "count_human_dna": humans,
            "ratio": 0
        }
    return json

def get_adn_ratio():
    return ratio
