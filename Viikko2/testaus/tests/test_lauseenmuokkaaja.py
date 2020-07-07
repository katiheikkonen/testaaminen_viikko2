import unittest
import Viikko2.testaus.Lauseenmuokkaaja.lauseenmuokkaaja as lausemuokkaus

class MyTestCase(unittest.TestCase):

    # testaa sanat jonka pituus on 5 tai enemmän
    def test_reverse_word(self):
        self.assertEqual(True, False)

    #testaa sanat, joiden pituus on kaksi


if __name__ == '__main__':
    unittest.main()
