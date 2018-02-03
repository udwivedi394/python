import time

INT_MAX = 564646782

#Naive Solution with backtracking
def minSteps2dest(arr, cur_pos=0, steps=0):
        if cur_pos >= len(arr)-1:
                return steps
 
        if arr[cur_pos] == 0:
                return INT_MAX

        min_count = INT_MAX
        for i in range(1,arr[cur_pos]+1):
                count = minSteps2dest(arr, cur_pos+i, steps+1)
                if count < min_count:
                        min_count = count
        return min_count

arr = [1,3,5,8,9,2,6,7,6,8,9]

t1 = time.time()
print minSteps2dest(arr)
t2 = time.time()
print "Naive Solution:",t2-t1
