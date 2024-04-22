recent = []


def addRecent(data):
    if len(recent) == 5:
        recent.pop(0)
    recent.append(data)


def predictionMapping(prediction):
    if prediction == 0 or prediction == 4:
        return 0
    elif prediction == 5:
        return 1
    else:
        return 2


def predict(prediction):
    prediction = predictionMapping(prediction)
    if len(recent) > 2:

        if recent[len(recent)-1] == recent[len(recent)-2] == prediction:
            addRecent(prediction)
            return prediction
        else:
            if len(recent) > 3:
                if recent[len(recent)-1] == recent[len(recent)-3] == prediction:
                    addRecent(prediction)
                    return prediction
                else:
                    addRecent(prediction)
                    return recent[len(recent)-2]
            else:
                addRecent(prediction)
                return recent[len(recent)-2]
    else:
        addRecent(prediction)
        return prediction


testData = [0, 0, 0, 1, 1, 2, 2, 0, 2, 2, 4,
            4, 4, 5, 5, 0, 5, 4, 3, 3, 3, 0, 3, 4]

pred = []

for i in testData:
    pred.append(predict(i))

print(pred)
