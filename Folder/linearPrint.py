#Print linearly from 1 to N
count = 1
N = 10
def linearPrint(count, N):
    if count > N:
        return
    print(count)
    count += 1
    linearPrint(count, N)

linearPrint(count, N)
