import unittest
from mutant import isSafe, moveRight, moveDownRight, moveDown, moveDownLeft, firstGen, secondGen, isMutant, get_adn_ratio, saveMutant, saveHuman

class TestMutant(unittest.TestCase):

    def test_isSafe_true(self):
        self.assertEqual(isSafe(5,1), True)
    def test_isSafe_false(self):
        self.assertEqual(isSafe(1,10), False)

    def test_moveRight_ture(self):
        matrix = ["AAAAGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
        self.assertEqual(moveRight(matrix, 0, 0, 1), True)
    def test_moveRight_false(self):
        matrix = ["ATCGA","ATCGA","ATCGA","ATCGA","ATCGA","ATCGA"]
        self.assertEqual(moveRight(matrix, 0, 0, 1), False)

    def test_moveDownRight_ture(self):
        matrix = ["AAAAGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
        self.assertEqual(moveDownRight(matrix, 0, 0, 1), True)
    def test_moveDownRight_false(self):
        matrix = ["AAAAAA","TTTTTT","AAAAAA","TTTTTT","AAAAAA","TTTTTT"]
        self.assertEqual(moveDownRight(matrix, 0, 0, 1), False)

    def test_moveDown_ture(self):
        matrix = ["AAAAAA","AAAAAA","AAAAAA","AAAAAA","CCCCCC","CCCCCC"]
        self.assertEqual(moveDown(matrix, 0, 0, 1), True)
    def test_moveDown_false(self):
        matrix = ["AAAAAA","TTTTTT","AAAAAA","TTTTTT","AAAAAA","TTTTTT"]
        self.assertEqual(moveDown(matrix, 0, 0, 1), False)

    def test_moveDownLeft_ture(self):
        matrix = ["CCCCCC","AAAAAA","AAAAAA","AAAAAA","AAAAAA","AAAAAA"]
        self.assertEqual(moveDownLeft(matrix, 2, 3, 1), True)
    def test_moveDownLeft_false(self):
        matrix = ["AAAAAA","TTTTTT","AAAAAA","TTTTTT","AAAAAA","TTTTTT"]
        self.assertEqual(moveDownLeft(matrix, 2, 3, 1), False)

    def test_firstGen_ture(self):
        matrix = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCTTA","TCACTG"]
        self.assertEqual(firstGen(matrix), True)
    def test_firstGen_false(self):
        matrix = ["TTTGGG","AAACCC","TTTGGG","AAACCC","TTTGGG","AAACCC"]
        self.assertEqual(firstGen(matrix), False)

    def test_secondGen_true(self):
        matrix = ["AAAAAA","TTTTTT","TTATGT","AGAAGG","CCCTTA","TCACTG"]
        self.assertEqual(firstGen(matrix), True)
    def test_secondGen_false(self):
        matrix = ["TTTTTT","AAACCC","TTTGGG","AAACCC","TTTGGG","AAACCC"]
        self.assertEqual(firstGen(matrix), False)

    def test_isMutant_true(self):
        data = {"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCTTA","TCACTG"]}
        self.assertEqual(isMutant(data), True)
    def test_isMutant_false(self):
        data = {"dna":["TTGCGA","CAGTGC","TTATGT","AGAAGG","CCCTTA","TCACTG"]}
        self.assertEqual(isMutant(data), False)
    def test_isMutant_false_null(self):
        self.assertEqual(isMutant({}), False)
    
    def test_get_adn_ratio(self):
        self.assertEqual(get_adn_ratio(), {
            "count_mutant_dna": 0,
            "count_human_dna": 0,
            "ratio": 0
        })

    def test_saveMutant(self):
        self.assertEqual(saveMutant({"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCTTA","TCACTG"]}), True)

    def test_saveHuman(self):
        self.assertEqual(saveHuman({"dna":["TTGCGA","CAGTGC","TTATGT","AGAAGG","CCCTTA","TCACTG"]}), True)


    ## TEST on calculate_adn_ratio depends on database actual data
    ## TEST on ratio_worker cannot be tested since its a worker
