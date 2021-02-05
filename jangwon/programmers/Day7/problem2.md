**문제2**

### 2016년

https://programmers.co.kr/learn/courses/30/lessons/12901

```js
function solution(a, b) {
    const date = new Date(`${a},${b},2016`);
    let day= (date+"").split(' ');
    return day[0].toUpperCase()
}
```

```js
function solution(a, b) {
    let date = new Date(`2016, ${a} ${b}`);
    let arr = ["SUN","MON","TUE","WED","THU","FRI","SAT"];
    return arr[date.getDay()]
}
```

### 배운 점 
* ```Date()``` 메소드
* ```Date.getDay()``` getDay() 메서드는 주어진 날짜의 현지 시간 기준 요일을 반환합니다
* ```Date.getDate()``` getDate() 메서드는 주어진 날짜의 현지 시간 기준 일


### 레퍼런스
* https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date
* https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay
* https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/getDate
