#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;

    queue<int> ind; //인덱스 큐 
    queue<int> output; //출력 순서 저장 큐
    priority_queue<int> q; //가장 큰 값 알아내려고..algorithem의 max_element 사용하면 필요 없음.
    queue<int> prior; //priorites를 큐로 만듦. ind값으로 priorities 사용하면 필요 없을 듯.
    for (int i = 0; i < priorities.size(); i++) {
        ind.push(i); 
        q.push(priorities[i]);
        prior.push(priorities[i]);
    }

    while (!prior.empty()) {
        if (prior.front() < q.top()) {
            int n = ind.front();
            ind.pop();
            ind.push(n);
            n = prior.front();
            prior.pop();
            prior.push(n);
        }
        else {
            q.pop();
            output.push(ind.front());
            ind.pop();
            prior.pop();

        }
    }

    int cnt = 1;
    while (!output.empty())
    {
        if (output.front() == location) {
            break;
        }
        else {
            output.pop();
            cnt++;
        }
    }
    answer = cnt;
    return answer;
}