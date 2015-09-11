import csv
from neighborhood import Neighborhood

neighborhoods = []

def makeNeighborhoodArray():
    f = open('Data/Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv')
    csvF = csv.reader(f)
    i = 0
    for row in csvF:
    	if(i > 0):#row 0 is the header
     		n = Neighborhood(row[0], row[1], row[2], row[3], row[4], row[5], row[6] , row[7])
    		neighborhoods.append(n)
    	else:
    		i += 1

def makeMortalityArray():
	f = open('Data/Public_Health_Statistics-_Infant_mortality_in_Chicago__2005__2009.csv')
    csvF = csv.reader(f)
    i = 0
    for row in csvF:
    	if(i > 0):#row 0 is the header
     		n = Neighborhood(row[0], row[1], row[2], row[3], row[4], row[5], row[6] , row[7])
    		neighborhoods.append(n)
    	else:
    		i += 1

print "Welcome to Infant Importality Rate Analysis"

makeNeighborhoodArray()
print "Loaded " + str(len(neighborhoods)) + " neighborhoods"

