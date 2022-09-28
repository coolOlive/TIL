function solution(n, t, m, p) {
    let answer = '', nums='';
    
    for (let i=0;i<m*t;i++) nums+=i.toString(n).toUpperCase();
    for (let j=p-1;j<t*m;j+=m) answer+=nums[j];
    
    return answer;
}