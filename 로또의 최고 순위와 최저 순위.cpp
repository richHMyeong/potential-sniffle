#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int ranking(int n);

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;

    sort(lottos.begin(), lottos.end());
    sort(win_nums.begin(), win_nums.end());

    int numOfZero = 0;
    for (int i = 0; i < lottos.size(); i++) {
        if (lottos[i] == 0) {
            numOfZero++;
        }
        else {
            break; //정렬했으니까 0아닌 거 나오면 break하면 된다.
        }
    }

    int corr = 0; //맞은 숫자의 개수

    for (int i = 0, j = 0; i < lottos.size();) {
        if (lottos[i] == win_nums[j]) {
            corr++;
            i++; j++;
        }
        else if (lottos[i] > win_nums[j]) {
            while (lottos[i] > win_nums[j])
            {
                j++;
            }
        }
        else
        {
            //lottos[i]<win_nums[j]인 경우
            while (lottos[i] < win_nums[j])
            {
                i++;
            }

        }
    }

    int best = corr + numOfZero;
    //최고 등수, 최저 등수 계산
    answer.push_back(ranking(best));
    answer.push_back(ranking(corr));



    return answer;
}
int ranking(int n) {
    if (n == 6) { return 1; }
    else if (n == 5) { return 2; }
    else if (n == 4) { return 3; }
    else if (n == 3) { return 4; }
    else if (n == 2) { return 5; }
    else {
        return 6;
    }
}