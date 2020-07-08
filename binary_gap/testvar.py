S = "13 DUP 4 POP 5 DUP + DUP + -"
stack = []

def solution(S):
    stack=[]
    S=S.split()
    for s in S:
        stack.append(s)
    return stack

if __name__=='__main__':
    solution(S)