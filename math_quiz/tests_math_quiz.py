import unittest
from math_quiz import Random_Int, Random_Operator, Perform_Operation


class TestMathGame(unittest.TestCase):

    def test_Random_Int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Random_Int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Random_Operator(self):
        #test if random operator is from the list ('+' , '-' , '*')


        for _ in range(1000):  # Test a large number of random values
            rand_opr = Random_Operator()
            self.assertTrue(rand_opr =="+" or rand_opr == "-" or rand_opr == "*")

    

    def test_Perform_Operation(self):
            #tests for different cases the function performs operations properly or not.
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (9, 5, '+', '9 + 5', 14),
                (3, 1, '*', '3 * 1', 3),
                (4, 7, '*', '4 * 7', 28),
                (4, 8, '-', '4 - 8', -4),
                (7, 6, '-', '7 - 6', 1),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                self.assertTrue((expected_problem,expected_answer) == (Perform_Operation(num1,num2,operator)))
                

if __name__ == "__main__":
    unittest.main()
