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
