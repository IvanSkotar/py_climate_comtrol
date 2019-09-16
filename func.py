import math

class TempDataset:
    temp_dataset_count = 0

    def __init__(self):
        self.data_set = None
        self.name = "Unnamed"
        TempDataset.temp_dataset_count += 1

    def set_name(self, name):
        if type(name) is str and name.replace(' ', '').isalpha() and name.isprintable():
            if len(name) > 2 and len(name) < 21:
                self.name = name
                return True
            else:
                return False
        else:
            return False

    def get_name(self):
        return self.name

    def process_file(self, filename):
        try:
            my_file = open(filename, 'r')
            for line in my_file:
                row = line.split(',')
                new = ()

                if row[3] == 'TEMP':
                    new += (int(row[0]),)
                    new += (math.floor(float(row[1]) * 24),)
                    new += (int(row[2]),)
                    new += (float(row[4]),)
                    self.data_set.append(new)
            my_file.close()
            return True
        except:
            return False

    def get_summary_statistics(self, active_sensors):
        inactive_sensors = []
        if self.data_set is None:
            return None
        else:
            for data in self.data_set:
                for sensor in active_sensors:
                    if sensor == data[2]:
                        inactive_sensors.append(data[3])
            average = sum(inactive_sensors) / len(inactive_sensors)
            result = (min(inactive_sensors), max(inactive_sensors), float("{0:.3f}".format(average)))
            return result

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        temperature_values = []
        for data in self.data_set:
            for sensor in active_sensors:
                if sensor == data[2] and time == data[1] and day == data[0]:
                    temperature_values.append(data[3])
        if self.data_set is None:
            return None
        elif len(active_sensors) > 0 and len(temperature_values) > 0:
            average = float(sum(temperature_values) / len(temperature_values))
            return average
        else:
            return None

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if self.data_set is None:
            return None
        else:
            return 0

    def get_loaded_temps(self):
        if self.data_set is None:
            return None
        else:
            return len(self.data_set)

    def get_num_objects():
        return TempDataset.temp_dataset_count


"""=========================TESTS================================="""

if __name__ == "__main__":

    current_set = TempDataset()

    print("First test of get_num_objects: ", end='')

    if TempDataset.get_num_objects() == 1:
        print("Success")
    else:
        print("Fail")

    second_set = TempDataset()

    print("Second test of get_num_objects: ", end='')

    if TempDataset.get_num_objects() == 2:
        print("Success")
    else:
        print("Fail")

    print("Testing get_name and set_name: ")
    print("- Default Name:", end='')

    if current_set.get_name() == "Unnamed":
        print("Success")
    else:
        print("Fail")

    print("- Try setting a name too short: ", end='')

    if current_set.set_name("to"):
        print("Fail")
    elif not current_set.get_name() == "Unnamed":
        print("Fail")
    else:
        print("Success")

    print("- Try setting a name too long: ", end='')

    if current_set.set_name("supercalifragilisticexpialidocious"):
        print("Fail")
    elif not current_set.get_name() == "Unnamed":
        print("Fail")
    else:
        print("Success")

    print("- Try setting a name just right: ", end='')

    if not current_set.set_name("New Name"):
        print("Fail")
    elif current_set.get_name() == "New Name":
        print("Success")
    else:
        print("Fail")

    print("- Make sure we didn't touch the other object: ", end='')
    if second_set.get_name() == "Unnamed":
        print("Success")
    else:
        print("Fail")

    print("Testing get_avg_temperature_day_time: ", end='')
    if current_set.get_avg_temperature_day_time(None, 0, 0) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_num_temps: ", end='')
    if current_set.get_num_temps(None, 0, 0) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_loaded_temps: ", end='')
    if current_set.get_loaded_temps() is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_summary_statistics: ", end='')
    if current_set.get_summary_statistics(None) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing process_file: ", end='')
    if current_set.process_file(None) is False:
        print("Success")
    else:
        print("Fail")
