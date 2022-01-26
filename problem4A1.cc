#include<iostream>
#include<chrono>
using namespace std;

int main()
{
int n;
cout<<"Enter number of position of element required "<<endl;	
cin>>n;
int fib[n];
fib[0]=0;
fib[1]=1;
chrono::time_point<std::chrono::high_resolution_clock> begin, end;
begin=chrono::high_resolution_clock::now();
for(int i=2;i<n+1;i++)
{
	fib[i]=fib[i-1]+fib[i-2];
}
end=chrono::high_resolution_clock::now();
cout<<fib[n]<<endl;
chrono::duration<double> diff=end-begin;
cout<<"Duration is given by"<<diff.count()<<"seconds";
}//n is representing here index of Fibonacci series i.e. (n+1)th element of series
