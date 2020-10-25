#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int a, b, c;
	cin >> a >> b >> c;

	vector<int> list;
	list.push_back(a);
	list.push_back(b);
	list.push_back(c);

	sort(list.begin(), list.end());
	cout << list.at(1) << endl;
}
