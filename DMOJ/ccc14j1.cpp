#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int a, b, c;
	cin >> a >> b >> c;

	if((a+b+c) != 180) {
		cout << "Error" << endl;
	} else if((a == b) && (a == c) && (b == c)) {
		cout << "Equilateral" << endl;
	} else if((a != b) && (a != c) && (b != c)) {
		cout << "Scalene" << endl;
	} else {
		cout << "Isosceles" << endl;
	}
}
