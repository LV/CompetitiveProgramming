#include <iostream>
#include <vector>
using namespace std;

int main() {
	int max = 10001;

	vector<int> primes;
	primes.push_back(2);
	primes.push_back(3);

	int x = 5;
	while(primes.size() < max) {
		for(int i = 0; i < primes.size(); ++i) {
			if(x % primes.at(i) == 0) {
				break;
			}

			if(i == (primes.size() - 1)) {
				primes.push_back(x);
				break;
			}
		}
		x += 2;
	}

	cout << primes.back() << endl; // 104743
}
