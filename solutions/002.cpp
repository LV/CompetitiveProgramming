#include <iostream>
using namespace std;

int main() {
	int prev, curr, next;

	int sum = 0;

	prev = 1;
	curr = 2;
	next = 0;

	while(curr < 4000000) {
		next = prev + curr;

		if(curr % 2 == 0) sum += curr;
		
		prev = curr;
		curr = next;
	}

	cout << sum << endl; // 4613732
}
