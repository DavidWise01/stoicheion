#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
using namespace std;
using i128=__int128;
const long long F[4][4]={
{-17801313208674LL,-15761198498141LL,15135416925109LL,7424607432690LL},
{-15761198498141LL,-18808565513138LL,15151261558975LL,6742605417749LL},
{15135416925109LL,15151261558975LL,-13901548148824LL,-5277176639089LL},
{7424607432690LL,6742605417749LL,-5277176639089LL,-6096520821564LL}};
unsigned __int128 sqr(unsigned __int128 a){
 unsigned __int128 s=(unsigned __int128)sqrtl((long double)a);
 while(s+1<=a/(s+1))++s;
 while(s>a/s)--s;return s;
}
int main(int argc,char**argv){
 if(argc!=2)return 2;
 ifstream f(argv[1]);int t,lo,hi,l1,h1;long long count=0,hits=0;
 while(f>>t>>lo>>hi>>l1>>h1)
 for(int x0=lo;x0<=hi;x0++)for(int x1=l1;x1<=h1;x1++){
  ++count;
  i128 A=F[3][3],B=2*((i128)F[3][0]*x0+(i128)F[3][1]*x1+(i128)F[3][2]*t);
  i128 C=(i128)F[0][0]*x0*x0+(i128)F[1][1]*x1*x1+(i128)F[2][2]*t*t+
  2*((i128)F[0][1]*x0*x1+(i128)F[0][2]*x0*t+(i128)F[1][2]*x1*t)+2;
  i128 d=B*B-4*A*C;
  if(d<0)continue;
  auto root=sqr((unsigned __int128)d);
  if(root*root!=(unsigned __int128)d)continue;
  for(int sg=-1;sg<=1;sg+=2){
   i128 num=-B+(i128)sg*(i128)root;
   if(num%(2*A))continue;
   i128 x3=num/(2*A);
   if(x3>INT64_MAX||x3<INT64_MIN)continue;
   i128 x[4]={x0,x1,t,x3},q=0;
   for(int i=0;i<4;i++)for(int j=0;j<4;j++)q+=x[i]*F[i][j]*x[j];
   if(q!=-2)return 9;
   cout<<"ROOT "<<x0<<" "<<x1<<" "<<t<<" "<<(long long)x3<<"\n";++hits;
  }
 }
 cerr<<"TOTAL "<<count<<" FOUND "<<hits<<"\n";
}
