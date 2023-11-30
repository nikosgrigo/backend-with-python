from converter import is_valid_conversion,dipslay_available_conversions,measurement_converter
import unittest as u

class Tests(u.TestCase):

    '''Test the main functions in converter.py main app'''

    def test_is_valid_conversion(self):
        #Valid units
        self.assertTrue(is_valid_conversion("meters","feet"))
        self.assertTrue(is_valid_conversion("pascal","pound per square inch"))

        # #Invalid units
        self.assertFalse(is_valid_conversion("m","feet"))
        self.assertFalse(is_valid_conversion("axax","feet per second"))
        self.assertFalse(is_valid_conversion("pascal","skoko"))
        self.assertFalse(is_valid_conversion("258","bar"))
        self.assertFalse(is_valid_conversion("kilogram","6"))
        self.assertFalse(is_valid_conversion("","acre"))
        self.assertFalse(is_valid_conversion("celsius",""))
        self.assertFalse(is_valid_conversion("",""))

    def test_dipslay_available_conversions(self):
        #Valid units
        self.assertTrue(dipslay_available_conversions('meters'))
        self.assertTrue(dipslay_available_conversions('celsius'))
        self.assertTrue(dipslay_available_conversions('liter'))
        self.assertTrue(dipslay_available_conversions('pascal'))
        self.assertTrue(dipslay_available_conversions('meter per second'))

        #Invalid units
        self.assertFalse(dipslay_available_conversions(''))
        self.assertFalse(dipslay_available_conversions('me'))
        self.assertFalse(dipslay_available_conversions('pounds'))
        self.assertFalse(dipslay_available_conversions('watt'))
  
    def test_measurement_converter(self):
        #Check celsius to fahrenheit convertion
        self.assertEqual(measurement_converter(35,"celsius","fahrenheit") == 95,True)
        self.assertEqual(measurement_converter(20,"celsius","fahrenheit") == 68,True)

        #Check meters to feet and meters to yards
        self.assertEqual(measurement_converter(20,"meters","feet") == 65.62,True)
        self.assertEqual(measurement_converter(10000,"meters","yards") == 10936.1,True)

        #Write more to cover all possible values and methods


# Driver code
if __name__ == '__main__':
    u.main()