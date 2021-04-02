from data_access import *
import time

ratio = {
    "count_mutant_dna": 0,
    "count_human_dna": 0,
    "ratio": 0
}

MAX_SIZE = 8
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
    if isSafe(i+1, j-1) and matrix[i+1][j-1] == matrix[i][j]:
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
                # print(i,j)
                # print(matrix[i][j])
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
                    # print(i,j)
                    # print(matrix[i][j])
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
        # print(np.matrix(matrix))         
        return firstGen(matrix)
    else:
        return False

def ratio_worker():
    global ratio
    while True:
        time.sleep(5)
        ratio = calculate_adn_ratio()

def calculate_adn_ratio():
    humans = get_human_count()
    mutants = get_mutant_count()

    if mutants != 0:
        json = {
            "count_mutant_dna": mutants,
            "count_human_dna": humans,
            "ratio": humans/mutants
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

# ratio_worker()