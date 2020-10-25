#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

int main() {
	int max = 20;
	bool found = false;
	int curr = max;
	
	while(!found) {
		for(int i = 1; i <= max; ++i) {
			if(curr % i != 0) break;
			if(i == max) found = true;
		}

		if(!found) curr += max;
	}

	cout << curr << endl; // 232792560
}
