#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = n;

    //���� ����
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());

    //������ ������ ü���� �Ҿ���� �л� ����
    for (vector<int>::iterator iter = reserve.begin(); iter != reserve.end();) {
        auto it = find(lost.begin(), lost.end(), *iter);

        if (it != lost.end()) {
            iter = reserve.erase(iter); //���⼭ �ε����� �޶���-> erase�� �޾Ƽ� iter�� �ٽ� ����
            lost.erase(it);
        }
        else {
            ++iter;
        }
    }

    answer = answer - lost.size();

    int count = 0;
    for (vector<int>::iterator iter = reserve.begin(); iter != reserve.end(); ++iter) {

        auto it1 = find(lost.begin(), lost.end(), (*iter) - 1);
        if (it1 != lost.end()) {
            count++;
            lost.erase(it1);
            continue;
        }


        auto it2 = find(lost.begin(), lost.end(), (*iter) + 1);
        if (it2 != lost.end()) {
            count++;
            lost.erase(it2);
        }
        //�ƹ��͵� ã�� ���ϸ� �׳� �Ѿ
    }
    answer = answer + count;

    return answer;
}
