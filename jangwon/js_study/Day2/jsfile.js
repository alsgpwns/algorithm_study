
/* 1번 */

function solution(arr, divisor) {    
  let result = arr.filter((el)=> el % divisor === 0).sort((a,b) => a - b);
  return result.length === 0 ? [ -1 ]: result;
}

/* 2번 */

function solution(strings, n) {
  return strings.sort((a, b) => a[n] == b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n]));
 }

 /* 3번 */
 
 function solution(s) {
  var answer = s.split("").sort().reverse().join("");
  return answer;
}