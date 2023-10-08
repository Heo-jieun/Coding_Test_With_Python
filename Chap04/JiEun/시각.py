n = int(input())

times = []
for t in range(n+1):
    for m in range(60):
        for s in range(60):
            times.append(str(t)+str(m)+str(s))

new_times = []
for i in range(len(times)):
    if '3' in times[i] :
        new_times.append(times[i]) 
        
print(len(new_times))