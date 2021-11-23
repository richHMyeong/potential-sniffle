#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;

    queue<int> ind; //�ε��� ť 
    queue<int> output; //��� ���� ���� ť
    priority_queue<int> q; //���� ū �� �˾Ƴ�����..algorithem�� max_element ����ϸ� �ʿ� ����.
    queue<int> prior; //priorites�� ť�� ����. ind������ priorities ����ϸ� �ʿ� ���� ��.
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