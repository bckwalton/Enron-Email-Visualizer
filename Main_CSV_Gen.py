import os
import csv

# Function to remove non Ascii's (Aded this to deal with odd spacing issues)


def removeNonAscii(s): return "".join(
    i for i in s if ord(i) < 126 and ord(i) > 31)


# Opens CSV file with write permissions
with open('email-actual.csv', 'w') as csvfile:
        # Goes to lowest level of each folder to files and runs below on each
    for root, dirs, files in os.walk("./maildir-(Actual)", topdown=False):
                # CSV writer
        csvFormatter = csv.writer(csvfile)
        # Run for each file
        for obj in files:
                        # constructs filepath
            filepath = root + os.sep + obj
            with open(filepath, "r") as it:
                from_str = " "
                to_str = " "
                try:
                    for line in it:
                        if line.startswith("X-From:"):
                            splits = line.split("X-From: ")
                            splits = splits[1].split('<', 2)
                            from_str = (splits[0])
                        elif line.startswith("X-To:"):
                            splits = line.split("X-To: ")
                            splits = splits[1].split('<', 2)
                            to_str = (splits[0])
                            break
                except UnicodeDecodeError:
                    break
                to_chunks = to_str.split(',')
                for chunk in to_chunks:
                    csvFormatter.writerow(
                        [removeNonAscii(from_str)] + [removeNonAscii(chunk)])
