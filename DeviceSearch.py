import time
import csv
from os import listdir
from os.path import join, isfile


device = []
email = []
file_list = []
http = []
logon = []
device_results = {}
email_results = {}
file_list_results = {}
http_results = {}
logon_results = {}
user_list = []

allfiles = []
malicious = []

mypath1 = "Test Files\Scenario 1"
mypath2 = "Test Files\Scenario 2"
mypath3 = "Test Files\Scenario 3"

onlyfiles1 = [f for f in listdir(mypath1) if isfile(join(mypath1, f))]
onlyfiles2 = [f for f in listdir(mypath2) if isfile(join(mypath2, f))]
onlyfiles3 = [f for f in listdir(mypath3) if isfile(join(mypath3, f))]

T = time.strptime('01/03/2010  6:45:00 AM', '%m/%d/%Y %H:%M:%S %p')
increment = 300  # in secs


end_time = time.mktime(T)  # time the file starts
start_time = time.mktime(time.strptime('01/02/2010 6:45:00 AM', '%m/%d/%Y %H:%M:%S %p'))

logon_incremented = {}
content_dict = {'numbers': 0}


# Create a list with all malicious users
def get_malicious():
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
        malicious.append(index[7:14])


# Extract data from files
def extract_file(file_path, data_list):
    f = open(file_path, 'r')
    reader = csv.reader(f)
    for row in reader:
        data_list.append(row)


# Create a list with all users
def get_users():
    for users in range(len(logon)):
        if logon[users][2] not in user_list:
            if logon[users][2] != 'user':
                user_list.append(logon[users][2])


def get_device_data(last_index, next_time):

    # device[n][1] = time and date
    # device[n][2] = user
    # device[n][3] = PC
    # device[n][4] = Activity
    usr_list = list(user_list)
    for i in range(last_index, len(device)):
        if time.mktime(time.strptime(device[i][1], '%m/%d/%Y %H:%M:%S %p')) <= next_time:
            # Put results to a table (list)
            if device[i][2] in device_results:
                device_results[device[i][2]].append([device[i][3], device[i][4], device[i][1],
                                                     start_time])
            else:
                device_results[device[i][2]] = [[device[i][3], device[i][4], device[i][1],
                                                 start_time]]
            last_index = i+1
            if logon[i][2] in usr_list:
                usr_list.remove(logon[i][2])
            continue
        else:
            for users in usr_list:
                if users in device_results:
                    device_results[users].append(['', '', '', start_time])
                else:
                    device_results[users] = [['', '', '', start_time]]
        break

    return last_index


def get_email_data(last_index, next_time):

    # email[n][1] = time and date
    # email[n][2] = user
    # email[n][3] = pc
    # email[n][4] = activity
    # email[n][5] = to:
    # email[n][6] = cc:
    # email[n][7] = bcc:
    # email[n][8] = size
    # email[n][9] = attachment
    # email[n][10] = content
    for i in range(last_index, len(email)):
        if time.mktime(time.strptime(email[i][1], '%m/%d/%Y %H:%M:%S %p')) <= next_time:
            # Put results to a table (list)
            if email[i][2] in email_results:
                email_results[email[i][2]].append([email[i][3], email[i][4], email[i][5],
                                                   email[i][6], email[i][7], email[i][8],
                                                   email[i][9], email[i][10], email[i][1],
                                                   start_time])
            else:
                email_results[email[i][2]] = [[email[i][3], email[i][4], email[i][5],
                                               email[i][6], email[i][7], email[i][8],
                                               email[i][9], email[i][10], email[i][1],
                                               start_time]]
            last_index = i + 1
            continue
        else:
            for users in user_list:
                if users in email_results:
                    email_results[users].append(['', '', '', '', '', '', '', '', '', start_time])
                else:
                    email_results[users] = [['', '', '', '', '', '', '', '', '', start_time]]
        break

    return last_index


def get_file_data(last_index, next_time):

    # file[n][1] = time and date
    # file[n][2] = user
    # file[n][3] = PC
    # file[n][4] = Filename.extension
    # file[n][5] = content
    usr_list = list(user_list)
    for i in range(last_index, len(file_list)):
        if time.mktime(time.strptime(file_list[i][1], '%m/%d/%Y %H:%M:%S %p')) <= next_time:
            # Put results to a table (list)
            if file_list[i][2] in file_list_results:
                file_list_results[file_list[i][2]].append([file_list[i][3], file_list[i][4],
                                                           file_list[i][5], file_list[i][1],
                                                           start_time])
            else:
                file_list_results[file_list[i][2]] = [[file_list[i][3], file_list[i][4],
                                                       file_list[i][5], file_list[i][1],
                                                       start_time]]
            last_index = i + 1
            if logon[i][2] in usr_list:
                usr_list.remove(logon[i][2])
            continue
        else:
            for users in usr_list:
                if users in file_list_results:
                    file_list_results[users].append(['', '', '', '', start_time])
                else:
                    file_list_results[users] = [['', '', '', '', start_time]]
        break

    return last_index


def get_http_data(last_index, next_time):
    # http[n][1] = time and date
    # http[n][2] = user
    # http[n][3] = PC
    # http[n][4] = URL
    # http[n][5] = content
    usr_list = list(user_list)
    for i in range(last_index, len(http)):
        if time.mktime(time.strptime(http[i][1], '%m/%d/%Y %H:%M:%S %p')) <= next_time:
            # Put results to a table (list)
            if http[i][2] in http_results:
                http_results[http[i][2]].append([http[i][3], http[i][4],
                                                 http[i][5], http[i][1], start_time])
            else:
                http_results[http[i][2]] = [[http[i][3], http[i][4],
                                             http[i][5], http[i][1], start_time]]
            last_index = i + 1
            if logon[i][2] in usr_list:
                usr_list.remove(logon[i][2])
            continue
        else:
            for users in usr_list:
                if users in http_results:
                    http_results[users].append(['', '', '', '', start_time])
                else:
                    http_results[users] = [['', '', '', '', start_time]]
        break

    for keys, values in http_results.items():
        for index in range(len(values)):
            if len(values[index][2]) > 0:
                for word in values[index][2].split():
                    try:
                        int(word)
                        content_dict['numbers'] += 1
                    except ValueError:
                        if word in content_dict:
                            content_dict[word] += 1
                        else:
                            content_dict[word] = 1

    return last_index


# Done as of now. Check later for bugs.
def get_logon_data(last_index, next_time):
    # logon[n][1] = time and date
    # logon[n][2] = user
    # logon[n][3] = PC
    # logon[n][4] = activity
    usr_list = list(user_list)
    total_logins = 0
    total_pc_list = []
    time_stamp = next_time
    for i in range(last_index, len(logon)):
        if time.mktime(time.strptime(logon[i][1], '%m/%d/%Y %I:%M:%S %p')) <= next_time:
            # Put results to a table (list)
            if logon[i][2] in logon_results:
                logon_results[logon[i][2]].append([logon[i][3], logon[i][4], logon[i][1],
                                                   start_time])

            else:
                logon_results[logon[i][2]] = [[logon[i][3], logon[i][4], logon[i][1],
                                               start_time]]
            last_index = i + 1
            if logon[i][2] in usr_list:
                usr_list.remove(logon[i][2])
            continue

        else:
            for users in usr_list:
                if users in logon_results:
                    logon_results[users].append(['', '', '', start_time])

                else:
                    logon_results[users] = [['', '', '', start_time]]
        break

    # Calculate Total Logins
    for keys, values in logon_results.items():
        for index in range(len(values)):
            if values[index][3] == time_stamp:
                if values[index][2] != '':
                    total_logins += 1

    # Calculate Total Different Computers
    for keys, values in logon_results.items():
        for index in range(len(values)):
            if values[index][3] == time_stamp:
                if values[index][0] != '':
                    if values[index][0] not in total_pc_list:
                        total_pc_list.append(values[index][0])
    total_pcs = len(total_pc_list)

    for keys, values in logon_results.items():
        login = 0
        after_logon = 0
        weekend_logon = 0
        usr_pc_list = []
        pc_count = 0
        nonuser_count = 0
        malicious_user = 0
        login_ratio = 0
        pc_ratio = 0
        for index in range(len(values)):
            if values[index][3] == time_stamp:
                if values[index][2] != '':
                    logon_time = str(time.strftime("%H %w", time.strptime(values[index][2],
                                                   '%m/%d/%Y %H:%M:%S %p'))).split()
                    login += 1
                    if int(logon_time[0]) < 8 or int(logon_time[0]) > 17:
                        after_logon += 1
                    if int(logon_time[1]) == 0 or int(logon_time[1]) == 6:
                        weekend_logon += 1
                if values[index][0] != '':
                    if values[index][0] not in usr_pc_list:
                        usr_pc_list.append(values[index][0])
                pc_count = len(usr_pc_list)
                if pc_count != 0:
                    nonuser_count = pc_count - 1
                if keys in malicious:
                    malicious_user = 1

        if total_logins > 0:
            login_ratio = login / total_logins
        if total_pcs > 0:
            pc_ratio = login / total_pcs

        if time_stamp in logon_incremented:
            logon_incremented[time_stamp].append([keys, login, after_logon, weekend_logon, pc_count,
                                                  nonuser_count, login_ratio, pc_ratio,
                                                  malicious_user])
        else:
            logon_incremented[time_stamp] = [[keys, login, after_logon, weekend_logon, pc_count,
                                              nonuser_count, login_ratio, pc_ratio,
                                              malicious_user]]

    return last_index


# Output non-incremented data
def create_csv():

    with open('Test Files/deviceDict.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Users', 'Device', 'Activity', 'Date and Time',
                         'Increment Time'])
        for key, value in device_results.items():
            for index in range(len(value)):
                writer.writerow([key, value[index][0], value[index][1],
                                 value[index][2], value[index][3]])

    with open('Test Files/logonDict.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Users', 'Device', 'Activity', 'Date and Time',
                         'Increment Time'])
        for key, value in logon_results.items():
            for index in range(len(value)):
                writer.writerow([key, value[index][0], value[index][1],
                                 value[index][2], value[index][3]])

    with open('Test Files/httpDict.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Users', 'Device', 'URL', 'Content', "Date and Time",
                         'Increment Time'])
        for key, value in http_results.items():
            for index in range(len(value)):
                writer.writerow([key, value[index][0], value[index][1],
                                 value[index][2], value[index][3], value[index][4]
                                 ])

    with open('Test Files/fileDict.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Users', 'Device', 'File name', 'Content', 'Date and Time',
                         'Increment Time'])
        for key, value in file_list_results.items():
            for index in range(len(value)):
                writer.writerow([key, value[index][0], value[index][1],
                                 value[index][2], value[index][3], value[index][4]
                                 ])

    with open('Test Files/emailDict.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Users', 'Device', 'Activity', 'To:', 'Cc:',
                         'Bcc:', 'Size', 'Attachment', 'Content', 'Date and Time',
                         'Increment Time'])
        for key, value in email_results.items():
            for index in range(len(value)):
                writer.writerow([key, value[index][0], value[index][1],
                                 value[index][2], value[index][3], value[index][4],
                                 value[index][5], value[index][6], value[index][7],
                                 value[index][8], value[index][9]])


# Output data for better visual.
def csv_logon_increment():

    with open('Test Files/Logon/_TotalData.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Increment', 'User', 'Logins', "Afterhours", "Weekend", "How many different machines",
                         "How many logins to non-user PC", "How many logins out of total during this period",
                         "How many unique machine logins out of total during interval", "Malicious User"])
        for keys, values in logon_incremented.items():
            for index in range(len(values)):
                writer.writerow([keys, values[index][0], values[index][1], values[index][2],
                                 values[index][3], values[index][4], values[index][5],
                                 values[index][6], values[index][7], values[index][8]])

    for users in user_list:
        with open('Test Files/Logon/' + users + ".csv", 'w', newline='') as csv_file1:
            writer1 = csv.writer(csv_file1)
            writer1.writerow(['Increment', 'Logins', "Afterhours", "Weekend", "How many different machines",
                              "How many logins to non-user PC", "How many logins out of total during this period",
                              "How many unique machine logins out of total during interval", "Malicious User"])
            for keys, values in logon_incremented.items():
                for index in range(len(values)):
                    if values[index][0] == users:
                        writer1.writerow([keys, values[index][1], values[index][2],
                                          values[index][3], values[index][4], values[index][5],
                                          values[index][6], values[index][7], values[index][8]])


def csv_content_histogram():
    with open('Test Files/HTTP/keywords.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Keys', 'Values'])
        for keys, values in content_dict.items():
            writer.writerow([keys, values])


extract_file('Test Files/deviceTest.csv', device)
extract_file('Test Files/emailTest.csv', email)
extract_file('Test Files/httpTest.csv', http)
extract_file('Test Files/fileTest.csv', file_list)
extract_file('Test Files/logonTest.csv', logon)

get_users()
get_malicious()

# loop through the files in a range based on time
device_last_index = 1
email_last_index = 1
file_last_index = 1
http_last_index = 1
logon_last_index = 1

while start_time < end_time:
    start_time = start_time + increment
    #device_last_index = get_device_data(device_last_index, start_time)
    #email_last_index = get_email_data(email_last_index, start_time)
    #file_last_index = get_file_data(file_last_index, start_time)
    #http_last_index = get_http_data(http_last_index, start_time)
    # logon_last_index = get_logon_data(logon_last_index, start_time)
    # print start_time, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))

#create_csv()
#csv_logon_increment()
#csv_content_histogram()





