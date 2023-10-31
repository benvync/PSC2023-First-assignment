#lia
k = 19
N = 6
def calculate_probability(k, N):
    Generation = [0] * (k + 1) #list for n. of organisms in each generation
    Generation[0] = 1 #starts with heterozygous
    
    for gen in range(1, k + 1):
        Generation[gen] = Generation[gen - 1] * 2 #each doubles
    
    
    Prob = 0 #probab of those organisms to be in that generation
    for i in range(N, Generation[k] + 1):
        probability += (0.25 ** i) * (0.75 ** (Generation[k] - i)) * comb(Generation[k], i)
    
    return probability

def comb(n, k):
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result

def calculate_probability(k, N): #function to store p. in each gen
    dp = [[0] * (N + 1) for _ in range(k + 1)]
    dp[0][1] = 1
    
    for gen in range(1, k + 1):
        for n in range(N + 1): #current gen
            if n > 0:
                dp[gen][n] = 0.25 * dp[gen - 1][n - 1]
            dp[gen][n] += 0.75 * dp[gen - 1][n]

    Prob = sum(dp[k][N:]) #prob as a whole
    
    return Prob
result = calculate_probability(k, N)
print(result)




