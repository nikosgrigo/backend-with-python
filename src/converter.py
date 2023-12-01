import functions as f

'''You can convert only from key ---> values not the opposite'''

UNIT_CHOICES = {'meters':['feet', 'yards'],
                'celsius':["fahrenheit"],
                'square meter':["acre"],
                'kilogram':["ounce","pound"],
                'pascal':["bar","pound per square inch"],
                'liter':["cubic meter"],
                'joule':["calorie","watt"],
                'meter per second':["feet per second","miles per hour"],}

unitList =list(UNIT_CHOICES.keys())

def init():

   '''Start program execution'''

   value = get_user_input()

   print("Please insert a valid unit to convert...")
   print(unitList)
   fromUnitString = input("Select one unit from the above list:").lower()

   dipslay_available_conversions(fromUnitString)

   toUnitString = input("Now please enter unit to convert to:").lower()

   if is_valid_conversion(fromUnitString,toUnitString):
      measurement_converter(value,fromUnitString,toUnitString)
   else:
      print("Something went wrong!")

def dipslay_available_conversions(unit:str):
    '''This function 1.checks if current unit is available on the unit list (as key)
                     2.returns true if unit that user provided exists
    '''
    if unit in UNIT_CHOICES:
      print(f"You can convert {unit} to: {UNIT_CHOICES[unit]}")
    else:
      print(f"Oops sorry but this converter does not support {unit} unit yet!")

def get_user_input():
   '''This function ask user to enter a valid number and if not throws an error'''
   try:
      value = float(input("Enter a value to convert:"))
      return value
   except ValueError:
      print("Error message:Invalid input from user Please provide a number.")

def is_valid_conversion(fromUnit:str,toUnit:str):
   '''This function checks if the provided unit to convert exists in my list AND
     then checks if the unit to convert to is possible
     
     Returns: Boolean
     
     Parameters: fromUnit - current unit for convertion
                 toUnit - convert to this unit
   '''
   if fromUnit in UNIT_CHOICES and toUnit in UNIT_CHOICES[fromUnit]:
      return True
   else:
      return False

def measurement_converter(value,fromUnit,toUnit):
   print("---------------------------")

   fromUnit = fromUnit.replace(" ","_")
   toUnit = toUnit.replace(" ","_")

   function_name = f"{fromUnit}_to_{toUnit}"

   # Check if the function exists in the module
   if hasattr(f, function_name) and callable(getattr(f, function_name)):
       
        # Call the function
       result = getattr(f, function_name)(value)
       result = round(result,2)
       print(f'{value} in {fromUnit} is equal to {result} in {toUnit}')
   else:
        print(f"Function '{function_name}' not found.")

#The program execution start here with this function - DELETE COMMENT TO RUN
init()


