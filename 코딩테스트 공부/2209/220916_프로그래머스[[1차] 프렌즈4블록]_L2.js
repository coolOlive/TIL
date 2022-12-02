function solution(m, n, board) {
    let answer = 0
    
    while (true) {
        let four=Array.from(Array(m),() => Array(n).fill(0))

        // 탐색
        for (let i=0;i<m-1;i++) {
            for (let j=0;j<n-1;j++) {
                if (board[i][j]!=='-'&& board[i][j]===board[i][j+1] && board[i][j]===board[i+1][j+1] && board[i][j]===board[i+1][j]) {
                    four[i][j]=1; four[i][j+1]=1; four[i+1][j+1]=1; four[i+1][j]=1
                }
            }
        }
        
        // 지우는 갯수 count
        let cnt=0
        four.forEach((arr,i)=>arr.forEach((a,j)=>{
            if (a==1) {
                cnt+=1
                if (j>0 && j!=n-1) board[i]=board[i].slice(0,j)+'-'+board[i].slice(j+1,)
                else if (j===0) board[i]='-'+board[i].slice(j+1,)
                else board[i]=board[i].slice(0,j)+'-'
            }
        }));
        if (cnt===0) break
        answer+=cnt

        //값 당겨오기
        for (let i=m-1;i>=0;i--) {
            for (let j=n-1;j>=0;j--) {
                if (board[i][j]==='-') {
                    for (let k=i-1;k>=0;k--) {
                        if (board[k][j]!=='-') {
                            if (j>0) {
                                board[i]=board[i].slice(0,j)+board[k][j]+board[i].slice(j+1,)
                                board[k]=board[k].slice(0,j)+'-'+board[k].slice(j+1,)
                            } else {
                                board[i]=board[k][j]+board[i].slice(j+1,)
                                board[k]='-'+board[k].slice(j+1,)
                            }
                            break
                        }
                    }
                }
            }
        }
    }
    return answer;
}