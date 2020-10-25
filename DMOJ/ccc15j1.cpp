#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int m, d;
	cin >> m >> d;

	if(m<2) {
		cout << "Before" << endl;
	} else if(m>2) {
		cout << "After";
	} else {
		if(d<18) {
			cout << "Before" << endl;
		} else if(d>18) {
			cout << "After" << endl;
		} else {
			cout << "Special" << endl;
		}
	}
}
