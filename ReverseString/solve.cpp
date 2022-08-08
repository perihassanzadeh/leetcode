#include <iostream>
#include <vector>

class Solution {
public:
    void reverseString(vector<char>& s) {
        vector<char> b;
        
         for(vector<char>::reverse_iterator it = s.rbegin(); it != s.rend(); ++it)
         {
             b.push_back(*it);
         }
        s.clear();
        for(auto it: b)
        {
            s.push_back(it);
        }
    }
};