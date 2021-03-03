# String

## 1108. Defanging an IP Address

* https://leetcode.com/problems/defanging-an-ip-address/

```js
var defangIPaddr = function(address) {
    let regex = /\./g
    return address.replace(regex,"[.]");
};
```