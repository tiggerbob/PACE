# CONSTANTS
temp = "secret message: "
validChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# QUERIES
step = int(input("What's the character step interval? "))
messageLength = int(input("How long is the secret message [chars]? "))

def readFile(file):
    f = open(file, "rt")
    r = f.read()
    f.close()
    return r

def magicMachine(str):
    l = str.split()
    count = -1
    stepCount = 1
    final = []
    for str in l:
        count += 1
        # variable value
        if stepCount > messageLength:
            break
        elif count % step == 0 and str[0] in validChar:
            final.append(str[0])
            stepCount += 1
        elif count % step == 0:
            final.append(str[1])
            stepCount += 1
        else:
            continue
    message = temp + ''.join(final).upper()
    if messageLength > 0:
        print(message)
    else:
        print("Denied [incorrect character length]")

# RUN
magicMachine(readFile("read.txt"))

