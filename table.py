import json
import pandas as pd

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
        
    # loop through the rows of the array, place the appropriate values in, and print in table style
    for row in range(numTeams):
        dataMatrix[row][row] = '--'
        for col in range(row + 1, numTeams): # to loop through these columns because the information is mirrored
            dataMatrix[row][col] = dataDict[teams[row]][teams[col]]['W']
            dataMatrix[col][row] = dataDict[teams[row]][teams[col]]['L']

    # print the matrix as a table
    print(pd.DataFrame(dataMatrix, columns=teams, index=teams))

if __name__ == "__main__":
    main()