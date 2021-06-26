jobs = [int(num) for num in input().split(", ")]
index = int(input())

job_wanted = index
job_dict = {}

for job in range(len(jobs)):
    cc = jobs[job]
    ind = job
    if cc in job_dict:
        job_dict[cc].append(job)
    else:
        job_dict[cc] = []
        job_dict[cc].append(job)

job_dict = dict(sorted(job_dict.items(), key=lambda x: x[0]))

cycles = 0
is_wanted = False
for job, cc in job_dict.items():
    for c in range(len(job_dict[job])):
        if job_dict[job][c] == job_wanted:
            cycles += int(job)
            is_wanted = True
            break
        else:
            cycles += int(job)
    if is_wanted:
        break

print(cycles)

