#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;

    string one = "12345";
    string two = "21232425";
    string three = "3311224455";
    while (one.size()<answers.size()) {
        one = one + "12345";
        if (answers.size() > two.size()) {
            two = two + "21232425";
        }
        if (answers.size() > three.size()) {
            three = three + "3311224455";
        }
        
    }

    vector<int> v = { 0,0,0 };

    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == (one[i] - '0')) {
            v[0]++;
        }
        if (answers[i] == (two[i] - '0')) {
            v[1]++;
        }
        if (answers[i] == (three[i] - '0')) {
            v[2]++;
        }
    }

    int val = *max_element(v.begin(), v.end());

    for (int i = 0; i < v.size(); i++) {
        if (val == v[i]) {
            answer.push_back(i+1);
        }
    }
    return answer;
}
