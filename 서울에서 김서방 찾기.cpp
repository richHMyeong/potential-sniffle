#include <string>
#include <vector>

using namespace std;

string solution(vector<string> seoul) {
    string answer = "";
    int ind;
    for (int i=0;i<seoul.size();i++){
        if("Kim"==seoul[i]){ ind=i; break;}
    }
    
    answer="김서방은 "+to_string(ind)+"에 있다";
    
    return answer;
}
