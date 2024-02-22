#include <iostream>
#include <string>

bool isValidBound(int n) {
    return n>=1 && n<=100;
}

int main() {
    // Read input
    int n;
    std::cin >> n;
    if(!isValidBound(n)) return -1;

    for(int i=0; i<n; i++) {
        std::string word;
        std::cin >> word;
        if(word.length() <= 10) std::cout << word << std::endl;
        else std::cout << word[0] << word.length()-2 << word[word.length()-1] << std::endl;
    }
 
    return 0;
}
