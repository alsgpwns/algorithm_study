import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int i=0;
        int k=people.length-1;
        Arrays.sort(people);
        
       while(i<=k) {
        	if(people[i]+people[k] <= limit) {
        		answer++;
        		i++;
        		k--;
        	}  else {
        		answer++;
        		k--;
        	}
        }
        return answer;
    }
}