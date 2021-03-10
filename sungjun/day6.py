def sort(n):
    """
    정수 내림차순으로 배치하기

    함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
    예를들어 n이 118372면 873211을 리턴하면 됩니다
    """
    list_n = list(str(n))
    list_n.sort(reverse=True)
    return int("".join(list_n))


def even_or_odd(num):
    """
    짝수와 홀수
    정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

    [제한 조건]
    num은 int 범위의 정수입니다.
    0은 짝수입니다.
    """
    return "Even" if num % 2 == 0 else "Odd"
