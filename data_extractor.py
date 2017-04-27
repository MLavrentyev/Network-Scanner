import os, glob
import datetime as dt
import matplotlib.pyplot as plt

#folder = input("Enter date to retrieve (mm-dd-yyyy): ")
folder = "04-27-2017"

date = [int(x.strip()) for x in folder.split("-")]
epoch = dt.datetime.utcfromtimestamp(0)
morn = dt.datetime(date[2], date[0], date[1])

times = []
vals = []

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

    times.append((time-morn).total_seconds()/3600)
    vals.append(num)

times, vals = zip(*sorted(zip(times, vals)))

plt.scatter(times, vals)
plt.ylim(ymax=700, ymin=0)
plt.show()
