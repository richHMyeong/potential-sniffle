#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    int answer = 0;
    
    long n=(long) num;
    if(n==1){
        return answer;
    }
    
    
    while(n!=1 && answer<500){
        if(n%2==0){
            n=n/2;
            answer++;
        }
        else{
            n=n*3+1;
            answer++;
        }
    }
    
    
    if(answer==500){
        answer=-1;
    }
    
    return answer;
}
