import os, glob
import datetime as dt
import matplotlib.pyplot as plt

#folders = input("Enter date to retrieve (mm-dd-yyyy): ")
folders = ["04-27-2017","04-28-2017","05-01-2017"]


times = []
vals = []

for folder in folders:

    date = [int(x.strip()) for x in folder.split("-")]
    morn = dt.datetime(date[2], date[0], date[1])
    tim = []
    val = []
    for filename in os.listdir(folder):
        if not(filename.endswith(".txt")):
            continue

        #Extract time from filename
        filename = filename[:-4]
        timePieces = [int(x.strip()) for x in filename.split("-")]
        time = dt.datetime(hour=timePieces[0], minute=timePieces[1], \
                       second=timePieces[2], year=date[2], month=date[0], \
                           day=date[1])

        #Extract number of hosts up from file content

        with open(folder + "/" + filename + ".txt", "r") as file:
            data = file.readlines()

            try:
                num = int([(x.strip())[1:] for x in data[len(data)-1].split()][5])
            except ValueError:
                continue

        tim.append((time-morn).total_seconds()/3600)
        val.append(num)
    # End looping over files

    times.append(tim)
    vals.append(val)
# End looping over folders

#Graph the actual values
for i in range(len(times)):
    plt.scatter(times[i], vals[i])
plt.ylim(ymax=700, ymin=0)
plt.show()
