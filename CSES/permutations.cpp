#include <bits/stdc++.h>

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);

    int inp;
    std::cin >> inp;

    if (inp == 1) std::cout << "1";
    else if (inp <= 3) std::cout << "NO SOLUTION";
    else {
        int next = inp;
        if (inp % 2 == 0) inp -= 1;
        else next -= 1;
        for (; inp >= 1; inp -= 2) std::cout << inp << " ";
        inp = next;
        for (; inp >= 2; inp -= 2) std::cout << inp << " ";
    }
}
