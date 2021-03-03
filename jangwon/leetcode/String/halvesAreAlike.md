# String

## 1704. Determine if String Halves Are Alike

* https://leetcode.com/problems/determine-if-string-halves-are-alike/

```js
var halvesAreAlike = function(s) {
    let str1 = s.substring(0,s.length / 2);
    let str2 = s.substring(s.length / 2, s.length);
    let count = 0;
    let arr =['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    
    for(let i=0; i<str1.length; i++){
        for(let el of arr){
            if(str1[i] === el){
                count++;
            }
            if(str2[i] === el){
                count--;
            }
        }
    }
    
    if(count === 0){
        return true;
    }
    return false;
};
```

* 다른 사람 풀이 

```js
return (s.substr(0, s.length/2).match(/[aeiouAEIOU]/g) || []).length === (s.substr(s.length/2).match(/[aeiouAEIOU]/g) || []).length;
```