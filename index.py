# The aim of this mini project is to analyze the LARGE data by giving count of total number of squirrels for each color

import pandas

data = pandas.read_csv("Central_Park_Squirrel_Data.csv")

# First we will extract the fur column

furs = data["Primary Fur Color"]

print(furs.head())  # To print the first 5 entries

# To find out the number of furs 
print(furs.unique())
# Result - [nan 'Gray' 'Cinnamon' 'Black']

# Now we will extract each fur type

GrayFur = data[data["Primary Fur Color"] == "Gray"]
print(GrayFur.shape) # To find the data dimension

CinnamonFur = data[data["Primary Fur Color"] == "Cinnamon"]
print(CinnamonFur.shape)

BlackFur = data[data["Primary Fur Color"] == "Black"]
print(BlackFur.shape)

# Result - (2473, 31), (392, 31) and (103, 31)

GrayFurLen = len(GrayFur)
print(GrayFurLen)

CinnamonFurLen = len(CinnamonFur)
print(CinnamonFurLen)

BlackFurLen = len(BlackFur)
print(BlackFurLen)

FurColorNotAvailable = len( data[ data["Primary Fur Color"].isna() == True ] )
print(FurColorNotAvailable)

# Storing the data

Analysis = {
    "Fur Color" : ["Gray", "Cinnamon", "Black", "Not Available"],
    "Count" : [GrayFurLen, CinnamonFurLen, BlackFurLen, FurColorNotAvailable]
}


# Converting the dictionary to csv

AnalysisDF = pandas.DataFrame(Analysis)

# Saving to CSV

AnalysisDF.to_csv("AnalysisResult.csv")


# Viewing the csv

result = pandas.read_csv('AnalysisResult.csv')

print(result)
