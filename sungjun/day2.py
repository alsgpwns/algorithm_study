# 1번
def arr_divisor(arr, divisor):
    answer = []
    
    for a in arr:
        
        if a % divisor == 0:
            answer.append(a)
    
    if len(answer) == 0:
        return [-1]
    
    # return 하기 전 배열 오름차순 정렬
    answer.sort()
    
    return answer


# 2번
def sort_strings(strings, n):
    answer = []
    
    # lambda를 사용하여 strings[n]의 문자 기준으로 strings 정렬
    # sorted를 두번 사용하는 이유는 같은 문자일 경우 사전순으로 다시 정렬하기 위함
    answer = sorted(sorted(strings), key=lambda strings: strings[n])
    return answer

# 3번
def char_desc(s):
    answer = ''
    
    list_ascii_sort = []
    
    # 문자열을 ascii code로 형변환하여 리스트에 넣어줍니다. ascii code에서 대문자는 소문자보다 작습니다.
    for char in s:
        list_ascii_sort.append(ord(char))
    
    # reverse=True 내림차순 정렬
    list_ascii_sort.sort(reverse=True)
    
    # 문자열 취합
    for c in list_ascii_sort:
        answer += chr(c) 
        
    return answer 