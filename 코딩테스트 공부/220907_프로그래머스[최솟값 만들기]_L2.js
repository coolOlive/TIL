function solution(a,b){
    var answer = 0;
    let L=a.length
    
    a.sort((num1,num2)=>{return num1-num2})
    b.sort((num1,num2)=>{return num2-num1})
    
    for (let i=0;i<L;i++) {
        answer+=a[i]*b[i]
    }

    return answer;
}