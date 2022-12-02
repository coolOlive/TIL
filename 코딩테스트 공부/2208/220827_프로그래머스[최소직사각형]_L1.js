// js 기본문법.. 낯설다 얼른 공부해서 익숙해져야겠어

function solution(sizes) {
    
    small=[]
    large=[]
    
    for (let i = 0; i<sizes.length;i++) {
        small.push(Math.min(...sizes[i]))
        large.push(Math.max(...sizes[i]))
    }
    
    return Math.max(...small)*Math.max(...large);
}