/**
 * @file increasing_array.cpp
 * @author Luis Victoria
 * @date 2024-08-12 15:14:34
 */

#include <bits/stdc++.h>

int main()
{
    std::cin.tie(0)->sync_with_stdio(0);

    size_t inp;
    std::cin >> inp;

    size_t prev;
    size_t curr;
    std::cin >> prev;

    size_t sum = 0;

    for (size_t i = 1; i < inp; i++) {
        std::cin >> curr;

        if (curr < prev) {
            sum += prev - curr;
            curr = prev;
        }

        prev = curr;
    }

    std::cout << sum << "\n";
}
