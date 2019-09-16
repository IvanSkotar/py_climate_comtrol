from func import TempDataset

from collections import OrderedDict

current_set = TempDataset()
current_set.data_set = []
curr_unit = 0

def convert_units(celsius_value, units):
    if units == 0:
        return celsius_value
    if units == 1:
        return celsius_value * 1.8 + 32
    if units == 2:
        return celsius_value + 273.15

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

sensors = {
    "4213": ("STEM Center", 0),
    "4201": ("Foundations Lab", 1),
    "4204": ("CS Lab", 2),
    "4218": ("Workshop Room", 3),
    "4205": ("Tiled Room", 4),
    "Out": ("Outside", 5),
}

sorted_sensors = OrderedDict(sorted(sensors.items(), key = lambda x: x[0]))

filter_list = []

for a, b in sensors.items():
    filter_list.append(b[1])

def print_filter(filter_list):
    print('\nEdit room filter\n'
          '----------------')
    for a, b in sorted_sensors.items():
        if b[1] in filter_list:
            print(a + ":", b[0], '[ACTIVE]')
        else:
            print(a + ':', b[0])
    print('\nType "x" to return to Main Menu \n'
          'OR')

def change_filter(sorted_sensors, filter_list):
    print_filter(filter_list)
    option = input('Type the room number (e.g.4201) to deactivate sensor: ')
    if option == 'x':
        programm()
    elif option in sorted_sensors:
        for a, b in sorted_sensors.items():
            if option == a:
                if b[1] in filter_list:
                    filter_list.remove(b[1])
                else:
                    filter_list.append(b[1])
        change_filter(sorted_sensors, filter_list)
    else:
        print('Invalid Sensor\n')
        change_filter(sorted_sensors, filter_list)

def programm():
    print_menu()
    print(current_set.get_avg_temperature_day_time(filter_list, 5, 7))
    option = input('What is your choice?: ')
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
            elif option == 1:
                new_file()
                programm()
            elif option == 2:
                choose_units()
                programm()
            elif option == 3:
                change_filter(sorted_sensors, filter_list)
            elif option == 4:
                try:
                    print(current_set.get_summary_statistics(filter_list), UNITS[curr_unit])
                except:
                    print('\nPlease load data file and make sure at least one sensor is active')
                    programm()
            elif option == 5:
                # day = int(input('Enter a week day in numbers (e.g 0-6): '))
                # time = float(input('Enter a Time in 24h format: '))
                # print(current_set.get_avg_temperature_day_time(filter_list, day, time))
                programm()
            else:
                print('\nOption 1 selected\n')
                programm()
    except:
        print('\n*** Please enter an integer only ***\n')
        programm()

print('STEM Center Temperature Project\n'
      'Iullia Skotar\n'
      '')

def new_file():
    filename = input('Enter the file name of the new dataset: ')

    if current_set.process_file(filename):
        print('Loaded', len(current_set.data_set), 'number of samples')

        dataname = input('Please Enter 3 to 20 characters for the data name: ')
        while current_set.set_name(dataname) is False:
            print('Wrong name!')
            dataname = input('Please Enter 3 to 20 characters for the data name: ')
    else:
        print('File is not exist or incorrect format')

UNITS = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K"),
    }

def choose_units():
    global curr_unit
    print('\nCurrent unit is:', UNITS[curr_unit][0])
    print('\nChoose new units\n'
          '----------------')
    for key, value in UNITS.items():
        print(key, '-', value[0])
    unit_selection = input('\nWhich unit?: ')
    try:
        unit_selection = int(unit_selection)
        if unit_selection in UNITS.keys():
            curr_unit = unit_selection
        else:
            print('Please choose a unit from the list')
            choose_units()
    except:
        print('*** Please enter a number only ***')
        choose_units()

programm()
