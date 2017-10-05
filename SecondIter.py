import csv
from os import listdir
from os.path import join, isfile

comprehensive = open('comprehensiveSet.csv')
complexCSV = csv.reader(comprehensive)
header = next(complexCSV)

data = []
activity = []

onlynames = []

mypath1 = "Scenario 1"
mypath2 = "Scenario 2"
mypath3 = "Scenario 3"

onlyfiles1 = [f for f in listdir(mypath1) if isfile(join(mypath1, f))]
onlyfiles2 = [f for f in listdir(mypath2) if isfile(join(mypath2, f))]
onlyfiles3 = [f for f in listdir(mypath3) if isfile(join(mypath3, f))]


def init_lists(data_list):
    for idx in range(0, 74):
        data_list.append([])


# Retrieving the data and putting into a list
def collect_data(data_list):
    print('Collecting Data')
    for row in complexCSV:
        for index in range(0, len(row)):
            data_list[index].append(row[index])
        if len(row) < 74:
            for index2 in range(len(row), 74):
                data_list[index2].append([])


# Create a list with all malicious users
def build_malicious():

    allfiles = []

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


# Each activity has its own row. 1 if true, 0 if false.
def build_activities():
    print('Formatting Data')
    build_malicious()

    count = 0
    index = 1

    # Determine number of total activities
    for users in range(1000):
        for weeks in range(1, len(data)):
            if len(data[weeks][users]) > 0:
                count += len(data[weeks][users].split())

    for activities in range(count+1):
        activity.append([])

    activity[0].append('User')
    activity[0].append('Week')
    activity[0].append('WeekdayLogon')
    activity[0].append('AfterhourLogon')
    activity[0].append('WeekendLogon')
    activity[0].append('Logoff')
    activity[0].append('FileExe')
    activity[0].append('FileJpg')
    activity[0].append('FileZip')
    activity[0].append('FileTxt')
    activity[0].append('FileDoc/pdf')
    activity[0].append('InternalEmail')
    activity[0].append('ExternalEmail')
    activity[0].append('Website')
    activity[0].append('WeekdayConnect')
    activity[0].append('AfterhoursConnect')
    activity[0].append('WeekendConnect')
    activity[0].append('DeviceDisconnect')
    activity[0].append('Malicious')

    for users in range(1000):
        for weeks in range(1, 74):
            if len(data[weeks][users]) > 0:
                string = data[weeks][users].split()
                for activities in range(len(string)):
                    if string[activities] == '1':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        activity[index].append('1')
                        for idx in range(15):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '2':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        activity[index].append('0')
                        activity[index].append('1')
                        for idx in range(14):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '3':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(2):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(13):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '4':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(3):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(12):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '5':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(4):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(11):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '6':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(5):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(10):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '7':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(6):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(9):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '8':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(7):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(8):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '9':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(8):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(7):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '10':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(9):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(6):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '11':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(10):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(5):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '12':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(11):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(4):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '13':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(12):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(3):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '14':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(13):
                            activity[index].append('0')
                        activity[index].append('1')
                        for idx2 in range(2):
                            activity[index].append('0')
                        index += 1
                    elif string[activities] == '15':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(14):
                            activity[index].append('0')
                        activity[index].append('1')
                        activity[index].append('0')
                        index += 1
                    elif string[activities] == '16':
                        activity[index].append(data[0][users])
                        activity[index].append(header[weeks])
                        for idx1 in range(15):
                            activity[index].append('0')
                        activity[index].append('1')
                        index += 1

    for idy in range(1, len(activity)):
        if activity[idy][0] in onlynames:
            activity[idy].append('1')
        else:
            activity[idy].append('0')


# writing an output file with all the data
def write_csv():
    with open("output1.csv", "wb") as f:
        print("Writing to File")
        writer = csv.writer(f)
        writer.writerows(activity)


init_lists(data)
collect_data(data)
build_activities()
write_csv()

