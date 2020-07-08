S = "13 DUP 4 POP 5 DUP + DUP + -"

'''
it should return 7
'''
stack=[]
def solution(S):
    
    S=S.split()
    
    
    for s in S:
        print (stack)
        if s.isdigit():
            pushes(s)
            print(s)
        elif s == "POP":
            word_pop()
            print(s)
        elif s == "DUP":
            word_dup()
            print(s)
        elif s == "+":
            addition()
            print(s)
        elif s == "-":
            substract()
            print(s)
        else:
            return None
    return stack.pop()

def pushes(b):
    return stack.append(b)
    
def word_pop():
    if len(stack) > 1:
        stack.pop()
        return stack
    return None
    
def word_dup():
    if len(stack) > 0:
        s = stack[-1]
        return stack.append(s)
    return None
    
def addition():
    if len(stack) > 1:
        num1 = int(stack.pop())
        num2 = int(stack.pop())
        s = num1 + num2
        return stack.append(s)
    return None
    

def substract():
    if len(stack) > 1:
        num1 = int(stack.pop())
        num2 = int(stack.pop())
        s = num1 - num2
        return stack.append(s)
    return None

if __name__ == '__main__':
    print(solution(S))