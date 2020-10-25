#include <iostream>
#include <math.h>

using namespace std;

int pythagoras(int a, int b) {
	return int(sqrt((a * a) + (b * b)));
}

bool isPythagoreanTriplet(int a, int b, int c) {
	int total = (a * a) + (b * b);
	int cSquare = c * c;
	return total == cSquare;
}

int main() {
	for(int b = 1; b < 1000; ++b) {
		for(int a = 1; a < b; ++a) {
			int c = pythagoras(a, b);
			if(isPythagoreanTriplet(a, b, c) && (a + b + c == 1000)) {
				int product = a * b * c;
				cout << product << endl; // 31875000
				break;
			}
		}
	}
}
