#include <iostream>
#include <string>

bool isValidBound(int n) {
    return n>=1 && n<=1000;
}

int main() {
    int n;
    std::cin >> n;
    if(!isValidBound(n)) return -1;

    int count=0;

    for(int i=0; i<n; i++) {
        int x, y, z;
        std::cin >> x;
        std::cin >> y;
        std::cin >> z;
        if((x+y+z)>=2) count++;
    }
    std::cout << count << std::endl;
    return 0;
}
