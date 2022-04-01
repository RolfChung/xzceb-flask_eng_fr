import unittest
import machinetranslation
from translator import englishToFrench, frenchToEnglish


class Test_translator(unittest.TestCase): 
    def test_engl_french(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  
        self.assertEqual(englishToFrench('Welcome'), 'Bienvenue')
		# self.assertEqual(frenchToEnglish('0'), '0')  
        self.assertIsNotNone(frenchToEnglish('Soleil'),  "Test value is not none.")

    def test_french_engl(self): 
        self.assertEqual(frenchToEnglish('Bienvenue'), 'Welcome') 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')  
		# self.assertEqual(frenchToEnglish('0'), '0')  
        self.assertIsNotNone(frenchToEnglish('Soleil'),  "Test value is not none.")

if __name__ == '__main__':
		unittest.main(argv=[''], verbosity=3, exit=False)