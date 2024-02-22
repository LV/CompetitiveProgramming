#include <bits/stdc++.h>
#include <bitset>

int main() {
    // Read input
    int n;
    std::cin >> n;

    // Extract final bit; must be divisible by two
    int finalBit = n & 0b1;

    if(n!=2 && finalBit==0b0) std::cout << "YES\n";
    else std::cout << "NO\n";

    return 0;
}
