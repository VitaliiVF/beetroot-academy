def queue_time(customers, n):
    count = [0]*n
    for i in range(len(customers)):
        for j in range(len(count)):
            if count[j] == min(count):
                count[j] += customers[i]
                break
    return max(count)

print(queue_time([2,2,3,3,4,4], 2))