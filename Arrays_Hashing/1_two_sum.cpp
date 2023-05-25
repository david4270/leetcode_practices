//1. Two Sum - easy - https://leetcode.com/problems/two-sum/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector <int> toReturn;
        for(int i = 0; i < nums.size(); i++){
            for(int j = i+1; j < nums.size(); j++){
                if(nums[i] + nums[j] == target){
                    toReturn.push_back(i);
                    toReturn.push_back(j);
                    return toReturn;
                    
                } 
            }
        }
        return toReturn;
    }
};