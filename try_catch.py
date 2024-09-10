x = input("Input length: ")
y = input("Input height: ")



def calculateArea(length, height):
    try:
        z = int(length) * int(height)
    except Exception as ex:
        z = None
        print("Exception occured: ",ex)
    
    print("multiplication value is:",z)


def calculateDiv(length, height):
    try:
        z = int(length) / int(height)
    except Exception as ex:
        z = None
        print("Exception occured: ",ex)
    
    print("division value is:",z)

calculateDiv(x,y)