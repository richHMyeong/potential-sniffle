#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;

    vector<int> day;
    for (int i = 0; i < progresses.size(); i++) {
        day.push_back(100 - progresses[i]);
    }
    for (int i = 0; i < day.size(); i++) {
        if (day[i] % speeds[i] == 0) {
            day[i] = day[i] / speeds[i];
        }
        else {
            day[i] = day[i] / speeds[i] + 1; //나머지 있으니까 하루 더해줌.
        }
    }
    int val = day[0];
    int cnt = 1;
    for (int i = 1; i < day.size(); i++) {
        if (val >= day[i]) {
            cnt++;
        }
        else {
            answer.push_back(cnt);
            val = day[i];
            cnt = 1;
        }
    }
    
    answer.push_back(cnt);


    return answer;
}