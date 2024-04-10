salary_a = 0
sal = 0
population = 0
exit_zic = True
while exit_zic:
    sal = int(input())
    if sal == 0:
        exit_zic = False
    population += 1
    salary_a += sal

print(salary_a/(population-1))
