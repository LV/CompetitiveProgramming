#include <bits/stdc++.h>
#include <fstream>


int main() {
    std::ifstream fin("paint.in");
    std::ofstream fout("paint.out");

    int a, b, c, d;
    fin >> a >> b >> c >> d;

    if ((a<=c && c<=b) || (c<=a && a<=d))
        fout << std::max(d-a, std::max(b-c, std::max(b-a, d-c)));
    else
        fout << (b-a) + (d-c);
}
