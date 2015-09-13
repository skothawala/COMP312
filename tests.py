import csv
import sys
import operator
import unittest
from neighborhood import Neighborhood
from analysis import LoadData
from scipy.stats.stats import pearsonr

#@author Saad Kothawala

class TestAnalysis(unittest.TestCase):  # use any meaningful name

    def testNeighborhoodObject(self):
        n = Neighborhood(0, 1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(n.areaNumber, 0)
        self.assertEqual(n.areaName, 1)
        self.assertEqual(n.percentHousingCrowded, 2)
        self.assertEqual(n.percentHousingBelowPovertyLine, 3)
        self.assertEqual(n.percentUnEmployed, 4)
        self.assertEqual(n.percentWithoutDiploma, 5)
        self.assertEqual(n.perCapitaIncome , 6)
        self.assertEqual(n.hardshipIndex, 7)


	#makes sure that the array length is equal and thus the indexes align
    def testLoading(self):
        neighborhoods = []
        numNeigborhoods = LoadData.makeNeighborhoodArray()
        leninfantMortalities = LoadData.getAndStoreInfantMortalities()
        lenPrenatalCare = LoadData.makePrenatalCareArrays()

        self.assertEqual(numNeigborhoods,leninfantMortalities, lenPrenatalCare)

    #tests index alignment
    def testAlignment(self):
        f = open('Data/Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv')
        neighborhoods = csv.reader(f)
        neighborhoods = list(neighborhoods)

        f = open('Data/Public_Health_Statistics-_Infant_mortality_in_Chicago__2005__2009.csv')
        mortalities = csv.reader(f)
        mortalities = list(mortalities)

        f = open('Data/Public_Health_Statistics_-_Prenatal_care_in_Chicago__by_year__1999___2009.csv')
        prenatalCare = csv.reader(f)
        prenatalCare = list(prenatalCare)

        self.assertEqual(prenatalCare[1][0], mortalities[1][0], neighborhoods[1][0])


    #makes sure the correlation method works properly, correlation should be 1
    def testCorrelation(self):
    	self.assertGreater(pearsonr([1,2,3], [1,2,3])[0], .999)

unittest.main()
