N = [1,2,147,483,647,1041,'word',1,0,-1,32]

P = 32
# print (bin(32)) >>> 0b100000

def solution():
    for i in range(len(N)):
        element = N[i]
        if type(element) == int and element > 1:
            print ("The binary representation for number: ", element, '\t', "is", 
            decimalToBinary(element), '\t', "has max gap", max_gap(element))
        else:
            print("not possible to print binary of ", element)
    
   
        

def decimalToBinary(N):
    return bin(N).replace("0b", "")

def max_gap(N):
    xs = bin(N)[2:].strip('0').split('1')
    return max([len(x) for x in xs])



if __name__ == '__main__':
    solution()