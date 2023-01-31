bubble = []
N = int(input())
for i in range(N):
    bubble.append(int(input()))

for i in range(N-1) :
    for j in range(N-i-1):
        if bubble[j] > bubble[j+1]:
            bubble[j], bubble[j+1] = bubble[j+1], bubble[j] 
[print(v) for v in bubble]
