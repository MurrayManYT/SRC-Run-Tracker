import urllib.request,json
import datetime
now = datetime.datetime.now()
GameID = input("Enter the Game ID") #Main Board ID.
CatExtID = input("Enter the Category Extension ID, if any, if you have no Category Extensions for your game, please input 'None'.") #Category Extension ID, feel free to remove if unnecessary.
#Searches for Main Board runs awaiting verification.VVVV
with urllib.request.urlopen(f"https://www.speedrun.com/api/v1/runs?game={GameID}&status=new&max=400") as url:
    data = json.loads(url.read().decode())
    mainBoardRuns = 1
    for number in data['data']:
        mainBoardRuns+=1
    print("number of main board runs is",mainBoardRuns) #Prints out runs in MCBE to the Terminal.

#Searches for Category Extension runs awaiting verification.VVVV
if CatExtID != "None":
    with urllib.request.urlopen(f"https://www.speedrun.com/api/v1/runs?game={CatExtID}&status=new&max=400") as url:
        data1 = json.loads(url.read().decode())
        ceRuns = 1
        for number in data1['data']:
            ceRuns+=1
        print("the number of category extension runs is",ceRuns)
        totalRuns = (mainBoardRuns + ceRuns)
        file = open("File Directory Here/DailyRuns.csv", "a")
        file.write(f"\n{datetime.datetime.now()},{totalRuns}")
        file.close()
        print("done, written to csv file.")
else:
    ceRuns = 0
    totalRuns = (mainBoardRuns + ceRuns)
    file = open("File Directory Here/DailyRuns.csv", "a")
    file.write(f"\n{datetime.datetime.now()},{totalRuns}")
    file.close()
    print("done, written to csv file.")