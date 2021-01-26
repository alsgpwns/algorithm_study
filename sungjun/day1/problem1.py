def find_sum_between_two_nums(a, b):
    answer = 0
    
    # b > a 인 경우 a,b를 swap
    if a > b: 
        temp = b 
        b = a 
        a = temp
    
    for i in range(a, b+1):
        answer += i
        
    return answer