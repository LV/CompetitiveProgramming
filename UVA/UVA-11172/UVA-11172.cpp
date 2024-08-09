/**
 * @brief Relational Operator
 * @note https://vjudge.net/problem/UVA-11172
 * @note https://github.com/LV/CompetitiveProgramming/blob/master/UVA/UVA-11172/UVA-11172.cpp
 * @author Luis Victoria
 * @date 2024-08-08 00:41
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
    std::vector<int> input_line = parseLineToInts(line);

    if (input_line[0] < input_line[1])
        std::cout << "<" << "\n";

    else if (input_line[0] > input_line[1])
        std::cout << ">" << "\n";

    else
        std::cout << "=" << "\n";
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
