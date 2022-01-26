#include<iostream>
using namespace std;	

int F(int x)
{
	return(10-3*x*x);
}

int main()
{
	int a=-1;
	int b=3;
	int n=4;
	int h=(b-a)/n;
	int I=h*(F(a)+F(b)+4*F(a+h)+2*F(a+2*h)+4*F(a+3*h))/3;
	cout<<"Integration is "<<I<<endl;
}
