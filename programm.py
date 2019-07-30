from collections import OrderedDict

def print_menu():
    print('\nMain Menu\n'
          '---------\n'
          '0 - Convert temperature\n'
          '1 - Process a new data file\n'
          '2 - Choose units\n'
          '3 - Edit room filter\n'
          '4 - Show summary statistics\n'
          '5 - Show temperature by date and time\n'
          '6 - Show histogram of temperatures\n'
          '7 - Quit\n'
          '')

print_menu()

def convert_units(celsius_value, units):
    if units == 0:
        return celsius_value
    if units == 1:
        return celsius_value * 1.8 + 32
    if units == 2:
        return celsius_value + 273.15

sensors = {
    "4213": ("STEM Center", 0),
    "4201": ("Foundations Lab", 1),
    "4204": ("CS Lab", 2),
    "4218": ("Workshop Room", 3),
    "4205": ("Tiled Room", 4),
    "Out": ("Outside", 5),
}

sortedSensors = OrderedDict(sorted(sensors.items(), key=lambda x: x[0]))

filter_list = []


def print_filter(filter_list):
    print('\nEdit room filter\n'
          '----------------')
    for a, b in sortedSensors.items():
        if b[1] in filter_list:
            print(a + ":", b[0])
        else:
            print(a + ':', b[0], '[ACTIVE]')
    print('\nType "x" to return to Main Menu \n'
          'OR')

def change_filter(sortedSensors, filter_list):
    print_filter(filter_list)

    option = input('Type the room number to deactivate sensor: ')
    if option == 'x':
        programm()
    elif option in sortedSensors:
        for a, b in sortedSensors.items():
            if option == a:
                if b[1] in filter_list:
                    filter_list.remove(b[1])
                else:
                    filter_list.append(b[1])
        change_filter(sortedSensors, filter_list)
    else:
        print('Invalid Sensor\n')
        change_filter(sortedSensors, filter_list)

def programm():
    print_menu()
    option = input('What is your choice? ')
    try:
        option = int(option)
        if option < 0 or option > 7:
            print('\nInvalid Choice\n')
            programm()
        else:
            if option == 7:
                print('\nThank you for using the STEM Center Temperature Project\n')
            elif option == 0:
                celsius_t = input('\nPlease enter a temperature in °C: ')
                fahrenheit_t = convert_units(float(celsius_t), 1)
                kelvin_t = convert_units(float(celsius_t), 2)
                print('\nThat\'s', fahrenheit_t, '°F and', kelvin_t, '°K')
                programm()
            elif option == 3:
                change_filter(sortedSensors, filter_list)
            else:
                print('\nOption 1 selected\n')
                programm()
    except:
        print('\n*** Please enter an integer only ***\n')
        programm()

programm()
