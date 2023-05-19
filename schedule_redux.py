def lastVal(a):
    return pow(2, max(a)) % modulo

job, worker = list(map(int, input().split(' ')))
job_array = list(map(int, input().split(' ')))

modulo = pow(10,9) + 7

if worker == 1:
    sum = 0
    for j in job_array:
        sum += pow(2,j)
    print(sum % modulo)
elif worker >= job:
    print(lastVal(job_array))
elif worker < job:
    job_set = set(job_array)
    if len(job_set) == len(job_array):
        print(lastVal(job_array))
    else:
        job_array.sort()
        for i in range(len(job_array) - 1):
            if job_array[i] == job_array[i+1]:
                job_array[i] = 0
                job_array[i+1] += 1
                job -= 1
                job_array.sort()
            if job == worker + 1:
                second_last = len(job_array)-2
                third_last = len(job_array)-3
                print((pow(2, job_array[second_last]) + pow(2, job_array[third_last])) % modulo)
                break
            if job <= worker:
                print(lastVal(job_array))
                break



