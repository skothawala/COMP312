class Neighborhood:
    """This class contains Neighborhood information"""
    def __init__(self, areaNumber, areaName, percentHousingCrowded, percentHousingBelowPovertyLine, percentUnEmployed, percentWithoutDiploma, perCapitaIncome , hardshipIndex):
        self.areaNumber = areaNumber
        self.areaName = areaName
        self.percentHousingCrowded = percentHousingCrowded
        self.percentHousingBelowPovertyLine = percentHousingBelowPovertyLine
        self.percentUnEmployed = percentUnEmployed
        self.percentWithoutDiploma = percentWithoutDiploma
        self.perCapitaIncome  = perCapitaIncome
        self.hardshipIndex = hardshipIndex