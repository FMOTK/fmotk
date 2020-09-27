import numpy as np

W = np.array([[0, 0, 0]])
print("W size", W.shape)

inside = np.array([[1, 1, 0.3], [1, 0.4, 0.5], [1, 0.7, 0.8]])
print("Size of inside", inside.shape)

def Target(elements):
    if elements[1] == 1 and elements[2] == 0.3:
        return True
    elif elements[1] == 0.4 and elements[2] == 0.5:
        return True
    elif elements[1] == 0.7 and elements[2] == 0.8:
        return False

def Predict(inside_f):
    Sum = W.dot(inside_f.T)
    print("inside", inside_f)
    print("Sun", Sum)
    if Sum > 0:
        print("Predict", Sum > 0)
        return True
    else:
        print("Predict", Sum > 0)
        return False

perfect = False
while not perfect:
    perfect = True
    for e in inside:
        print("e", e)
        if Predict(e) != Target(e):
            perfect = False
            print("perfect", perfect)
            if Predict(e) == False:
                W = W + e
                print("w", W)
            elif Predict(e) == True:
                W = W - e
                print("W", W)
print("result", W)
