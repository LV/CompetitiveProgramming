#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

int main() {
	int max = 2000000;
	int limit = int(sqrt(max)) + 1;

	vector<int> primes;
	primes.push_back(2);
	primes.push_back(3);
	primes.push_back(5);

	int x = 7;

	while(x <= max) {
		int loopLimit = int(sqrt(x)) + 1;
		int i = 1; // skip processing the number 2
		bool pastLimit = false;

		while(!pastLimit) {
			int curr = primes.at(i);
			if(x % curr == 0) break;
			if(curr > loopLimit) {
				primes.push_back(x);
				pastLimit = true;
			}
			++i;
		}
		x += 2;
	}

	long long int sum = 0;
	for(int i = 0; i < primes.size(); ++i) sum += primes.at(i);


	cout << sum << endl; // 142913828922
}
