#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
	int t;cin>>t;
	for (int tc=0; tc<t; tc++){
		int r,c;cin>>r>>c;
		string s;
		int arr[r][c];
		int sum_i=0,sum_j=0,counter=0;
		vector<pair<int,int> >v;
		for (int i=0; i<r; i++){
			cin>>s;
			for (int j=0; j<c; j++){
				arr[i][j]=s[j]-'0';
				if (s[j]-'0'==1){
					counter++;
					sum_i+=i+1;
					sum_j+=j+1;
					v.push_back(make_pair(i+1,j+1));
				}
			}
		}
		sum_i/=counter;sum_j/=counter;
		arr[sum_i-1][sum_j-1]=1;
		v.push_back(make_pair(sum_i,sum_j));
		int best=1000000000,ans=0;
		for (int i=0; i<r; i++){
			for (int j=0; j<c; j++){
				if(arr[i][j]==0){
					best=1000000000;
					for (int k=0; k<(int)v.size(); k++){
						best=min(best,abs(i+1-v[k].first)+abs(j+1-v[k].second));
					}
					ans=max(ans,best);
				}
			}
		}
		cout<<"Case #"<<tc+1<<": "<<ans<<endl;
	}
}
// |r1 - r2| + |c1 - c2|
