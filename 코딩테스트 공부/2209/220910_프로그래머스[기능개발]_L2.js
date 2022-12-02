function solution(progresses, speeds) {
    var answer = [];
    let cnt=0
    
    while (progresses.length!==0) {
        if (progresses[0]>=100) {
            while(progresses[0]>=100) {
                cnt+=1
                progresses.shift()
                speeds.shift()
            }
            answer.push(cnt)
        } else {
            cnt=0
            for(let j=0;j<progresses.length;j++) {
                progresses[j]=progresses[j]+speeds[j]
            }
        }
    }
    
    return answer;
}