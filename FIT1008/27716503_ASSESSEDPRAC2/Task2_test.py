import unittest
from Task2_AssPrac import ArrayBasedList

class testFunction(unittest.TestCase):
    def test__str__(self):
        testCase = ArrayBasedList(10)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        self.assertEqual(testCase.__str__(), "3\n4\n5\n6\n")
        self.assertNotEqual(testCase.__str__(),"3\n4\n6\n")

    def test__len__(self):
        testCase = ArrayBasedList(10)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        self.assertEqual(testCase.__len__(), 4)
        self.assertNotEqual(testCase.__len__(),3)

    def test_append(self):
        testCase = ArrayBasedList(10)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        self.assertEqual(testCase.__str__(), "3\n4\n5\n6\n")
        self.assertNotEqual(testCase.__str__(), "3\n4\n6\n")

    def test_increaseSize(self):
        testCase = ArrayBasedList(4)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        testCase.append(7)
        self.assertEqual(testCase.__len__(), 5)
        self.assertNotEqual(testCase.__len__(), 6)

    def test_isFull(self):
        testCase = ArrayBasedList(4)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        self.assertEqual(testCase.isFull(), True)
        self.assertNotEqual(testCase.isFull(), False)

    def test__contains__(self):
        testCase = ArrayBasedList(10)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        self.assertEqual(testCase.__contains__(3), True)
        self.assertEqual(testCase.__contains__(7), False)

    def test_getitem__(self):
        testCase = ArrayBasedList(10)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        self.assertEqual(testCase.__getitem__(3), 6)
        self.assertRaises(IndexError,testCase.__getitem__,5)

    def test_setitem__(self):
        testCase = ArrayBasedList(10)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        testCase.__setitem__(0,2)
        self.assertEqual(testCase.__str__(), "2\n4\n5\n6\n")
        self.assertRaises(IndexError, testCase.__setitem__,5,2)

    def test__eq__(self):
        testCase = ArrayBasedList(10)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        other = [3,4,5,6]
        self.assertEqual(testCase.__eq__(other), True)
        other = [1,2,3,4]
        self.assertNotEqual(testCase.__eq__(other), True)

    def test_insert(self):
        testCase = ArrayBasedList(10)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        testCase.insert(0, 2)
        self.assertEqual(testCase.__str__(), "2\n3\n4\n5\n6\n")
        self.assertRaises(IndexError, testCase.insert, 5, 2)

    def test_delete(self):
        testCase = ArrayBasedList(10)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        testCase.delete(0)
        self.assertEqual(testCase.__str__(), "4\n5\n6\n")
        self.assertRaises(IndexError, testCase.delete, 5)

    def test_remove(self):
        testCase = ArrayBasedList(10)
        testCase.append(3)
        testCase.append(4)
        testCase.append(5)
        testCase.append(6)
        testCase.remove(3)
        self.assertEqual(testCase.__str__(), "4\n5\n6\n")
        self.assertRaises(ValueError, testCase.remove, 5)



if __name__ == '__main__':
    unittest.main()


