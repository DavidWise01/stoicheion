#include <iostream>
#include <fstream>
#include <cstdint>
using namespace std;
int64_t F[6][6]={{-468782,15168,178351,37872,462988,-183661},{15168,-223516,37502,26866,171889,-5384},{178351,37502,-853828,127821,16760,-649137},{37872,26866,127821,-284676,-548007,264413},{462988,171889,16760,-548007,-1535486,732055},{-183661,-5384,-649137,264413,732055,-1047292}};
int main(int argc,char **argv){if(argc!=2)return 2;ifstream f(argv[1]);int64_t total=0,found=0;int t,lo[5],hi[5];while(f>>t){for(int i=0;i<5;i++)f>>lo[i]>>hi[i];for(int a=lo[0];a<=hi[0];a++)for(int b=lo[1];b<=hi[1];b++)for(int c=lo[2];c<=hi[2];c++)for(int d=lo[3];d<=hi[3];d++)for(int e=lo[4];e<=hi[4];e++){
int64_t x[6]={a,b,c,t,d,e};int64_t q=0;for(int i=0;i<6;i++){q+=F[i][i]*x[i]*x[i];for(int j=i+1;j<6;j++)q+=2*F[i][j]*x[i]*x[j];}total++;if(q==-2){found++;cout<<"ROOT";for(int i=0;i<6;i++)cout<<" "<<x[i];cout<<"\n";}}
}cout<<"CERTIFIED_CASES "<<total<<" ROOT_COUNT "<<found<<"\n";}