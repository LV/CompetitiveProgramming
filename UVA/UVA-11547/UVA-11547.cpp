/**
 * @brief Automatic Answer
 * @note https://vjudge.net/problem/UVA-11547
 * @note https://github.com/LV/CompetitiveProgramming/blob/master/UVA/UVA-11547/UVA-11547.cpp
 * @author Luis Victoria
 * @date 2024-08-08 23:23
 */

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

void solve(int num)
{

    num *= 567;
    num /= 9;
    num += 7492;
    num *= 235;
    num /= 47;
    num -= 498;

    num = num % 100 / 10;

    std::cout << num << "\n";
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    unsigned int test_cases;
    std::cin >> test_cases;

    while (test_cases--) {
        int num;
        std::cin >> num;

        solve(num);
    }

    return 0;
}
