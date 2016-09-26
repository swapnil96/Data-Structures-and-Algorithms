
# include <bits/stdc++.h>
using namespace std;

int main(){

	int test;
	long long int s, e, n;
	cin >> test;
	for(int i =0; i<test; i++){

		cin >> s >> e;
		cin >> n;
		long long int in[n][2];
		for(int j = 0; j<n; j++){
			cin >> in[j][0] >> in[j][1];
		}
		int got = 1;
		for(int j = 0; j<n; j++){
			if ((in[j][0] <= s && in[j][1] <= e) or (in[j][0] >= s && in[j][1] >= e)){
				continue;
			}
			else{
				got = 0;
				break;
			}

		}
		if (got == 1){
			cout << "YES" << endl;
		}
		else{
			cout << "NO" << endl;
		}

	}
	return 0;

}
