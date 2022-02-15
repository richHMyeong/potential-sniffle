#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int prim(int n) {
    vector<int> v;
    int k = 2;

    //소인수분해
    while (n != 1) {
        if (n % k == 0) {
            v.push_back(k);
            n = n / k;
        }
        else {
            k++;
        }
    }

    int cnt = 1;
    int tmp = 0;
    for (int i = 2; i <= k; i++) {
        tmp = count(v.begin(), v.end(), i);
        cnt = (tmp + 1) * cnt;
    }

    return cnt;
}
int solution(int left, int right) {
    int answer = 0;

    for (int i = left; i <= right; i++) {
        if (prim(i) % 2 == 0) {
            answer = answer + i;
        }
        else {
            answer = answer - i;
        }
    }
    return answer;
}
