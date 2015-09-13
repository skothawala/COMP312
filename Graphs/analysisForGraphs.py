import csv
import sys
import operator
from neighborhood import Neighborhood


#THIS FILE PRINTS OUT DATA POINTS TO BE IMPORTED INTO EXCEL AND USED TO MAKE THE GRAPHS IN THIS DIRECTORY



#stores neighborhood objects -> each object contains socioeconomic indicators
neighborhoods = []

#number of infant deaths for 2008-2009 for each neighborhood. 
#I'm throwing out the rest of the data (2005-2007) because the average socioeconomic indicators are only available up until 2012
infantMortalities = []

#the following data is an average of 2008-2009 (percents)
#store percent of parents that started giving prenatal care in the first trimester
percentOfInfantsGivenPrenatalCareFirstTrimester = []
#store percent of parents that started giving prenatal care in the second trimester
percentOfInfantsGivenPrenatalCareSecondTrimester = []
#store percent of parents that started giving prenatal care in the third trimester
percentOfInfantsGivenPrenatalCareThirdTrimester = []
#store percent of parents that gave prenatal care sometime
percentOfInfantsGivenPrenatalCare = []

########################################Data Loading###################################################

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
    del neighborhoods[-1] #last row is stats for whole chicago -> not needed

def getAndStoreInfantMortalities():
    f = open('Data/Public_Health_Statistics-_Infant_mortality_in_Chicago__2005__2009.csv')
    csvF = csv.reader(f)
    i = 0
    for row in csvF:
        if(i > 0):#row 0 is the header
            #the index is the neigborhood id -1 (since we start at 0). The index refers to the same neighborhood as the neigborhodos[]
            #Therefore, no need to store the neighborhood information along with this.
            infantMortalities.append(int(row[5]) + int(row[6]))
            i += 1
        else:
    		i += 1
    del infantMortalities[-1]#last row is stats for whole chicago -> not needed

def makePrenatalCareArrays():
    f = open('Data/Public_Health_Statistics_-_Prenatal_care_in_Chicago__by_year__1999___2009.csv')
    csvF = csv.reader(f)
    rows = list(csvF)
    del rows[0] #row 0 is the header
    rows.pop()
    index = 0
    while index < len(rows):
        #I have to do it this way because the data is incomplete. Some neighborhoods don't have data for percent of people who didn't report prenatal care
        #or percent who know they didn't give prenatal care
        #However, every neighborhood has data for percent of 1st, 2nd adn 3rd trimester

        #the first while loop loops through each neighborhood, when the index is updated the neighborhood changed
        currentNeigborhood = rows[index][0]
        totalPercentGiven = 0.0

        #this while loop loops through the data for the given neighborhood (e.g 1st, 2nd, 3rd trimeseter, not given or unknown)
        while (index + 1) < len(rows):
            if(currentNeigborhood == rows[(index + 1)][0]):
                average = (float(rows[index][40]) + float(rows[index][44])) / 2.0
                totalPercentGiven += average
                if("1ST" in rows[index][2]):
                    percentOfInfantsGivenPrenatalCareFirstTrimester.append(average)
                elif("2ND" in rows[index][2]):
                    percentOfInfantsGivenPrenatalCareSecondTrimester.append(average)
                elif("3RD" in rows[index][2]):
                    percentOfInfantsGivenPrenatalCareThirdTrimester.append(average)
                index += 1
            else:
                percentOfInfantsGivenPrenatalCare.append(totalPercentGiven)
                break
        index += 1

#Is there a relationship between infant mortality rate and the socioeconomic hardship index?
print "perCapitaIncome\n"
perCapitaIncome = []

for i in xrange(0,len(neighborhoods)):
    perCapitaIncome.append([float(neighborhoods[i].perCapitaIncome), infantMortalities[i]])

for row in perCapitaIncome:
    print str(row[0]) + ", " + str(row[1])

print "percentHousingCrowded\n"
percentHousingCrowded = []
for i in xrange(0,len(neighborhoods)):
    percentHousingCrowded.append([float(neighborhoods[i].percentHousingCrowded), infantMortalities[i]])

for row in percentHousingCrowded:
    print str(row[0]) + ", " + str(row[1])

print "percentHousingBelowPovertyLine\n"
percentHousingBelowPovertyLine = []
for i in xrange(0,len(neighborhoods)):
    percentHousingBelowPovertyLine.append([float(neighborhoods[i].percentHousingBelowPovertyLine), infantMortalities[i]])

for row in percentHousingBelowPovertyLine:
    print str(row[0]) + ", " + str(row[1])

print "percentUnEmployed\n"
percentUnEmployed = []
for i in xrange(0,len(neighborhoods)):
    percentUnEmployed.append([float(neighborhoods[i].percentUnEmployed), infantMortalities[i]])

for row in percentUnEmployed:
    print str(row[0]) + ", " + str(row[1])

print "percentWithoutDiploma\n"
percentWithoutDiploma = []
for i in xrange(0,len(neighborhoods)):
    percentWithoutDiploma.append([float(neighborhoods[i].percentWithoutDiploma), infantMortalities[i]])

for row in percentWithoutDiploma:
    print str(row[0]) + ", " + str(row[1])









