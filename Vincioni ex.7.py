n = 81
m = 20
Ages = [0] * m
Ages[0] = 1
for _ in range(n - 1):
    New_Ages = [0] * m
    New_Ages[0] = sum(Ages[1:])
    
    for i in range(1, m):
        New_Ages[i] = Ages[i - 1]
    
    Ages = New_Ages

Population = sum(Ages)
print(Population)
