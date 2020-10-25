#include <iostream>
#include <math.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int a;
	cin >> a;

	cout << "The largest square has side length " << int(sqrt(a)) << "." << endl;
}
