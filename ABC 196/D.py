principal = 6112800
principal1 = principal
investment_income = 0
for i in range(240):
    if (i+1)%12==0:
        #print(f"principal{principal}")
        principal1 = investment_income + principal
        print(f"社会人{(i+1)//12}年目で {int(principal1)}円")
    investment_income += ((principal1 * 0.00583) // 1)-24504