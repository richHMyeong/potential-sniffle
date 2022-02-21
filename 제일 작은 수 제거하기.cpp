#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;

    if (arr.size() != 1) {
        int ind = min_element(arr.begin(), arr.end()) - arr.begin();
        arr.erase(arr.begin() + ind);
        answer.assign(arr.begin(), arr.end());
    }
    else {
        answer.push_back(-1);
    }

    return answer;
}
