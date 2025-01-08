#include <bits/stdc++.h>

long long unsigned int getNumber(long long unsigned int y, long long unsigned int x) {
    if (y == 1 && x == 1) return 1;

    long long unsigned int maximum = std::max(y, x);

    bool isClockwise = maximum % 2 == 0;
    long long unsigned int maxNumberInLane = maximum * maximum; // NOTE: `std::pow` gives the wrong answer!
    if (isClockwise) {
        if(y == maximum) return maxNumberInLane - x + 1;
        else return maxNumberInLane - x - x + 1 + y;
    } else {
        if(x == maximum) return maxNumberInLane - y + 1;
        else return maxNumberInLane - y - y + 1 + x;
    }
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);

    long long unsigned int tests;
    std::cin >> tests;

    long long unsigned int y, x;

    for (long long unsigned int i=0; i<tests; i++) {
        std::cin >> y >> x;
        std::cout << getNumber(y, x) << "\n";
    }
}
