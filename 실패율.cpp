#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

//map을 value기준으로 정렬할 때 쓸 함수
bool cmp(const pair<int, float>& a, const pair<int, float>& b) {
    if (a.second == b.second) return a.first < b.first;
    return a.second > b.second;
}


vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;

    //각 스테이지 별 도전, 성공, 실패율 구하기.
    map<int, float> f_rate;

    int challenger = stages.size();
    int loser;
    //도전자를 설정. 그 후 실패자 찾기(현재i와 같은 숫자의 개수). 그 후 성공자 찾기.(저장해두기). 그 후 실패율 계산 후 저장(벡터에).
    for (int i = 1; i <= N; i++) {
        //실패자 구함
        loser=count(stages.begin(), stages.end(), i);
        
        
        //실패율 구해서
        float fail;
        if (challenger == 0) {
            fail = 0;
        }
        else {
            fail = loser * 1.0 / challenger;
        }
        //삽입
        f_rate[i] = fail;

        //성공자 구함
        int suc = challenger - loser;

        //다음 스테이지의 도전자는 현재 스테이지의 성공자이므로. challenger 갱신.
        challenger = suc;
    }

    //실패율 전부 구한 후 빠져나옴

    //실패율에 따라 정렬
    //map정렬의 두 단계. 
    //1. map을 vector로 이동 
    vector<pair<int, float>> v(f_rate.begin(), f_rate.end());

    //2.vector를 second기준으로 정렬
    sort(v.begin(), v.end(), cmp);

    
    for (int i = 0; i < v.size();i++) {
        answer.push_back(v[i].first);
    }

    return answer;
}
