using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = -1;

    long long sum = 0;
    for (int i = 1; i <= count; i++) {
        sum = sum + (price * i);
    }

    if (money - sum >= 0) {
        answer = 0;
    }
    else {
        answer = (money - sum) * -1;
    }

    return answer;
}
