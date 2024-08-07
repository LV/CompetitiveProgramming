/**
 * @brief Combination Lock
 * @note https://vjudge.net/problem/UVA-10550
 * @note https://github.com/LV/CompetitiveProgramming/blob/master/UVA/UVA-10550.cpp
 * @author Luis Victoria
 * @date 2024-08-06 22:54:16
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

const int FULL = 360;
const int MARKS = 40;
const int UNIT = (FULL / MARKS);

int clockwise(int from, int to)
{
    int diff = to - from;

    if (diff < 0)
        return (MARKS + diff) * UNIT;
    else
        return diff * UNIT;
}

int counterclockwise(int from, int to)
{
    int diff = to - from;

    if (diff < 0)
        return -diff * UNIT;
    else
        return (MARKS - diff) * UNIT;
}

void solve()
{
    std::string line;

    while (std::getline(std::cin, line)) {
        std::vector<int> numbers = parseLineToInts(line);

        int count = 0;
        count += FULL * 2; // 2 full clockwise turns
        count += clockwise(numbers[0], numbers[1]);
        count += FULL; // 1 full counter clockwise turn
        count += counterclockwise(numbers[1], numbers[2]);
        count += clockwise(numbers[2], numbers[3]);

        std::cout << count << "\n";
    }
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    solve();

    return 0;
}
