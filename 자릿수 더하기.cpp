#include <iostream>

using namespace std;
int solution(int n)
{
    int answer = 0;
    
    long long tmp=n;
    
    while(tmp!=0){
        answer=answer+(tmp%10);
        tmp=tmp/10;
        
    }
    

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;

    return answer;
}
