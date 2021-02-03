# 문제 1 

**완주 하지 못한 선수**

https://programmers.co.kr/learn/courses/30/lessons/42576
```
import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
      Arrays.sort(participant); // 참가자 오름차순 정렬시켜줌
      Arrays.sort(completion);  // 완주자 오름차순 정렬시켜줌
        
        for (int i =0; i<completion.length; i++) {
            if(!participant[i].equals(completion[i])){
                return participant[i];                     // for문 돌려 탐색 , i번째 참여자 ,완주자 불일치시, i번째 참여자 리턴
            }       
        }
        
            return participant[completion.length]; //참가자
    }
}
```
## 설명
  * 참가자, 완주자 배열 오름차순으로 정렬해줌 -> 정렬된 배열로 미완주자 판별을 위해서
  * for문 돌려 i번째 참가자, 완주자 불일치시 i번째 참가자 리턴시켜줌 

## 다른 풀이
```
import java.util.HashMap;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        for (String player : participant) hm.put(player, hm.getOrDefault(player, 0) + 1);
        for (String player : completion) hm.put(player, hm.get(player) - 1);

        for (String key : hm.keySet()) {
            if (hm.get(key) != 0){
                answer = key;
            }
        }
        return answer;
    }
}
```
* HashMap을 사용함 


# 문제 2 

**완전 탐색**

https://programmers.co.kr/learn/courses/30/lessons/42840
후에 공부해서 업로드 하겠습니다.
## 설명

# ## 문제 3

**이상한 문자 만들기**
```
https://programmers.co.kr/learn/courses/30/lessons/12930
class Solution {
    public String solution(String s) {
        String answer = "";
        int index = 0; //글자 순서 index
        for (int i=0; i<s.length(); i++){
            if (s.charAt(i) == ' '){
                answer += Character.toString(s.charAt(i));
                index = 0;
                continue;
            }
            if (index %2 == 0){ //index를 짝수 2로 나누었을때 0이면 대문자로 answer 에 저장 인덱스 증가
                answer += Character.toString(s.charAt(i)).toUpperCase(); //char ->String , 대문자로 변환하여 저장 
                index++;
            }
            else{ 
                answer += Character.toString(s.charAt(i)).toLowerCase(); 
                index++;
            }
        }
        return answer;
    }
}
```
## 설명
* char형 데이터를 String으로 변환 후 answer변수에 담아줌.
* index를 2로 나눴을때 0이면 toUpperCase()사용, 대문자로 변환하여 answer에 저장,  index +
* 그 외 , 소문자로 저장 index +
#  문제 4 

**문자열을 정수로 바꾸기**

https://programmers.co.kr/learn/courses/30/lessons/12925
```
import java.util.*;
class Solution {
    public int solution(String s) {
        return Integer.parseInt(s); //parseInt를 사용, 문자열을 숫자로 변환 
    }
}
```

## 설명
* parseInt를 이용, 스트링 변수를 Int형으로 변환해줌
#  문제 5

**평균 구하기**

```
https://programmers.co.kr/learn/courses/30/lessons/12944
class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        for(int i =0; i<arr.length;i++){
            answer+= arr[i];   //for문으로 배열 내 값들 +, answer 변수에 저장
        }
        return answer/(arr.length); // 더한 값들을 배열의 길이 만큼 나눠줌
    }
}
```
## 설명
* 배열안의 값들을 answer변수에 for문을 돌려 저장 후 배열의 길이만 큼 나눈 값을 리턴해줌