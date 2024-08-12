/**
 * @file repetitions.cpp
 * @author Luis Victoria
 * @date 2024-08-12 14:54:33
 */

#include <bits/stdc++.h>

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);

    std::string inp;
    std::cin >> inp;

    unsigned int max = 0;
    unsigned int count = 0;

    char curr;
    for (char &c : inp) {
        if (c == curr)
            count++;
        else {
            curr = c;
            if (count > max)
                max = count;
            count = 1;
        }
    }

    if (count > max) {
        std::cout << count << "\n";
        return 0;
    }

    std::cout << max << "\n";
}
