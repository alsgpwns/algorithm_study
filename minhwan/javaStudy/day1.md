
# **알고리즘 스터디** MH-Day1

## 1.두 정수 사이의 합
```java
class Solution {
  public int solution(int a, int b) {
      int result = 0;

      if (a < b) {
          for (int i = a; i <= b; i++) {
              result += i;
          }
      } else {
          for (int i = b; i <= a; i++) {
              result += i;
          }
      }
      return result;
  }
}
```

 * 정수 a 가 b보다 작은 수일 경우  a값을 b값과 같거나 작을때까지 ++해주고 result 변수에 더해주었고 그 외의 경우에는 b값을 a값과 같거나 작을경우 
  *   두 정수 사이의 합을 구할때 복합대입연산자를 사용하여 result = result +i 에서 변수를 한번 생략해주었습니다.
#
## 2.문자열 내 p와 y의 개수


```java
class Solution {
    boolean solution(String s) {
        boolean result = true;
        
        s = s.toUpperCase();
        
        int count =0;
        
        for( int i=0; i<s.length();i++){
            if(s.charAt(i)=='P')
                count++;
            else if(s.charAt(i)=='Y')
                count --;
        }

        if(count==0)
            return true;
        else
            return false;
    }
}
```
* 알파벳 py에 대해 대소문자 구별을 필요로 하지 않은 조건에서 toUpperCase함수를 사용해 대문자로 통일시켜주고 문자열s에 대한 p의 개수만큼 카운트를 +해주고 y의 개수만큼 카운트를 해줬습니다.

* 카운트의 합이 0일 경우true를 반환, 그 외의 경우에는 false를 반환시켜 주었습니다. 

