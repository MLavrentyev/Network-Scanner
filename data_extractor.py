import os
import datetime as dt

#folder = input("Enter date to retrieve (mm-dd-yyyy): ")
folder = "04-26-2017"

times = []
vals = []

for filename in os.listdir(folder):
    if not(filename.endswith(".txt")):
        continue

    #Extract time from filename
    filename = filename[:-4]
    timePieces = [int(x.strip()) for x in filename.split("-")]
    time = dt.time(hour=timePieces[0], minute=timePieces[1], \
                   second=timePieces[2])

    #Extract number of hosts up from file content

    with open(folder + "/" + filename + ".txt", "r") as file:
        data = file.readlines()

        num = int([(x.strip())[1:] for x in data[len(data)-1].split()][5])

    times.append(time)
    vals.append(num)
