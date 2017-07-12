#include <bits/stdc++.h>
using namespace std;

struct node
{
	int value;
	node *left, *right;

	node(int value, node *left, node *right):
		value(value), left(left), right(right) {}

	node* insert(int l, int r, int val, int idx);
	int get(int start, int end, int l, int r);
};

node *null = new node(0, NULL, NULL);

node * node::insert(int l, int r, int val, int idx)
{
	if(l <= idx && idx <= r)
	{
		if(l == r)
			return new node(this->value^val, null, null);

		int m = (l+r)>>1;
		if (m < idx)
			return new node(this->value^val, this->left, this->right->insert(m+1, r, val, idx));	
		
		else
			return new node(this->value^val, this->left->insert(l, m, val, idx), this->right);
	}
    return this;
}

int node::get(int start, int end, int l, int r)
{
	if (r < start || end < l)
		return 0;

	if (l <= start && end <= r)
		return this->value;

	int m = (start + end)>>1;
	return (this->left->get(start, m, l, r) ^ this->right->get(m+1, end, l, r));

}

void dfs(node* root[], map<int, int> tree[], map<int, int> hash, int maxi, int N)
{
	stack<int> nodes;
	nodes.push(1);
	int pa[N];
	int explored[N] = {0};
	pa[1] = 0;
	while (!nodes.empty())
	{
		int u = nodes.top();
		nodes.pop();
		if (explored[u] == 0)
		{
			if (u == 1)
				root[u] = null;

			else
				root[u] = (root[pa[u]])->insert(0, maxi, tree[u][pa[u]], hash[tree[u][pa[u]]]);
			
			explored[u] = 1;
			for( map <int, int > :: iterator it = tree[u].begin(); it != tree[u].end(); it++ )
		    	if (explored[it->first] == 0)
				{
					pa[it->first] = u;
					nodes.push(it->first);
				}
		}
	}
}

int main()
{
	int tt;
	scanf("%d", &tt);
	null->left = null->right = null;
	while(tt--)
	{
		int n;
		scanf("%d", &n);
		map<int, int> tree[n+1];
		map <int, int> hash;
		vector <int> weight;
		for(int i = 0; i < n-1; i++)
		{
			int u, v, c;
			scanf("%d %d %d", &u, &v, &c);
			tree[u][v] = c;
			tree[v][u] = c;
			hash[c];
		}
		int high = 0;
		for( map <int, int > :: iterator it = hash.begin(); it != hash.end(); it++ )
		{
			hash[it->first] = high;
			weight.push_back(it->first);
			high += 1;
		}

		node * root[n+1];
		dfs(root, tree, hash, high-1, n+1);
		
		int m;
		scanf("%d", &m);
		while(m--)
		{
			int u, v, k;
			scanf("%d %d %d", &u, &v, &k);
    		int lo = 0;
			int hi = high;
			while (lo < hi)
			{
        		int mid = (lo+hi)/2;
        		if (weight[mid] < k)
					lo = mid+1;

        		else
					hi = mid;
			}
			map <int, int>::iterator it = hash.find(k);
			if (it == hash.end())
				lo --;
			
			if (lo < 0)
			{
				printf("%d\n", 0);
				continue;
			}

			int c1 = root[u]->get(0, high-1, 0, lo);
			int c2 = root[v]->get(0, high-1, 0, lo);
			printf("%d\n", c1 ^ c2);
		}
	}
}