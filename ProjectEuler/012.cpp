#include <iostream>
#include <math.h>

using namespace std;

int triangle(int i) {
	int sum = 0;
	for(int j=i; j>0; j--) sum+=j;
	return sum;
}

int divisors(int i) {
	int limit = int(sqrt(i)+1);
	int count = 0;
	for(int j=1; j<limit; j++) {
		if(i % j == 0) count += 2;
	}
	return count;
}




int main() {
	bool found = false;
	long long int i = 1;
	while(!found) {
		long long int num = triangle(i);
		if(divisors(num) > 500) {
			cout << num << endl; // 76576500
			found = true;
			break;
		}
		++i;
	}
}
