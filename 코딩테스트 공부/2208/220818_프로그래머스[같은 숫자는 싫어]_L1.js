// 스택,큐

function solution(arr)
{
    var ans = [];
    
    for (let i = 0; i<arr.length;i++) {
        if (arr[i]==arr[i+1]) {
            continue
        } else {
            ans.push(arr[i])
        }
    }
    
    return ans;
}