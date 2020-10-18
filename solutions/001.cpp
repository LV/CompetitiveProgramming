#include <iostream>
using namespace std;

int main() {
	int max = 1000;
	int sum = 0;

	for(int i = 1; i < max; ++i) {
		if((i % 3 == 0) || (i % 5 == 0)) {
			sum += i;
		}
	}

	cout << sum << endl;
}
