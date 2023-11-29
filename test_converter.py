# import converter  as m
# import unittest as u

# class Tests(u.TestCase):

#     def test_is_valid_conversion(self):
#         #Valid units
#         self.assertTrue(m.is_valid_conversion("meters","feet"))
#         self.assertTrue(m.is_valid_conversion("meter PEr second","feet per second"))
#         self.assertTrue(m.is_valid_conversion("pascal","BAR"))
#         self.assertTrue(m.is_valid_conversion("pascal","pound per square inch"))

#         # #Invalid units
#         self.assertFalse(m.is_valid_conversion("m","feet"))
#         self.assertFalse(m.is_valid_conversion("axax","feet per second"))
#         self.assertFalse(m.is_valid_conversion("pascal","skoko"))
#         self.assertFalse(m.is_valid_conversion("258","bar"))
#         self.assertFalse(m.is_valid_conversion("kilogram","6"))
#         self.assertFalse(m.is_valid_conversion("","acre"))
#         self.assertFalse(m.is_valid_conversion("celsius",""))
#         self.assertFalse(m.is_valid_conversion("",""))

#     def test_dipslay_available_conversions(self):
#         #Valid units
#         self.assertTrue(m.dipslay_available_conversions('meters'))
#         self.assertTrue(m.dipslay_available_conversions('celsius'))
#         self.assertTrue(m.dipslay_available_conversions('liter'))
#         self.assertTrue(m.dipslay_available_conversions('pascal'))
#         self.assertTrue(m.dipslay_available_conversions('meter per second'))

#         #Invalid units
#         self.assertFalse(m.dipslay_available_conversions(''))
#         self.assertFalse(m.dipslay_available_conversions('me'))
#         self.assertFalse(m.dipslay_available_conversions('pounds'))
#         self.assertFalse(m.dipslay_available_conversions('watt'))
  
#     def test_measurement_converter(self):
#         #Check celsius to fahrenheit convertion
#         self.assertEqual(m.measurement_converter(35,"celsius","fahrenheit") == 95)
#         self.assertEqual(m.measurement_converter(20,"celsius","fahrenheit") == 68)

#         #Check meters to feet and meters to yards
#         self.assertEqual(m.measurement_converter(20,"meters","feet") == 65.61)
#         self.assertEqual(m.measurement_converter(10000,"meters","yards") == 10936.13)

#         #Write more to cover all possible values and methods


# # Driver code
# if __name__ == '__main__':
#     u.main()
     
