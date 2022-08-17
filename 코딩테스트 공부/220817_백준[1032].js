// 구현,문자열_명령 프롬프트/브론즈1
// js 공부

////입력받는 코드
const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
// let input = fs.readFileSync(__dirname+'/input.txt').toString().split("\n");

let n = +input[0];
const inputFileName = [];

for (let i = 1; i <= n; i++) {
  inputFileName.push(input[i]);
}

//////문제 풀이 코드
solution(inputFileName);

function solution(arr) {
  let answer = [];
  for (let i = 0; i < arr[0].length; i++) {
    let temp = arr[0][i];
    let num = 0;
    for (let j = 0; j < arr.length; j++) {
      if (temp !== arr[j][i]) {
        answer.push("?");
        break;
      } else {
        num++;
      }
      if (num === arr.length) answer.push(temp);
    }
  }
  console.log(answer.join(""));
}
