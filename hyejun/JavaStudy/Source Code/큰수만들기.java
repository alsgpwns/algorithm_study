import java.util.*;
class Solution {
    public String solution(String number, int k) {
        StringBuilder ans = new StringBuilder(number);
        String answer = "";
        
        while (k > 0) {
            int len = ans.length();
            boolean removed = false;
            for (int i = 0; i < len - 1; i++) {
                if (ans.charAt(i) < ans.charAt(i + 1)) {
                    ans.deleteCharAt(i);
                    removed = true;
                    break;
                }
            }
           if (!removed) {
            	answer = ans.substring(0, len - 1);
               return answer;
            }
            k--;
        }
        answer = ans.toString();
        return answer;
    }
}