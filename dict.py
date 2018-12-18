import time

#wf = open('out.txt','wb')
#n = eval(input("Number of pointers: "))
n = 400
maxV = 'হ্হ্হ্হ্হ্হ্হ্হ্হ্হ্হ্হ্হ্'
class Node:
    def __init__(self,n):
        self.totalKey = 0
        self.pNode = None #parent node
        self.values = [maxV]*1000
        self.cNode = [None]*1000

    def show(self):
        print(self.totalKey, self.pNode, self.values, self.cNode)


rootNode = Node(n)

def search(val, node):
    found = False
    for k in range (0,node.totalKey+1,1):
        print(val,node.values[k])
        if val==node.values[k].encode('utf-8'):
            return True
        elif val<node.values[k].encode('utf-8'):
            if node.cNode[k]==None:
                return False
            found = search(val,node.cNode[k])
            if found == True:
                break;

    return found

def printTree(node):

    newList = []
    for i in range(0,len(node),1):
        current = node[i]
        wf.write("[| ".encode('utf-8'))

        for j in range(0,current.totalKey,1):
            wf.write(current.values[j].encode('utf-8'))
            wf.write("|".encode('utf-8'))
            if current.cNode[j] != None:
                newList.append(current.cNode[j])
        j += 1
        if current.values[j] == maxV and current.cNode[j] != None:
            newList.append(current.cNode[j])
        wf.write("] ".encode('utf-8'))

    if(len(newList)==0):
        wf.write("\n".encode('utf-8'))
        del node[:]
    else:
        del node[:]
        wf.write("\n".encode('utf-8'))
        printTree(newList)







def splitLeaf(curNode):
    global rootNode
    if n%2 == 0:
        half = n//2
    else:
        half = (n+1)//2
    #print(half)
    rightNode = Node(n)
    curNode.totalKey = half
    rightNode.totalKey = n-half
    rightNode.pNode = curNode.pNode

    j = 0
    for i in range(half,n,1):
        rightNode.values[j] = curNode.values[i]
        curNode.values[i] = maxV
        j += 1

    val = rightNode.values[0]
    if(curNode.pNode == None):
        parent = Node(n)
        parent.totalKey = 1
        parent.values[0] = val
        parent.cNode[0] = curNode
        parent.cNode[1] = rightNode
        rightNode.pNode = parent
        curNode.pNode = parent

        rootNode = parent
        #rootNode.show()
       # print("child:")
        #rootNode.cNode[0].show()
       # rootNode.cNode[1].show()
        return


    else:
        curNode = curNode.pNode
        child = Node(n)
        child = rightNode

        for i in range(0,curNode.totalKey+1,1):
            if(val<curNode.values[i]):
                curNode.values[i], val = val, curNode.values[i]

        curNode.totalKey += 1
        for i in range(0,curNode.totalKey,1):
            if( child.values[0] < curNode.cNode[i].values[0]):
                curNode.cNode[i], child = child, curNode.cNode[i]

        curNode.cNode[i+1] = child

        i=0
        while(curNode.cNode[i] != None):
            curNode.cNode[i].pNode = curNode
            i += 1
        #print("yes")
        #rootNode.show()
        return
        
                
def splitNonLeaf(curNode):
    global rootNode
    half = n//2
    rightNode = Node(n)

    curNode.totalKey = half
    rightNode.totalKey = n-half-1
    rightNode.pNode = curNode.pNode

    j=0

    for i in range(half,n+1,1):
        rightNode.values[j] = curNode.values[i]
        rightNode.cNode[j] = curNode.cNode[i]
        curNode.values[i] = maxV
        if i!=half:
            curNode.cNode[i] = None
        j += 1
    val = rightNode.values[0]

    rightNode.values[:] = rightNode.values[1:]
    rightNode.cNode[:] = rightNode.cNode[1:]

    i = 0
    while(curNode.cNode[i] != None):
        curNode.cNode[i].pNode = curNode
        i+=1
    i = 0
    while(rightNode.cNode[i] != None):
        rightNode.cNode[i].pNode = rightNode
        i+=1

    if curNode.pNode == None:
        parent  = Node(n)
        parent.pNode  = None
        parent.totalKey = 1
        parent.values[0] = val
        parent.cNode[0] = curNode
        parent.cNode[1] = rightNode
        curNode.pNode = parent
        rightNode.pNode = parent

        rootNode = parent

        return
    else:
        curNode = curNode.pNode
        child = Node(n)
        child = rightNode

        #print(child.cNode)

        for i in range(curNode.totalKey+1):
            if val < curNode.values[i]:
                curNode.values[i], val = val, curNode.values[i]

        curNode.totalKey += 1
        j = 0
        for i in range(curNode.totalKey):
            if child.values[0]<curNode.cNode[i].values[0]:
                curNode.cNode[i], child = child, curNode.cNode[i]
            j += 1

        curNode.cNode[j+1] = child

        i = 0
        while (curNode.cNode[i] != None):
            curNode.cNode[i].pNode = curNode
            i += 1






def insert(curNode, val):
   # print("insert call:", val)
   # curNode.show()
    for i in range(0,curNode.totalKey+1,1):
        if(val < curNode.values[i]) and (curNode.cNode[i] == None):
            val, curNode.values[i] = curNode.values[i], val

            if (i==curNode.totalKey):
                curNode.totalKey += 1
                break
            
        elif(val < curNode.values[i]) and (curNode.cNode[i] != None):
            insert(curNode.cNode[i],val)
            
           # curNode.cNode[i].show()

            if(curNode.totalKey == n):
                splitNonLeaf(curNode)
            return

    if(curNode.totalKey == n):
        #curNode.show()
        splitLeaf(curNode)
        #curNode.show()

                

#rootNode.show()
         

#MAIN()-------------------------------------------------

#K = eval(input("How many Inputs: "))
#print("NUMBERS TO INPUT: ")
#inputVal = []
#for p in range(K):
#    x = input()
#    inputVal.append(x)
def Load():
    f = open('word.txt','r',encoding='utf-8')
    #wf = open('nw.txt','wb')
    cnt  = 0
    allWords = []
    while(1):
        cnt += 1
        message = f.readline().strip("\n")
        #print (cnt,message)
        if message == "":
            break;
        allWords.append(message)
        insert(rootNode, message)



    f.close()
    return allWords




nodeList = []
nodeList.append(rootNode)

#printTree(nodeList)
#wf.close()
#print(rootNode.cNode[0].values[0])
def searching(sVal):
    print(sVal.encode('utf-8'))

    if sVal.encode('utf-8')>=maxV.encode('utf-8'):
        return -1, False
       # print("Not found")
    else:
        t1 = time.time()
        found = search(sVal.encode('utf-8'),rootNode)
        t2 = time.time()

        if(found):
            print("Found", "in", t2-t1, "seconds" )
            return t2-t1, True
        else:
           # print("Not found")
            return -1, False
