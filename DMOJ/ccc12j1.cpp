#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int l, c;
	cin >> l >> c;

	int diff = c - l;

	if(diff<=0) {
		cout << "Congratulations, you are within the speed limit!" << endl;
	} else {
		int f;
		if((diff>=1) && (diff<=20)) {
			f = 100;
		} else if((diff>=21) && (diff<=30)) {
			f = 270;
		} else {
			f = 500;
		}

		cout << "You are speeding and your fine is $" << f << "." << endl;
	}
}
