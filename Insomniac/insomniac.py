from random import choice

sleeping_pills = [1,2,3,4]

def awake(t):
    minutes = 0
    while minutes<t:
        minutes += random.choice(sleeping_pills)
    return minutes

n=100000
t=60
results=[]

for i in range(n):
    results.append(awake(t))

prob = round(results.count(t)/n,3)

print(f'The probability of the insomniac being awake at t={t} minutes is approximately {prob}')
