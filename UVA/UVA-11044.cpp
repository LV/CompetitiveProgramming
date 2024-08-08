/**
 * @brief Searching for Nessy
 * @note https://vjudge.net/problem/UVA-11044
 * @note https://github.com/LV/CompetitiveProgramming/blob/master/UVA/UVA-11044.cpp
 * @author Luis Victoria
 * @date 2024-08-07 19:55:57
 */

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

std::vector<int> parseLineToInts(const std::string& line)
{
    std::istringstream stream(line);
    std::vector<int> numbers;
    int number;

    while (stream >> number)
        numbers.push_back(number);

    return numbers;
}

void solve(std::string& line)
{
    std::vector<int> dimensions = parseLineToInts(line);
    std::cout << int(dimensions[0]/3) * int(dimensions[1]/3) << "\n";
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int test_cases;
    std::cin >> test_cases;
    std::cin.ignore(); // ignore newline
    for (int t = 0; t < test_cases; ++t) {
        std::string line;
        std::getline(std::cin, line);
        solve(line);
    }

    return 0;
}
