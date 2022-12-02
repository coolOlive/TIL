function solution(bridge_length, weight, truck_weights) {
    var answer = 1;
    const que=new Array(bridge_length-1).fill(0)
    
    while (que.length!=0) {
        const tmp=que.reduce((sum,cur)=>sum+cur,0)
        if(tmp+truck_weights[0]<=weight && que.length+1<=bridge_length) {
            que.push(truck_weights.shift())
        }  else if (truck_weights.length!==0){
            que.push(0)
        }
        que.shift()
        answer+=1
        
    }
    
    return answer;
}