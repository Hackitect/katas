'''
given an array A of N integers, returns the smallest 
positive integer (greater than 0) that does not occur in A in O(n) time complexity

example A = [2,1,4,6,3] should return 5
'''

def solution(A):
    j = set(A)
    min_int = 1
    while min_int in j:
        min_int += 1
    return min_int

def offset_prog():
    offset = 8
    while offset != 0:
        print("correcting....",offset)
        offset -= 1

if __name__ == '__main__':
    offset_prog()


