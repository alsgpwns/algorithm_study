# 문제 1
def num_to_list(n):
    n = str(n)
    # map을 사용해 배열안의 원소를 int로 캐스팅
    # 배열[::-1] == reverse()
    return list(map(int,list(n)[::-1]))


# 문제 2
def pe_class(n, lost, reserve):
    
    # 읽어버리고 여벌 챙긴 애들
    lost_but_reserved = set(reserve) & set(lost) 
    # 여분 가지고 있는 애들
    reserve = set(reserve) - lost_but_reserved
    # 아예 없는 애들
    lost = set(lost) - lost_but_reserved
    
    for r in reserve:
        
        if r + 1 in lost:
            lost.remove(r+1)
            
        elif r - 1 in lost:
            lost.remove(r-1)
            
    return n - len(lost)




# 문제 3
def get_divisor(n):
    answer = 0
    
    for i in range(1,n+1):
        # 나누어 떨어지면 더해주기
        if n % i == 0:
            answer += i
            
    return answer