if Input== 't':
    
    initial = input("Please enter what unit you would like to convert. \nCelsius (type 'c') \nFahrenheit (type 'f') \nKelvin (type 'k') \n")
    
    
    if initial == 'c':
        final = input("Please enter what unit you would like to convert Celsius into: \nFahrenheit (type 'f') \nKelvin (type 'k') \n")
        amount = int(input("Please enter the amount of degrees in Celsius you would like to convert: "))
    elif initial == 'f':
        final = input("Please enter what unit you would like to convert Fahrenheit into: \nCelsius (type 'c') \nKelvin (type 'k') \n")
        amount = int(input("Please enter the amount of degrees in Fahrenheit you would like to convert: "))
    elif initial == 'k':
        final = input("Please enter what unit you would like to convert Kelvin into: \nCelsius (type 'c') \nFahrenheit (type 'k') \n")
        amount = int(input("Please enter the amount of degrees in Kelvin you would like to convert: "))
        
    temp = Temperature(initial, final, amount)
    temp.unit()
    
elif Input == 'v':
    initial = input("Please enter what unit you would like to convert. \nCubic meters (type 'm3') \nBarrel(type 'b')\nCubic feet(type 'ft3')\nCubic decimeter(type 'dm3')\n")
    
    if initial == "m3":
        final = input("Please enter what unit you would like to convert cubic meters to: \nBarrels (type 'b') \nCubic feet (type 'ft3') \nCubic decimeters (type 'dm3') \n")
        amount = int(input("Please enter the amount of cubic meters you would like to convert: "))
    elif initial == "b":
        final = input("Please enter what unit you would like to convert Barrels to: \ncubic meters (type 'm3') \nCubic feet (type 'ft3') \nCubic decimeters (type 'dm3') \n")
        amount = int(input("Please enter the amount of Barrels you would like to convert: "))
    elif initial == "ft3":
        final = input("Please enter what unit you would like to convert cubic feet to: \ncubic meters (type 'm3') \nBarrel (type 'b') \nCubic decimeters (type 'dm3') \n")
        amount = int(input("Please enter the amount of cubic feet you would like to convert:"))
    elif initial == "dm3":
        final = input("Please enter what unit you would like to convert cubic decimeters to: \ncubic meters (type 'm3') \nBarrel (type 'b') \nCubic feet (type 'ft3') \n")
        amount = int(input("Please enter the amount of cubic decimeters you would like to convert:"))   
    
    vol = Volume(initial, final, amount)
    vol.unit()
