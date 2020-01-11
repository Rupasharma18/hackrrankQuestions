def pickingNumbers(arr):
    arr_s = sorted(arr)
    res = 1
    cur = 1
    diff = 0
    for ind in range(1, len(arr_s)):
        diff += arr_s[ind] - arr_s[ind - 1]
        if diff > 1:
            res = max(res, cur)
            cur = 1
            diff = 0
        else:
            cur += 1
            
    res = max(res, cur)
    
    return res
print  pickingNumbers([4, 6, 5, 3, 3, 1])     
print  pickingNumbers([1, 2, 2, 3, 1, 2])    