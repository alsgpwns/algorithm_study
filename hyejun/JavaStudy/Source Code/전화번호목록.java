import java.util.*;
class Solution_전화번호목록 {
    public boolean solution(String[] phone_book) {
       	boolean answer = true;
        
		for(int i=0; i<phone_book.length-1; i++)
		{
			String prefix = phone_book[i];
			for(int j=i+1; j<phone_book.length; j++)
			{
				if(prefix.startsWith(phone_book[j])) return false;
				if(phone_book[j].startsWith(prefix)) return false;
			}
		}
        
        return answer;
    }
}