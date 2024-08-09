/**
 * @brief Parking
 * @note https://vjudge.net/problem/UVA-11364
 * @note https://github.com/LV/CompetitiveProgramming/blob/master/UVA/UVA-11364/UVA-11364.cpp
 * @author Luis Victoria
 * @date 2024-08-08 21:45
 */

#include <iostream>
#include <limits>
#include <string>
#include <sstream>
#include <vector>

std::vector<int> parseLineToIntsSpecifyingDimensions(const int& dimensions, const std::string& number_line)
{
    std::istringstream stream(number_line);
    std::vector<int> numbers(dimensions);
    int number;
    unsigned int count = 0;

    while (stream >> number)
        numbers[count++] = number;

    return numbers;
}

void solve(std::vector<int>& number_line)
{
    if (number_line.size() == 1) {
        std::cout << 0 << "\n";
        return;
    }

    unsigned int min = std::numeric_limits<unsigned int>::max();
    unsigned int max = 0;

    for (int& i : number_line) {
        if (i < min)
            min = i;

        if (i > max)
            max = i;
    }

    std::cout << (max-min)*2 << "\n";
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int test_cases;
    std::cin >> test_cases;
    std::cin.ignore(); // ignore newline after test_cases

    for (int t = 0; t < test_cases; ++t) {
        int dimensions;
        std::cin >> dimensions;
        std::cin.ignore(); // ignore newline after dimensions

        std::string number_line;
        std::getline(std::cin, number_line);

        std::vector<int> numbers = parseLineToIntsSpecifyingDimensions(dimensions, number_line);
        solve(numbers);
    }

    return 0;
}
