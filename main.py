import functions as f

unit_choices = {'meters':['feet', 'yards'],
                'celsius':["fahrenheit"],
                'square meter':["acre"],
                'kilogram':["ounce","pound"],
                'pascal':["bar","pound per square inch"],
                'liter':["cubic meter"],
                'joule':["calorie","watt"],
                'meter per second':["feet per second","miles per hour"],}

unitList =list(unit_choices.keys())

def init():

    '''Start program execution'''

    value = get_user_input()

    if(value):

      print("Please insert a valid unit to convert...")
      print(unitList)
      fromUnitString = input("Select one unit from the above list:").lower()

      if dipslay_available_convertions(fromUnitString):

         toUnitString = input("Now please enter unit to convert to:").lower()

         if is_valid_convertion(fromUnitString,toUnitString):
            measurement_converter(value,fromUnitString,toUnitString)
         else:
            print("Something went wrong!")

def dipslay_available_convertions(unit:str):
    '''This function 1.checks if current unit is available on the unit list (as key)
                     2.returns true if unit that user provided exists
    '''

    if unit in unit_choices:
      print(f"You can convert {unit} to: {unit_choices[unit]}")
      return True
    else:
      print(f"Oops sorry but this converter does not support {unit} unit yet!")
      return False

def get_user_input():
   '''This function ask user to enter a valid number and if not throws an error'''
   try:
    value = float(input("Enter a value to convert:"))
    return value
   except ValueError:
      print("Error message:Invalid input from user Please provide a number.")

def is_valid_convertion(fromUnit:str,toUnit:str):
   '''This function checks if the provided unit to convert exists in my list AND
     then checks if the unit to convert to is possible
     
     Returns: Boolean
     
     Parameters: fromUnit - current unit for convertion
                 toUnit - convert to this unit
   '''

   if fromUnit in unit_choices and toUnit in unit_choices[fromUnit]:
      return True
   else:
      return False

def measurement_converter(value,fromUnit,toUnit):
   # print("Start convertion...")
   print("---------------------------")

   fromUnit = fromUnit.replace(" ","_")
   toUnit = toUnit.replace(" ","_")

   # print(fromUnit,toUnit)

   function_name = f"{fromUnit}_to_{toUnit}"

   # print(function_name)

   # Check if the function exists in the module
   if hasattr(f, function_name) and callable(getattr(f, function_name)):
        # Call the function
       result = getattr(f, function_name)(value)
       print(f'{value} in {fromUnit} is equal to {result} in {toUnit}')
   else:
        print(f"Function '{function_name}' not found.")

init()



