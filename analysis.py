import csv
import sys
import operator
from neighborhood import Neighborhood
from scipy.stats.stats import pearsonr

#@author Saad Kothawala



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
class LoadData():
    @staticmethod
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
        return len(neighborhoods)

    @staticmethod
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
        return len(infantMortalities)

    @staticmethod
    def makePrenatalCareArrays():
        f = open('Data/Public_Health_Statistics_-_Prenatal_care_in_Chicago__by_year__1999___2009.csv')
        csvF = csv.reader(f)
        rows = list(csvF)
        del rows[0] #row 0 is the header
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
        return len(percentOfInfantsGivenPrenatalCare)

def printCorrelationStatements(correlationCoefficient, variablesTested):
    print "The pearson correlation coefficent for " + variablesTested + " is: " + str(correlationCoefficient)

    if(correlationCoefficient > 0.1 and correlationCoefficient < 0.5):
        print "This means that there is a slightly positive correlation between "  + variablesTested
    elif(correlationCoefficient > -0.1 and correlationCoefficient < 0.1):
        print "This means that there is almost no correlation between "  + variablesTested
    elif(correlationCoefficient > 0):
        print "This means that there is a positive correlation between "  + variablesTested
    else:
        print "This means that there is a negative correlation between "  + variablesTested
    print "\n"

if __name__ == "__main__":
    print "Welcome to Infant Importality Rate Analysis"

    LoadData.makeNeighborhoodArray()
    print "Loaded " + str(len(neighborhoods)) + " neighborhoods"

    LoadData.getAndStoreInfantMortalities()
    print "Loaded death rates for " + str(len(infantMortalities)) + " neighborhoods"

    LoadData.makePrenatalCareArrays()
    print "Loaded prenatal averages for  " + str(len(percentOfInfantsGivenPrenatalCare)) + " neighborhoods"
    print "\n"

    ########################################End Data Loading#####Start Analysis###################################

    #Is there a relationship between infant mortality rate and the socioeconomic hardship index?
    perCapitaIncome = []
    for i in xrange(0,len(neighborhoods)):
        perCapitaIncome.append(float(neighborhoods[i].perCapitaIncome))
    correlationCoefficient = pearsonr(perCapitaIncome, infantMortalities)[0]

    printCorrelationStatements(correlationCoefficient, "per capita income and infant mortality rate")

    percentHousingCrowded = []
    for i in xrange(0,len(neighborhoods)):
        percentHousingCrowded.append(float(neighborhoods[i].percentHousingCrowded))
    correlationCoefficient = pearsonr(percentHousingCrowded, infantMortalities)[0]

    printCorrelationStatements(correlationCoefficient, "percent of houses crowded and infant mortality rate")

    percentHousingBelowPovertyLine = []
    for i in xrange(0,len(neighborhoods)):
        percentHousingBelowPovertyLine.append(float(neighborhoods[i].percentHousingBelowPovertyLine))
    correlationCoefficient = pearsonr(percentHousingBelowPovertyLine, infantMortalities)[0]

    printCorrelationStatements(correlationCoefficient, "percent of houses below the poverty line and infant mortality rate")

    percentUnEmployed = []
    for i in xrange(0,len(neighborhoods)):
        percentUnEmployed.append(float(neighborhoods[i].percentUnEmployed))
    correlationCoefficient = pearsonr(percentUnEmployed, infantMortalities)[0]

    printCorrelationStatements(correlationCoefficient, "unemplyment percent and infant mortality rate")

    percentWithoutDiploma = []
    for i in xrange(0,len(neighborhoods)):
        percentWithoutDiploma.append(float(neighborhoods[i].percentWithoutDiploma))
    correlationCoefficient = pearsonr(percentWithoutDiploma, infantMortalities)[0]

    printCorrelationStatements(correlationCoefficient, "percent of citizens without a diploma and infant mortality rate")

    hardshipIndex = []
    for i in xrange(0,len(neighborhoods)):
        hardshipIndex.append(float(neighborhoods[i].hardshipIndex))
    correlationCoefficient = pearsonr(hardshipIndex, infantMortalities)[0]

    printCorrelationStatements(correlationCoefficient, "hardship Index and infant mortality rate")


    #Is there a relationship between infant mortality rate and prenatal care?

    correlationCoefficient = pearsonr(percentOfInfantsGivenPrenatalCare, infantMortalities)[0]

    printCorrelationStatements(correlationCoefficient, "percent of infants given prenatal care and infant mortality rate")

    #Is there a relationship between infant mortality rate and geographic location?

    dictionary = {}
    for i in xrange(0,len(neighborhoods)):
        dictionary[neighborhoods[i].areaName] = infantMortalities[i]
    #http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
    sorted_dict = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)

    print "Neighborhood\t# of Mortalities"
    for (key, value) in sorted_dict:
        print key + "\t" + str(value)











