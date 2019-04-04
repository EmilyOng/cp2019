#include <iostream>
#include <algorithm>
#include <vector>
#define ll long long
#define INF 1000000000
using namespace std;
int main(){
    int a;cin>>a;
    for (int i=0; i<a; i++){
		int n,p;cin>>n>>p;
		vector<int>s; int x;
		for (int i=0; i<n; i++){
			cin>>x;
			s.push_back(x);
		}
		int best=INF,sum=0;
		sort(s.begin(),s.end(),greater<int>());
		for (int i=0; i<p; i++){
			sum+=s[i];
		}
		best=min(best,s[0]*p-sum);
		for (int i=1; i<n; i++){
			if(i+p-1==n){break;}
			sum-=s[i-1];
			sum+=s[i+p-1];
			best=min(best,s[i]*p-sum);
		}
		cout<<"Case #"<<i+1<<": "<<best<<endl;
		best=INF;
	}
}
