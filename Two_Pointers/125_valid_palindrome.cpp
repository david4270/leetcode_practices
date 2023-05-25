// 125. Valid Palindrome - Easy - https://leetcode.com/problems/valid-palindrome/

#include <string>
class Solution {
public:
    bool isPalindrome(string s) {
        string str;
        for(int i = 0; i < s.size(); i++){
            if(isalnum(s[i])){
                str += tolower(s[i]);
            }
        }
        for(int i = 0; i < str.size()/2; i++){
            if(str[i] != str[str.size()-i-1]){
                return false;
            }
        }
        return true;
    }
};