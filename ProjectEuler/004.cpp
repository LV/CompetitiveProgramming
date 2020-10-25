#include <iostream>
#include <math.h>
#include <vector>
#

using namespace std;

bool isPalindrome(long long int x) {
	string first = to_string(x);
	string second = to_string(x);
	reverse(second.begin(), second.end());

	return first == second;
}


int main() {
	long long int max = 0;
	long long int product;

	for(int i = 800; i < 1000; ++i) {
		for(int j = 800; j < 1000; ++j) {
			product = i * j;
			if(isPalindrome(product) && (product > max)) {
				max = product;
			}
		}
	}

	cout << max << endl; // 906609
}
