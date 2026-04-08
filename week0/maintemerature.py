from temperature_converter import TemperatureConverter
cl= TemperatureConverter()
print('''
Program starting.
Initializing temperature converter...
Temperature converter initialized.
      
      ''')
while True: 
    print(
    '''
    Options:
    1) Set temperature
    2) Convert to Celsius
    3) Convert to Fahrenheit
    4) Convert to Kelvin
    0) Exit program
    '''
    )
    try:
        user = int(input('Choice: '))
        
        if user == 1:
            value  =int(input( 'Set Temprature: '))
            cl.setTemperature(value)
            print("Temperature set successfully.")

        elif user == 2:
            print(cl.toCelsius())
        elif user ==3:
            print(cl.toFahrenheit())
        elif user ==4:
            print(cl.toKelvin())
        elif user==0:
            print('Programme ending')
            break
        else:
            print('Invalid number!')
    except ValueError:
        print('Something went wrong.')