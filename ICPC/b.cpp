#include <bits/stdc++.h>
using namespace std;

int main(){

	int test;
	cin >> test;

	for (int i = 0; i < test; i++)
	{

		long long int p, q;
		string in;

		cin >> in;
		cin >> p >> q;
		long long int N[q];
		long long int count[26] = {0};

		for (int j = 0; j<q; j++){
			cin >> N[j];
		}

		for (int j = 0; j<in.length(); j++){
			count[in[j] - 'a']++;
		}

		string final;
		char alphabet[27] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
		long long int fin[26] = {0};
		fin[0] = count[0]*p;
		/*
		for (int j = 1; j<26; j++){
			fin[j] = fin[j-1] + p*count[j];
			//cout << fin[j] << endl;
		}

		*/
		for(int j = 0; j<26; j++){
			string temp(count[j]*p, alphabet[j]);
			//cout << temp << endl;
			final += temp;
			//cout << final<<endl;
		}

		//cout << final;
		//long long int len = p*in.length();
		long long int len = final.length();
		for (int j= 0; j<q; j++){
			if (N[j] > len){
				cout << -1 << endl;
			}
			else{
				/*
				int k = 0;
				for(k = 0; k<26; k++)
				{
					if (fin[k] >= N[j]){
						//cout << fin[k] << N[j];
						break;
					}
				}	
				cout << alphabet[k] << endl;
				*/
				cout << final[N[j] - 1] << endl;
			}
		}
		
	}
	return 0;

}