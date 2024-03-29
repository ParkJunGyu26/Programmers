#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int sum = 0;
    int idx = 0;
    
    // 다리 위에 올라간 트럭
    queue<int> q;
    
    while(idx != truck_weights.size())
    {
        answer++;
        
        int tmp = truck_weights[idx];
        
        if(q.size() == bridge_length)
        {
            sum -= q.front();
            q.pop();
        }
        
        if(sum + tmp <= weight)
        {
            q.push(tmp);
            sum += tmp;
            idx++;
        }
        else
        {
            q.push(0);
        }
    }
    
    return answer + bridge_length;
}