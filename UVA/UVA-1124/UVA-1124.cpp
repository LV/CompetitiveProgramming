/**
 * @file UVA-1124.cpp
 * @brief Celebrity Jeopardy
 * @note https://vjudge.net/problem/UVA-1124
 * @note https://github.com/LV/CompetitiveProgramming/blob/master/UVA/UVA-1124/UVA-1124.cpp
 * @author Luis Victoria
 * @date 2024-08-06 22:28:35
 */

#include <iostream>
#include <string>

void solve()
{
    std::string line;

    while (std::getline(std::cin, line)) {
        for (char &ch : line)
            std::cout << ch;
        std::cout << "\n";
    }
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    solve();

    return 0;
}

