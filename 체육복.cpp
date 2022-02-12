#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = n;

    //벡터 정렬
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());

    //여벌이 있으나 체육복 잃어버린 학생 제거
    for (vector<int>::iterator iter = reserve.begin(); iter != reserve.end();) {
        auto it = find(lost.begin(), lost.end(), *iter);

        if (it != lost.end()) {
            iter = reserve.erase(iter); //여기서 인덱스가 달라짐-> erase를 받아서 iter로 다시 쓰기
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
        //아무것도 찾지 못하면 그냥 넘어감
    }
    answer = answer + count;

    return answer;
}
