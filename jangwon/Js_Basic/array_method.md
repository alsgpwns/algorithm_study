# 

## 1. 숫자 / 문자열 배열에서 중복 제거 하기

이것은 map/reduce/filter에 해당 되지 않는 것들인데, 이 리스트에서 제외 시키기에는 너무 간결하다. 

```jsx
let values = [3, 1, 3, 5, 2, 4, 4, 4];
let uniqueValues = [...ne Set(values)];
// uniqueValues is [3, 1, 5, 2, 4]
```

## 2. 간단한 검색(case-sensitive)

**filter() 함수는 인자로 제공되는 함수에 의해 test 를  통과한 모든 요소를 새로운 array로 만든다.** 

```jsx
let users = [
  { id: 11, name: 'Adam', age: 23, group: 'editor' },
  { id: 47, name: 'John', age: 28, group: 'admin' },
  { id: 85, name: 'William', age: 34, group: 'editor' },
  { id: 97, name: 'Oliver', age: 28, group: 'admin' }
];
let res = users.filter(it => it.name.includes('oli'));
// res is []
```

## 3. 간단한 검색(case-insensitive)

**정규 표현식을 이용한 필터링**

```jsx
let res = users.filter(it => new RegExp('oli', "i").test(it.name));
// res is
[
  { id: 97, name: 'Oliver', age: 28, group: 'admin' }
]
```

## 4. 특정 유저가 admin 권한을 갖고 있는지 확인

```jsx
let hasAdmin = users.some(user => user.group === 'admin');
// hasAdmin is true
```

## 5. array of arrays 펼치기

**첫번째 iteration은 […[], …[1, 2, 3]] 이렇게 결과가 나오는데, 이는 [1,2,3] 으로 바뀐다. 이것은 두번째 iteration 의 acc로 위치한다.**

```jsx
let nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
let flat = nested.reduce((acc, it) => [...acc, ...it], []);// flat is [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 6. 특정 키의 빈도를 포함하는 객체를 만들기

```jsx
let users = [
  { id: 11, name: 'Adam', age: 23, group: 'editor' },
  { id: 47, name: 'John', age: 28, group: 'admin' },
  { id: 85, name: 'William', age: 34, group: 'editor' },
  { id: 97, name: 'Oliver', age: 28, group: 'admin' }
];let groupByAge = users.reduce((acc, it) =>
  ({ ...acc, [it.age]: (acc[it.age] || 0) + 1 }),
{});// groupByAge is {23: 1, 28: 2, 34: 1}
```

## 7. array of objects 인덱싱 (lookup table)

**id로 유저를 찾기위해 전체 array 를 처리하는 것 대신에 user’s id 가 key로 작용하는 객체를 만들 수 있다. (일정한 검색 시간)**

```jsx
let uTable = users.reduce((acc, it) => ({...acc, [it.id]: it }), {})
// uTable equals:
{
  11: { id: 11, name: 'Adam', age: 23, group: 'editor' },
  47: { id: 47, name: 'John', age: 28, group: 'admin' },
  85: { id: 85, name: 'William', age: 34, group: 'editor' },
  97: { id: 97, name: 'Oliver', age: 28, group: 'admin' }
}
```

> uTable[85].name처럼 id로 데이터에 접근할 때 유용하다.

## `8. 배열 안의 각각의 item에서 특정 키로 유일한 값들 뽑아내기`

map()은 각 item 의 group 값만 모아서 새로운 배열을 만들것이다.

```jsx
let listOfUserGroups = [...new Set(users.map(it => it.group))];
// listOfUserGroups is ['editor', 'admin'];
```

## 9. 객체 key-value map 역전

```jsx
let cities = {
  Lyon: 'France',
  Berlin: 'Germany',
  Paris: 'France'
};
let countries = Object.keys(cities).reduce(
  (acc, k) => (acc[cities[k]] = [...(acc[cities[k]] || []), k], acc) , {});
// countries is
{
  France: ["Lyon", "Paris"],
  Germany: ["Berlin"]
}
```

## 10. 섭씨 온도를 화씨 온도로 바꾸기

```jsx
let celsius = [-15, -5, 0, 10, 16, 20, 24, 32]
let fahrenheit = celsius.map(t => t * 1.8 + 32);
// fahrenheit is [5, 23, 32, 50, 60.8, 68, 75.2, 89.6]
```

## 11.객체를 쿼리 스트링으로 인코딩하기

```jsx
let params = {lat: 45, lng: 6, alt: 1000};
let queryString = Object.entries(params).map(p => encodeURIComponent(p[0]) + '=' + encodeURIComponent(p[1])).join('&')
// queryString is "lat=45&lng=6&alt=1000"
```

## 12. 명시된 키와 함께 읽기 가능한 string 으로 유저 테이블 출력

```jsx
let users = [
  { id: 11, name: 'Adam', age: 23, group: 'editor' },
  { id: 47, name: 'John', age: 28, group: 'admin' },
  { id: 85, name: 'William', age: 34, group: 'editor' },
  { id: 97, name: 'Oliver', age: 28, group: 'admin' }
];
users.map(({id, age, group}) => `\n${id} ${age} ${group}`).join('')
// it returns:
"
11 23 editor
47 28 admin
85 34 editor
97 28 admin"
```

## 13. A와 B의 합집합

```jsx
let arrA = [1, 4, 3, 2];
let arrB = [5, 2, 6, 7, 1];
[...new Set([...arrA, ...arrB])]; // returns [1, 4, 3, 2, 5, 6, 7]
```

## 14. A와 B의 교집합

```jsx
let arrA = [1, 4, 3, 2];
let arrB = [5, 2, 6, 7, 1];arrA.filter(it => arrB.includes(it)); // returns [1, 2]
```