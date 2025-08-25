import io
import unittest.mock
import exercise_math


class MyTestCase(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_math(self, mock_stdout):
        exercise_math.main()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "64")  # suma
        self.assertEqual(results[1], "50")  # diferencia
        self.assertEqual(results[2], "399")  # producto
        self.assertEqual(results[3], "32.0")  # promedio
        self.assertEqual(results[4], "8")  # cociente entero
        self.assertEqual(results[5], "1")  # resto
        self.assertEqual(results[6], "8.142857142857142")  # division real


if __name__ == '__main__':
    unittest.main()
