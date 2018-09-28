#Jude AND Max

class MyDictionary:
    def __init__(self):
        self.keyList = []
        self.valuesList = []

    def put(self, key, value):
        for i in range(len(self.keyList)):
            if key == self.keyList[i]:
                print('ERROR')
        self.keyList.append(key)
        self.valuesList.append(value)
    def get(self, key):
        return self.valuesList[self.keyList.index(key)]
    def remove(self, key):
        newVal = self.valuesList[self.keyList.index(key)]
        self.valuesList.remove(newVal)
        self.keyList.remove(key)
        return newVal
    def contains(self, key):
        return key in self.keyList
    def isEmpty(self):
        return len(self.keyList) == 0
    def size(self):
        return len(self.keyList)
    def keys(self):
        return self.keyList
    def values(self):
        return self.valuesList

class CompressDictionary:
    def __init__(self):
        self.dict = MyDictionary()
        self.phrase = input("Type the phrase: ")
        self.index = 0
    def compress(self):
        phrase = input("Type the phrase you want to compress: ")
        if phrase not in self.dict.values():
            self.dict.put(self.index, phrase)
            self.index += 1
    def getCompressedPhrase(self):
        newString = ""
        arr = self.phrase.split()
        for i in range(len(arr)):
            keyNotFound = True
            for j in range(self.index):
                if arr[i] == self.dict.get(j):
                    newString += str(j)
                    keyNotFound = False
            if keyNotFound:
                newString += (arr[i])
            newString += " "
        return newString

    def compressRate(self):
        totalVal = 0
        for i in range(self.index):
            totalVal += len(self.dict.get(i))
        return (len(self.phrase) - len(self.getCompressedPhrase()) + self.index + totalVal)/len(self.phrase) * 100
    def remove(self):
        

if __name__ == "__main__":
    test = CompressDictionary()
    for i in range(3):
        test.compress()
        print(test.getCompressedPhrase())
        print(test.compressRate())
