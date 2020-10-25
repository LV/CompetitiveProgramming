#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

int main() {
	long int max = 600851475143;
	long int limit = sqrt(max) + 1;
	vector<int> primes;

	while(true) {
		for(int i = 2; i <= limit; ++i) {
			if(max % i == 0) {
				max = max / i;
				primes.push_back(i);
				break;
			}
		}
		
		sort(primes.begin(), primes.end());
		if(max <= primes.back()) break;
	}

	cout << primes.back() << endl; // 6857
}
