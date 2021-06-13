/**
 *    author:  youssef_boumhaout
 *    Platform : Codechef.com
**/

#include <bits/stdc++.h>

using namespace std;
using boost::multiprecision::cpp_int;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
	    int n;
	    cpp_int fact=n;
	    cin>>n;
	    fact=n;
	    for(int j=1;j<n;j++){
	        fact=fact*j;
	    }
	    cout<<fact<<endl;
	}
	return 0;
}
