function solution(arr) {
    var answer = 0;

    arr.forEach((value)=> {
        answer+=value
    })

    return answer/arr.length;
}
