function solution(line) {
    const l=line.length
    const INF = Number.MAX_SAFE_INTEGER;
    let point=[]
    let xtmp=0,ytmp=0
    let minx=INF,maxx=-INF,miny=INF,maxy=-INF
    
    for (let i=0;i<l-1;i++) {
        for (let j=i+1;j<l;j++) {
            const [a, b, e] = line[i];
            const [c, d, f] = line[j];
            
            const down=(a*d)-(b*c)
            if (!down) continue
            
            xtmp=((b*f)-(e*d))
            ytmp=((e*c)-(a*f))
            if (xtmp%down || ytmp%down) continue
            
            xtmp/=down
            ytmp/=down
            minx=Math.min(minx,xtmp)
            maxx=Math.max(maxx,xtmp)
            miny=Math.min(miny,ytmp)
            maxy=Math.max(maxy,ytmp)
            point.push([xtmp,ytmp])
        }
    }
    
    let board=Array.from(Array(maxy-miny+1), ()=>
        Array(maxx-minx+1).fill('.')
    );
    
    point.forEach(([x,y])=> {
        board[maxy-y][x-minx]='*'
    })

    return board.map((bo)=>bo.join(""));
}