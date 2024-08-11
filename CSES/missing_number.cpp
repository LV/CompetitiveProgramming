/**
 * @file missing_number.cpp
 * @author Luis Victoria
 * @date 2024-08-11 17:47:16
 */

#include <bits/stdc++.h>

int main()
{
    unsigned long long amount;
    std::cin >> amount;

    unsigned long long total = 0;
    unsigned long long curr;

    for (unsigned long long i = 0; i < amount-1; i++) {
        std::cin >> curr;
        total += curr;
    }

    unsigned long long arithmetic_sum = (amount * (amount + 1)) / 2;

    std::cout << arithmetic_sum - total << "\n";
}
