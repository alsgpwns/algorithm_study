# 자연수 뒤집어 배열로 만들기

https://programmers.co.kr/learn/courses/30/lessons/12932
```
import java.util.*;

class Solution {
  public int[] solution(long n) {
      String str1 = String.valueOf(n);
      String[] strs = str1.split(""); 

      List<String> list = Arrays.asList(strs);    //배열을 리스트로 변환해줌

      Collections.reverse(list);                  // 리스트 뒤집어 줌

    // 리스트를 배열로 다시 변환
    String[] str2 = list.toArray(new String[list.size()]);
    int[] result = new int[str2.length];

    for(int i=0 ; i<str2.length ; i++){
      answer[i] = Integer.parseInt(str2[i]);
    }      
      return result;
  }
}
```

# 체육복

https://programmers.co.kr/learn/courses/30/lessons/42862

```
import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int result = n;
        HashSet<Integer> resList = new HashSet<>();  
        HashSet<Integer> losList = new HashSet<>();

        for (int i : reserve)
            resList.add(i);
        for (int i : lost) {
            if(resList.contains(i))
                resList.remove(i);
            else
                losList.add(i);
        }
        for (int i : lost) {
            if(losList.contains(i)) {
                if(resList.contains(i-1))
                    resList.remove(i-1);
                else if(resList.contains(i+1))
                    resList.remove(i+1);
                else
                    result--;
            }
        } 
        return result;
    }
}
```
* 난이도가 어려워서 다른분의 코드를 참고했습니다. 후에 더 공부해서 풀 수 있도록 노력하겠습니다.

# 약수의 합 

https://programmers.co.kr/learn/courses/30/lessons/12928

```
class Solution {
    public int solution(int n) {
       
        int result = 0;
        
        for (int i =1; i<=n; i++){
            if(n % i == 0 ){
                result +=i;
                }
        }
	/*약수는 어느 수에 대해 나누었을때 0 으로 떨어지는 수라고 볼수 있다.
         이 값들을 모두 더한 값을 리턴해주었다.
	*/
        
        return result;


    }
}


```