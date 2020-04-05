# Send email to freshers with phone no., email, Name of respective team captain.
# Also send email to respective captain and vice captain about their info.

# importing csv module
import csv
from sendEmail import sendemailtoFresher, sendemailVC

# initializing the titles and rows list
def Init(filename):
    fields = []
    rows = []
    hockey = []
    football = []
    squash = []
    badi = []
    swimming = []
    cricket = []
    volly = []
    baski = []
    athletic = []
    weight = []
    tennis = []
    tt = []
    other = []
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = csvreader.next()

        # extracting each data row one by one
        for row in csvreader:
            c = 0
            if "Cricket" in row[5]:
                cricket.append(row)
                c =1
            if "Football" in row[5]:
                football.append(row)
                c =1
            if "Squash" in row[5]:
                squash.append(row)
                c=1
            if "Volleyball" in row[5]:
                volly.append(row)
                c=1
            if "Basketball" in row[5]:
                baski.append(row)
                c=1
            if "Athletic" in row[5]:
                athletic.append(row)
                c=1
            if "Weight Lifting" in row[5]:
                weight.append(row)
                c=1
            if "Tennis" in row[5]:
                tennis.append(row)
                c=1
            if "Swimming" in row[5]:
                swimming.append(row)
                c=1
            if "Badminton" in row[5]:
                badi.append(row)
                c=1
            if "Hockey" in row[5]:
                hockey.append(row)
                c=1
            if "Table" in row[5]:
                tt.append(row)
                c=1
            if c == 0:
                other.append(row)
    # sendemailVC(hockey, "Hockey")
    # sendemailVC(baski, "Basketball")
    # sendemailVC(athletic, "Athletic")
    # sendemailVC(tt, "Table")

    # sendemailVC(cricket, "Cricket")
    sendemailVC(Squash, "Squash")



if __name__ == '__main__':
    # csv file name
    filename = "/Users/mayankdubey/Desktop/Python/Freshers Info/Nilgiri Sports Fresher's Info.csv"
    Init(filename)
