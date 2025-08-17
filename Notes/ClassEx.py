#Example Class in Python
class MyClass:
    def __init__(self, nums):
        #Member vars
        self.nums = nums
        self.size = len(nums)




    def getLength(self):
        return self.size
    


    def getDoubleLength(self):
        return self.getLength() * 2


def main():

    myList = MyClass([1,2,3])
    print(myList.getLength())


if __name__ == "__main__":
    main()



