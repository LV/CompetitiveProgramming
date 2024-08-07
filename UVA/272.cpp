// TEX Quotes
// https://vjudge.net/problem/UVA-272

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
