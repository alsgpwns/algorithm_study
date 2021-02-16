function disjointSet (){
  // 부모 노드를 찾는 함수 (여기서 인자 array는 parent)
  function getParent (array,value) {
    let parent = array;
    if(parent[value] === value) return value;
    return parent[value] = getParent(parent,parent[value]);
  }

  // 두 부모 노드를 합치는 함수
  function unionParent(array,a,b) {
    let parent = array;
    const aRoot = getParent(parent,a);
    const bRoot = getParent(parent,b);
    if(aRoot < bRoot) parent[b] = a;
    else parent[aRoot] = bRoot;
  }

  // 같은 부모를 가지는지 확인

  function findParent(array,a,b) {
    const aRoot = getParent(array,a);
    const bRoot = getParent(array,b);
    if( aRoot === bRoot ) return true;
    return false;
  }

  function check () {
    let parent = [];
    for(let i=0; i<=10; i++ ) {
      parent[i] = i;
    }


    // 그래프 연결 과정 
    unionParent(parent,1,2);
    unionParent(parent,2,3);
    unionParent(parent,3,4);
    unionParent(parent,5,6);
    unionParent(parent,6,7);
    unionParent(parent,7,8);

    console.log(`1과 2는 연결이 되어 있나요??` , findParent(parent,1,2))
  }

  check();
}