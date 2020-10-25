#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int a, e;
	cin >> a >> e;

	if((a>=3) && (e<=4)) {
		cout << "TroyMartian" << endl;
	}

	if((a<=6) && (e>=2)) {
		cout << "VladSaturnian" << endl;
	}

	if((a<=2) && (e<=3)) {
		cout << "GraemeMercurian" << endl;
	}
}
