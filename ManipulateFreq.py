import csv
from os import listdir
from os.path import join, isfile

frequency = open('Test Files\comprehensiveFreq.csv')
frequencyCSV = csv.reader(frequency)
header = next(frequencyCSV)

allfiles = []
onlynames = []

mypath1 = "Test Files\Scenario 1"
mypath2 = "Test Files\Scenario 2"
mypath3 = "Test Files\Scenario 3"

onlyfiles1 = [f for f in listdir(mypath1) if isfile(join(mypath1, f))]
onlyfiles2 = [f for f in listdir(mypath2) if isfile(join(mypath2, f))]
onlyfiles3 = [f for f in listdir(mypath3) if isfile(join(mypath3, f))]

data = []
activity = []


def init_lists(data_list):
    for idx in range(0, 73):
        data_list.append([])


# Total number of activity plus one for header
def init_activities(activity_list):
    for idx in range(0, 73001):
        activity_list.append([])


# Create a list with all malicious users
def build_malicious():
    ind1 = range(len(onlyfiles1))
    ind2 = range(len(onlyfiles2))
    ind3 = range(len(onlyfiles3))

    for i in ind1:
        try:
            if ".csv" in onlyfiles1[i]:
                allfiles.append(onlyfiles1[i])
        except:
            pass

    for i in ind2:
        try:
            if ".csv" in onlyfiles2[i]:
                allfiles.append(onlyfiles2[i])
        except:
            pass

    for i in ind3:
        try:
            if ".csv" in onlyfiles3[i]:
                allfiles.append(onlyfiles3[i])
        except:
            pass

    for index in allfiles:
        onlynames.append(index[7:14])


# Retrieving the data and putting into a list
def collect_data(data_list):
    print('Collecting Data')
    itr = 0
    for row in frequencyCSV:
        for idx in range(0, len(row)):
            data_list[itr].append(row[idx])
        itr += 1


def build_activities():
    print('Formatting Data')
    build_malicious()

    index = 0
    activity[index].append('Users')
    activity[index].append('Weeks')
    activity[index].append('WeekdayLogon')
    activity[index].append('AfterhourLogon')
    activity[index].append('WeekendLogon')
    activity[index].append('Logoff')
    activity[index].append('FileExe')
    activity[index].append('FileJpg')
    activity[index].append('FileZip')
    activity[index].append('FileTxt')
    activity[index].append('FileDoc/pdf')
    activity[index].append('InternalEmail')
    activity[index].append('ExternalEmail')
    activity[index].append('Website')
    activity[index].append('WeekdayConnect')
    activity[index].append('AfterhoursConnect')
    activity[index].append('WeekendConnect')
    activity[index].append('DeviceDisconnect')
    activity[index].append('Malicious')
    for weeks in range(0, 73):
        index2 = 1
        for week in range(1000*index, (1000*index)+1000):
            activity[week+1].append(header[index2])
            activity[week+1].append(data[weeks][0])
            index2 += 1
        index += 1
    for weeks in range(0, 73):
        for users in range(1, len(data[weeks])):
            string = data[weeks][users].strip('[]').split(',')
            for char in range(len(string)):
                activity[(1000 * weeks) + users].append(string[char])

    for idx in range(1, len(activity)):
        if activity[idx][0] in onlynames:
            activity[idx].append('1')
        else:
            activity[idx].append('0')


def write_csv():
    with open("Test Files\output.csv", "wb") as f:
        print("Writing to File")
        writer = csv.writer(f)
        writer.writerows(activity)


init_lists(data)
init_activities(activity)
collect_data(data)
build_activities()
write_csv()





