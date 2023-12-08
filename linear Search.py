from jovian.pythondsa import evaluate_test_cases

def linearSearch(elements,searchKey):
    position=0
    while position<len(elements):
        if elements[position]==searchKey:
            return position
        position+=1
    return -1
tests=[]
n=int(input("Enter the no.of test Case: "))
for i in range(n):
    print(i+1,'time')
    tests.append({'input':{'elements':list(map(int,input("Enter the elements: ").split())),'searchKey':int(input("Enter the search key: "))},'output':int(input("Enter the answer: "))})
#if linearSearch()

print(tests)

evaluate_test_cases(linearSearch,tests)