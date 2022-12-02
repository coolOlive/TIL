function solution(participant, completion) {
    
    dic={}
    participant.forEach((par)=>par in dic?dic[par]+=1:dic[par]=0)
    completion.forEach((com)=>dic[com]==0?delete dic[com]:dic[com]-=1)
    
    return String(Object.keys(dic));
}