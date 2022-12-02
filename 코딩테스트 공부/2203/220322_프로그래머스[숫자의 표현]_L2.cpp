using namespace std;

int solution(int n) {
    int cnt = 1, start=2;
    int mid=n/2;
    
    if(n==1)
        return 1;
    else if(n%2==1) {
        cnt++;
        start--;
    }
    
    while(start<mid) {
        int tmp=0;
        for(int i=start;tmp<=n;i++) {
            if(tmp==n)
                cnt++;
            tmp+=i;
        }
        start++;
    }
    
    return cnt;
}