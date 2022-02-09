#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int func(vector<int> arr, vector<int> v) {
    vector<int> tmp;
    for (int i = v[0] - 1; i < v[1]; i++) {
        tmp.push_back(arr[i]);
    }
    sort(tmp.begin(), tmp.end());

    return tmp[v[2] - 1];
}




vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    for (int i = 0; i < commands.size(); i++) {
        answer.push_back(func(array, commands[i]));
    }


    return answer;
}