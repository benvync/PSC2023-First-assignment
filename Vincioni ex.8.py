#genotypes in total
k = 24
m = 22
n = 20
total_count = k + m + n

#dominance determination
dominant_k = 1
dominant_mm = 0.75
dominant_mn = 0.5
dominant_nn = 0

# Calculate probabilities for different genotype combinations
prob_kk = (k / total_count) * ((k - 1) / (total_count - 1)) * dominant_k
prob_km = (k / total_count) * (m / (total_count - 1)) * dominant_k
prob_kn = (k / total_count) * (n / (total_count - 1)) * dominant_k

prob_mk = (m / total_count) * (k / (total_count - 1)) * dominant_k
prob_mm = (m / total_count) * ((m - 1) / (total_count - 1)) * dominant_mm
prob_mn = (m / total_count) * (n / (total_count - 1)) * dominant_mn

prob_nk = (n / total_count) * (k / (total_count - 1)) * dominant_k
prob_nm = (n / total_count) * (m / (total_count - 1)) * dominant_mn
prob_nn = (n / total_count) * ((n - 1) / (total_count - 1)) * dominant_nn

#computation of the probability as a whole
total_probability = prob_kk + prob_km + prob_kn + prob_mk + prob_mm + prob_mn + prob_nk + prob_nm + prob_nn

print(total_probability)
