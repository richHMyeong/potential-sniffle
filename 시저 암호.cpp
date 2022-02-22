#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string s, int n) {
    string answer = "";

    for (int i = 0; i < s.size(); i++) {
        
        if (isalpha(s[i])) {
            char tmp;
            if (isupper(s[i])) {
                if (s[i] + n > 90) {
                    tmp = (s[i] + n) % 90 + 64;
                }
                else {
                    tmp = s[i] + n;
                }
                answer = answer + tmp;
            }
            else {
                if (s[i] + n > 122) {
                    tmp = (s[i] + n) % 122 + 96;
                }
                else {
                    tmp = s[i] + n;
                }
                answer = answer + tmp;
            }
        }
        else {
            answer = answer + s[i];
        }
    }


    return answer;
}

int main() {
    cout << solution("a B z", 4) << endl;
}