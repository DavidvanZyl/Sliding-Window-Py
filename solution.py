import csv


def openBondCSV(filename):
    bondList = []
    with open(filename, 'r') as bond_list:
        reader = csv.reader(bond_list)
        bondList.extend(list(reader))
    return bondList


def findMaxProfitBonds(totalToFind, bondList):
    maxBonds = {}

    if not bondList:
        return -1
    if totalToFind <= 0:
        return -1

    for bondValues in bondList:
        boughtAt = -1
        salePrice = -1
        profit = -1
        isCheaperPriceFound = True
        bondName = bondValues[0]

        # +\-2 Accounts for bondName and length calculation
        for i in range(len(bondValues)-2):
            salePrice = bondValues[i+2]
            if isCheaperPriceFound:
                boughtAt = bondValues[i+1]
            if salePrice < boughtAt:
                isCheaperPriceFound = True
            else:
                isCheaperPriceFound = False
                temp = float(salePrice) - float(boughtAt)
                if temp > profit:
                    profit = temp

        if len(maxBonds) < totalToFind:
            maxBonds[bondName] = profit
        else:
            lowestMax = min(maxBonds, key=maxBonds.get)
            if profit >= maxBonds[lowestMax]:
                del maxBonds[lowestMax]
                maxBonds[bondName] = profit

    for key, value in maxBonds.items():
        print(key, ': ', value)


findMaxProfitBonds(
    3,
    openBondCSV('bond_px.csv')
)
