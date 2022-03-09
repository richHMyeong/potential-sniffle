#include <string>
#include <vector>
#include <stack>

using namespace std;

int lastItem(vector<vector<int>> &board, int n) {
    for (int i = 0; i < board.size(); i++) {
        if (board[i][n] != 0) {
            int num = board[i][n];
            board[i][n] = 0;
            return num;
        }
    }
    return 0;
}

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    stack<int> s;
    for (int i = 0; i < moves.size();i++) {
        int num=lastItem(board, moves[i]-1);
        
        if (num != 0) {
            if (!s.empty() && s.top() == num) {
                s.pop();
                answer++;
                answer++;
                //cout << "answer 변화함. 현재 answer " << answer << endl;
            }
            else {
                s.push(num);
                //cout << "push된 값 : " << num << endl;
            }
        }
    }





    return answer;
}
