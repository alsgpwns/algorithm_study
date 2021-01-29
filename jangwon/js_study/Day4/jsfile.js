
function solution1(s, n) {
  return s.split("").map((str) => {
    const code = str.charCodeAt() + n;
        if(str.charCodeAt() >= "a".charCodeAt() && str.charCodeAt() <= "z".charCodeAt()) {
            if(code > "z".charCodeAt()) return String.fromCharCode(code -26);
            return String.fromCharCode(code);
        }

        if(str.charCodeAt() >= "A".charCodeAt() && str.charCodeAt() <= "Z".charCodeAt()) {
            if(code > "Z".charCodeAt()) return String.fromCharCode(code -26);
            return String.fromCharCode(code);
        }
        return " ";
    }).join("");
  }


function solution2(arr) {
  arr.splice(arr.indexOf(Math.min(...arr)) ,1)
  return arr.length === 0 ? [-1] : arr
}

function solution3(n)
{
    var answer = 0;   
    let arr = n.toString().split("").map((el)=> parseInt(el))
    for(let i=0; i< arr.length; i++){
        answer += arr[i]
    }
    return answer
}