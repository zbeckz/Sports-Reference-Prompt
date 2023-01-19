import json
import sys

# this is the driver function
def main():

    # load the json file in as a python dictionary
    dataFile = open("data.json")
    dataDict = json.load(dataFile)
    dataFile.close()

    # create a 2d array where a value at row i, column j represents how many wins team i had against team j
    teams = list(dataDict.keys())
    numTeams = len(teams)
    dataMatrix = [[0] * numTeams for i in range(numTeams)] # numTeams x numTeams matrix filled with 0s
        
    # loop through the array and place the appropriate values in
    for row in range(numTeams):
        dataMatrix[row][row] = '--'
        for col in range(row + 1, numTeams): # to loop through these columns because the information is mirrored
            dataMatrix[row][col] = dataDict[teams[row]][teams[col]]['W']
            dataMatrix[col][row] = dataDict[teams[row]][teams[col]]['L']

if __name__ == "__main__":
    main()