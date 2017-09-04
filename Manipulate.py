import csv

complex = open('comprehensiveSet.csv')

simpleCSV = csv.reader(complex)

header = next(simpleCSV)

data = []
activity = []
wlogon = 0
alogon = 0
wklogon = 0
logoff = 0
exe = 0
jpg = 0
zip = 0
txt = 0
doc_pdf = 0
iemail = 0
eemail = 0
site = 0
wconnect = 0
aconnect = 0
wkconnect = 0
disconnect = 0
count = 0


def init_lists(list):
    for idx in range(0, 74):
        list.append([])

init_lists(data)
init_lists(activity)

# retrieving the data and putting into a list
for row in simpleCSV:
    for index in range(0, len(row)):
        data[index].append(row[index])

# finding the frequency of every user, every week
# Skip the first data index (user ID)
# 1000 is the number of users
# Turn this into callable function
idz = 1

for entry in range(0, 1000):
    for idx, char in enumerate(data[idz][entry]):
        if char == '1':
            if data[idz][entry][idx+1] == '0':
                iemail += 1
            elif data[idz][entry][idx+1] == '1':
                eemail += 1
            elif data[idz][entry][idx+1] == '2':
                site += 1
            elif data[idz][entry][idx+1] == '3':
                wconnect += 1
            elif data[idz][entry][idx+1] == '4':
                aconnect += 1
            elif data[idz][entry][idx+1] == '5':
                wkconnect += 1
            elif data[idz][entry][idx+1] == '6':
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
            zip += 1
        elif char == '8':
            txt += 1
        elif char == '9':
            doc_pdf += 1

    activity[idz-1].append([wlogon, alogon, wklogon, logoff, exe, jpg, zip,
                        txt, doc_pdf, iemail, eemail, site, wconnect,
                        aconnect, wkconnect, disconnect])

    wlogon = 0; alogon = 0; wklogon = 0; logoff = 0; exe = 0; jpg = 0
    zip = 0; txt = 0; doc_pdf = 0; iemail = 0; eemail = 0; site = 0
    wconnect = 0; aconnect = 0; wkconnect = 0; disconnect = 0

print data[0]
print activity[0]