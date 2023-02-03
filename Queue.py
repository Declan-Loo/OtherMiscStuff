#you got me looking for attention

MyQueue=['','',''] #List to test functions
HeadIndex = 0 #letting index be 1.
TailIndex = 1 #index of the next free space
NumberInQueue = 0

def Enqueue(DataToInsert):
    global MyQueue, HeadIndex, TailIndex, NumberInQueue
    if NumberInQueue > TailIndex - 1:
        return False
    else:
        MyQueue[TailIndex-1] = DataToInsert
        TailIndex += 1
        if TailIndex > len(MyQueue):
            TailIndex = len(MyQueue) #No more free space so keep at 9 aka max space
        NumberInQueue += 1
        return True

def Dequeue():
    global MyQueue, HeadIndex, TailIndex, NumberInQueue
    if NumberInQueue == 0:
        return -1
    else:
        #Move queue front
        if MyQueue[0] != '':
            value = MyQueue[HeadIndex]
        else:
            value = MyQueue[HeadIndex-1]
        for val in range(len(MyQueue)-1):
            MyQueue[val] = MyQueue[val+1]
        MyQueue[len(MyQueue)-1] = ''
        NumberInQueue -= 1
        if TailIndex == len(MyQueue) and NumberInQueue == len(MyQueue)-1: #Keep TailIndex the same, so it points to the free, recently dequeued space
            TailIndex = len(MyQueue)
        else: #Otherwise decrement TailIndex
            TailIndex -= 1
        return value
        
        
def CheckPosition():
    global MyQueue, HeadIndex, TailIndex, NumberInQueue
    number = int(input("Number: "))
    flag = False
    for i in range(1,len(MyQueue)+1):
        if MyQueue[i-1] == number:
            print("Integer is found in the queue.")
            flag = True
            return 'Position: ' + str(i)
    if flag == False:
        print("Integer is not found in the queue")
        return -1

print("Current state of queue")
print(MyQueue)
print()
print("Enqueue element 'John':")
Enqueue('John')
print(MyQueue)
print()
print("Enqueue element 'Abela':")
Enqueue('Abela')
print(MyQueue)
print()
print("Enqueue element 'Ling':")
Enqueue('Ling')
print(MyQueue)
print()

print("Dequeue element:",Dequeue())
print(MyQueue)
print()

print("Dequeue element:",Dequeue())
print(MyQueue)
print()

print("Final results:")
print(MyQueue)
print()
