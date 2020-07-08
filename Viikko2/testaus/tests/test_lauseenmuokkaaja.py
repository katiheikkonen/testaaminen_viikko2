import unittest
import Viikko2.testaus.Lauseenmuokkaaja.lauseenmuokkaaja as lausemuokkaus

class MyTestCase(unittest.TestCase):

    # testaa sanat jonka pituus on 5 tai enemmän
    def test_reverse_word(self):
        exp = "appieH"
        result = lausemuokkaus.clausemachine('Heippa')
        self.assertEqual(result, exp)

    #  testaa sanat, joiden pituus on kaksi kirjainta
    def test_upper_letters(self):
        exp = "HI"
        result = lausemuokkaus.clausemachine('Hi')
        self.assertEqual(result, exp)

    # testaa lauseet
    def test_many_words(self):
        exp = "otulP IS a dog"
        result = lausemuokkaus.clausemachine('Pluto is a dog')
        self.assertEqual(result, exp)

    #  Lauseen ensimmäinen kirjain iso

    #  Viimeinen merkki joku seuraavista ”.!?” (jos ei ole, niin loppuun lisätään ”.”)


if __name__ == '__main__':
    unittest.main()
