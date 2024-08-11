/**
 * @file weird_algorithm.cpp
 * @author Luis Victoria
 * @date 2024-08-11 01:55:22
 */

#include <bits/stdc++.h>

int main()
{
    long long n;
    std::cin >> n;

    while(true) {
        std::cout << n<< " ";
        if (n == 1)
            break;
        if (n % 2 == 0)
            n /= 2;
        else
            n = (n*3) + 1;
    }

    std::cout << "\n";
}
