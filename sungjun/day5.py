from collections import Counter


def get_participant(participant, completion):
    """
    마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
    완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

    [제한사항]
    마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
    completion의 길이는 participant의 길이보다 1 작습니다.
    참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
    참가자 중에는 동명이인이 있을 수 있습니다.

    [풀이]
    collections 모듈에 Counter를 사용해보자. 알고리즘 문제풀이에 굉장히 유용할거 같아서 알아두면 좋을 것 같다.

    Counter 클래스는 딕셔너리의 객체들의 개수를 리턴해준다. key: 객체, values: 개수

    따라서 참가자, 완주자들의 이름을 key 개수를 value로 딕셔너리를 만들어 참가자 개수와 완주자 개수를 빼주면 완주하지 못한
    참가자가 나오게 된다. 코드의 가독성을 위해 single line으로 처리하기 보다는 따로 변수를 할당했다

    completion의 길이는 participant의 길이보다 1 작으므로 failed_participant의 첫번째 key만 return 해주면 정답이 된다.
    """

    participant_count_dict = Counter(participant)
    completion_count_dict = Counter(completion)

    failed_participant = participant_count_dict - completion_count_dict

    return list(failed_participant.keys())[0]


def exhaustive_search():
    """
    완전탐색 (Exhaustive Search)

    [문제 설명]
    수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

    1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

    1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
    """
    student_index_list = list()
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 학생 별 정답 카운트
    answer_count = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if answer == student_1[idx % len(student_1)]:
            answer_count[0] += 1

        if answer == student_2[idx % len(student_2)]:
            answer_count[1] += 1

        if answer == student_3[idx % len(student_3)]:
            answer_count[2] += 1
    # 최다 정답 개수
    max_answer_count = max(answer_count)

    # 최다 정답 개수와 같으면 학생 번호를 student_index_list에 추가
    for student, a in enumerate(answer_count):
        if max_answer_count == a:
            student_index_list.append(student + 1)

    return student_index_list


def char_to_upper(s):
    """ 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로,
        홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

        [제한 사항]
        문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
        첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
    """
    words = s.split(" ")
    answer = []

    for word in words:
        word = list(word)

        for idx, char in enumerate(word):
            if idx % 2 == 0:
                word[idx] = word[idx].upper()
            else:
                word[idx] = word[idx].lower()

        answer.append("".join(word))

    return " ".join(answer)


def is_instance(s):
    """
    문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

    [ 제한 조건 ]
    s의 길이는 1 이상 5이하입니다.
    s의 맨앞에는 부호(+, -)가 올 수 있습니다.
    s는 부호와 숫자로만 이루어져있습니다.
    s는 "0"으로 시작하지 않습니다.
    """
    if isinstance(s, str):
        return int(s)
    elif isistance(s, int):
        return str(s)

