#include<iostream>
using namespace std;
int main()
{	
	int l,j,n;
	cout<<"Enter length of array";
	cin>>l;
	cout<<"Enter n(for top n values): ";
	cin>>n;
	float arr[l],b,s;
	for(int i=0;i<l;i++)
	{
		cout<<"Enter element no "<<i+1<<" of array"<<endl;
		cin>>arr[i];
		
	}
	for(int t=0;t<n;t++)
	{
		b=arr[t];
		j=t;
		for(int i=t;i<l;i++)
		{
			if(b<arr[i])
			{	
				b=arr[i];
				j=i;
			}
		}
		s=arr[j];
		arr[j]=arr[t];
		arr[t]=s;
	}
	for(int i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}
}
