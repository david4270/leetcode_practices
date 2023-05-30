// 739. Daily Temperatures - Medium - https://leetcode.com/problems/daily-temperatures/description/

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int tempSize = temperatures.size();
        vector<pair<int,int>> tempStack;
        vector<int> result(tempSize);
        int currDay, prevDay, currTemp;
        for(size_t i = 0; i< tempSize; i++){
            currDay = i;
            currTemp = temperatures[i];
            
            while(!tempStack.empty() && tempStack.back().second < currTemp){
                prevDay = tempStack.back().first;
                tempStack.pop_back();

                result[prevDay] = currDay - prevDay;
            }
            tempStack.push_back({currDay, currTemp});
        }
        return result;
    }
};