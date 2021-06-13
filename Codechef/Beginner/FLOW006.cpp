/**
 *    author:  youssef_boumhaout
 *    Platform : Codechef.com
**/

#include <iostream>
#include<cmath>

using namespace std;

int main() {
	long int n,sum,num;
	cin>>n;
	
	for(int i=0;i<n;i++)
	{
	    cin>>num;
	    sum=0;
	    int long m=num;
	    while(num!=0)
	    {
	        sum=sum+num%10;
	        num=num/10;
	    }
	    cout<<sum<<endl;
	}
	return 0;
}
