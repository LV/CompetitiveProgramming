#include <iostream>

using namespace std;

int sumSquare(int x) {
	long long int sum = 0;
	for(int i = 1; i <= x; ++i) sum += (i * i);
	return sum;
}

int squareSum(int x) {
	long long int sum = 0;
	for(int i = 1; i <= x; ++i) sum += i;
	return (sum * sum);
}

int main() {
	int max = 100;

	cout << squareSum(max) - sumSquare(max) << endl; // 25164150
}
