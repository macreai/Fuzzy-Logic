import csv
from multiprocessing import Condition

def splitData():
    filecsv = open(
        "D:\\belajar\\AI semester 4\\fuzzy logic\\bengkel.csv", "r")
    theDataLine = filecsv.read().split("\n")
    filecsv.close

    arrSprData = []
    splitData = []

    for i in theDataLine:
        splitData.append(i.split(","))

    for i in range(0, 100):
        arrSprData.append(splitData[i])

    return arrSprData

def fungsiServis(value):
    servisBaikmax = 90
    servisBaikmin = 80

    servisCukupmax = 85
    servisCukupmin = 50

    servisBurukmax = 55
    servisBurukmin = 20
    value = float(value)

    if (value <= 80.0):
        condition = 0
    elif (value > 90.0):
        condition = 1
    elif (80.0 < value <= 90.0):
        condition = (value - 80.0) / (90.0 - 80.0)
    elif (value <= 50.0):
        condition = 0
    elif (value > 85.0):
        condition = 1
    elif (50.0 < value <= 85.0):
        condiition = (value - 50.0) / (85.0 - 50.0)
    elif (value <= 20.0):
        condition = 0
    elif (value > 55.0):
        condition = 1
    elif (20.0 < value <= 55.0):
        condition = (value - 20.0) / (55.0 - 20.0)
    
    return condition

def fungsiHarga(value):
    hargaMahalmax = 9
    hargaMahalmin = 8

    hargaSedangmax = 8.5
    hargaSedangmin = 5

    hargaMurahmax = 5.5
    hargaMurahmin = 2
    value = float(value)

    if (value <= 8.0):
        condition = 0
    elif (value > 9.0):
        condition = 1
    elif (8.0 < value <= 9.0):
        condition = (value - 8.0) / (9.0 - 8.0)
    elif (value <= 5):
        condition = 0
    elif (value > 8.5):
        condition = 1
    elif (5.0 < value <= 8.5):
        condition = (value - 5.0) / (8.5 - 5.0)
    elif (value <= 2):
        condition = 0
    elif (value <= 5.5):
        condition = 1
    elif (2 < value <= 5.5):
        condition = (value - 2) / (5.5 - 2)
    
    return condition



