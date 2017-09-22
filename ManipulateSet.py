import csv


comprehensive = open('comprehensiveSet.csv')
complexCSV = csv.reader(comprehensive)
header = next(complexCSV)

data = []
activity = []


def init_lists(data_list):
    for idx in range(0, 74):
        data_list.append([])


# Retrieving the data and putting into a list
def collect_data(data_list):
    print 'Collecting Data'
    for row in complexCSV:
        for index in range(0, len(row)):
            data_list[index].append(row[index])
        if len(row) < 74:
            for index2 in range(len(row), 74):
                data_list[index2].append([])


# Finding the frequency of every user, every week
# Also includes header data for better output file
# O(n^3) but works
def build_activities():
    print 'Finding Frequency of Data'
    activity[0].append(header[0])
    for user in range(0, 1000):
        activity[0].append(data[0][user])
    for number in range(1, len(activity)):
        activity[number].append(header[number])
    for week in range(1, 74):
        for entry in range(0, len(data[week])):
            wlogon = 0
            alogon = 0
            wklogon = 0
            logoff = 0
            exe = 0
            jpg = 0
            zip_file = 0
            txt = 0
            doc_pdf = 0
            iemail = 0
            eemail = 0
            site = 0
            wconnect = 0
            aconnect = 0
            wkconnect = 0
            disconnect = 0
            for idx, char in enumerate(data[week][entry]):
                if char == '1':
                    if data[week][entry][idx+1] == '0':
                        iemail += 1
                    elif data[week][entry][idx+1] == '1':
                        eemail += 1
                    elif data[week][entry][idx+1] == '2':
                        site += 1
                    elif data[week][entry][idx+1] == '3':
                        wconnect += 1
                    elif data[week][entry][idx+1] == '4':
                        aconnect += 1
                    elif data[week][entry][idx+1] == '5':
                        wkconnect += 1
                    elif data[week][entry][idx+1] == '6':
                        disconnect += 1
                    else: wlogon += 1
                elif char == '2':
                    alogon += 1
                elif char == '3':
                    wklogon += 1
                elif char == '4':
                    logoff += 1
                elif char == '5':
                    exe += 1
                elif char == '6':
                    jpg += 1
                elif char == '7':
                    zip_file += 1
                elif char == '8':
                    txt += 1
                elif char == '9':
                    doc_pdf += 1

            activity[week].append([wlogon, alogon, wklogon, logoff, exe, jpg,
                            zip_file, txt, doc_pdf, iemail, eemail, site,
                            wconnect, aconnect, wkconnect, disconnect])


# writing an output file with all the data
def write_csv():
    with open("comprehensiveFreq.csv", "wb") as f:
        print "Writing to File"
        writer = csv.writer(f)
        writer.writerows(activity)

# call functions
#init_lists(data)
#init_lists(activity)
#collect_data(data)
#build_activities()
#write_csv()
