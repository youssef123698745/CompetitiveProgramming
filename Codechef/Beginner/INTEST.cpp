#include <bits/stdc++.h>

using namespace std ;

void solve(){
	int a,b;
	int count = 0 ;
	cin >> a >> b;
	for(int i=0; i<a; i++){
		int n;
		cin >> n;
		if(n%b == 0){
			count  = count + 1;
		}
	}
	cout << count << "\n";
}

int main(){
	solve();
	return 0;
}
