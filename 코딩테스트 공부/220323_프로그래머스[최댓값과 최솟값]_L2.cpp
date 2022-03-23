#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> v;
    string num;
    
    for (int i = 0; i < s.size(); i++) {
        if(s[i] == ' ') {
            v.push_back(atoi(num.c_str()));
            num.clear();
        }
        else {
            num += s[i];
        }
    }
    v.push_back(atoi(num.c_str()));
    sort(v.begin(), v.end(), greater<int>());
    answer = to_string(v.back()) + " " +to_string(v.front());
    return answer;

}

// 오랫만에 벡터를 다루니 낯설어 푸는데 오래 걸렸다.
// 이건 다른 풀이법도 찾아서 블로그에 올려야겠다. -> c_str() , atoi 사용 복습하기**