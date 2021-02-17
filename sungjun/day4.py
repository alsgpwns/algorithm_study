def caesar_cipher(s, n):
    """ 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
        제한 조건
        공백은 아무리 밀어도 공백입니다.
        s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
        s의 길이는 8000이하입니다.
        n은 1 이상, 25이하인 자연수입니다.
    """
    LEN_OF_ALPHABET = 26
    answer = ""

    for c in s:
        if c == " ":
            answer += " "
        else:
            if c.isupper():
                answer += chr((ord(c) + n - 65) % LEN_OF_ALPHABET + 65)
            else:
                answer += chr((ord(c) + n - 97) % LEN_OF_ALPHABET + 97)

    return answer


def list_value_in_arr(arr):
    """
    정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
    단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를
    리턴 하고, [10]면 [-1]을 리턴 합니다.
    """
    arr.remove(min(arr))

    if len(arr) == 0:
        return [-1]

    return arr


