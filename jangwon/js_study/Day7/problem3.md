**문제3**

### 직사각형 별 찍기

https://programmers.co.kr/learn/courses/30/lessons/12969

**문제 풀이**

1. 입력 된 값을 배열로 만들어주기 위해 ```Array().fill()``` 메소드 사용
2. 2차원 배열로 만들어주어 각 요소를 * 로 채워주기 위해 한번 더 사용
3. 배열을 순회하고 ```join()```메소드를 두번 사용하여 2차원 배열을 문자열로 바꿔줌


**풀이1**

```js
process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    let arr = Array(b).fill(Array(a).fill("*"));
    console.log(arr.map((el)=>el.join("")).join("\n"))
});
```

**다른 사람 풀이**

```js
process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    const row = '*'.repeat(a)
    for(let i =0; i < b; i++){
        console.log(row)
    }

});
```


### 배운 점 

* join의 줄바꿈 ```join(\n)``` join메소드와 줄 바꿈을 같이 사용할 수 있다는것 을 알았습니다.
* ```repeat()``` 메소드 : repeat메소드의 사용법 ```str.repeat()``` 
* https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/repeat