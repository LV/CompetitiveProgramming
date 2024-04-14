// @leet start
class Solution {
public:
    bool isValidChar(char c) {
        const int a = int(c); // ASCII value of char

        // check char is either lower case, upper case, or number
        return (a>=97 && a<=122) || (a>=65 && a<=90) || (a>=48 && a<=57);
    }

    string processString(string s) {
        string result = "";
        for(int i=0; i<s.size(); i++) if(isValidChar(s[i])) result.push_back(tolower(s[i]));
        return result;
    }

    bool isPalindrome(string s) {
        string postProcessedStr = processString(s);

        const int ppSize = postProcessedStr.size();

        for(int i=0; i<ppSize; i++) {
            int altIndex = ppSize-1-i;
            if(postProcessedStr[i] != postProcessedStr[altIndex]) return false;
        }
        return true;
    }
};
// @leet end
