def p_count_y_count(s):
    p_count = 0
    y_count = 0

    # 주어진 문자열을 모두 소문자로 변환
    s = s.lower()
    
    for char in s:
        
        if char == 'p':
            p_count += 1
        elif char == 'y':
            y_count += 1
    
    if p_count != y_count:
        return False

    return True