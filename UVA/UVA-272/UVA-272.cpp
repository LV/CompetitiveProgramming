/**
 * @file UVA-272.cpp
 * @brief TEX Quotes
 * @note https://vjudge.net/problem/UVA-272
 * @note https://github.com/LV/CompetitiveProgramming/blob/master/UVA/UVA-272/UVA-272.cpp
 * @author Luis Victoria
 * @date 2024-08-06 22:24:00
 */

#include <iostream>
#include <string>

void solve()
{
    std::string line;
    bool open_quote = true;

    while (getline(std::cin, line)) {
        for (char &ch : line) {
            if (ch == '"') {
                if (open_quote)
                    std::cout << "``";
                else
                    std::cout << "''";

                open_quote = !open_quote;
            }
            else
                std::cout << ch;
        }
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
