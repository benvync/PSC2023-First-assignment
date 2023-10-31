n = 32
k = 3
def calculate_rabbits(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    Rabbits = [1, 1]  
    for i in range(2, n):
        offspring = Rabbits[-1] + k * Rabbits[-2]
        Rabbits.append(offspring)
    
    return Rabbits[-1]

result = calculate_rabbits(n, k)
print(result)
