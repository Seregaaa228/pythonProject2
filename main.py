# ЗАДАЧА 1
def my_function(x, y):
    numbList = []
    for i in range(x, y):
        if i % 2 == 0:
            numbList.append(i)
    print(numbList)


my_function(1, 7)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


# ЗАДАЧА 2
def averageMarks(dictMarks):
    numbers = 0
    for i in dictMarks['class']['student']['marks'].items():
        numbers += i[1]
    average = numbers / len(dictMarks['class']['student']['marks'].items())
    return average


print(averageMarks(sampleDict))
