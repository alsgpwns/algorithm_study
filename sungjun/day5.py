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
