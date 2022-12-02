function solution(cacheSize, cities) {
    var answer = 0;
    const L=cities.length
    let cach=[]
    
    if (cacheSize===0) return 5*L
    
    for (let i=0;i<L;i++) {
        let tmp=cities[i].toUpperCase()
        if (cach.includes(tmp)) {
            cach.splice(cach.indexOf(tmp),1)
            cach.push(tmp)
            answer+=1
            continue
        }
        if (cach.length==cacheSize) cach.shift()
        cach.push(tmp)
        answer+=5
    }

    return answer;
}