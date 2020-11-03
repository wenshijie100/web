#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
char s[100];
int a[100];
int len=0;
int find_x(int start,int j){
	while(s[start]!=':'){
		start=start+j;		
	} 
	return start;
}
int find_y(int start,int j){
	while(s[start]!=' '){
		start=start+j;		
	} 
	return start;
}
int main(){
	freopen("C:\\Users\\wensh.LAPTOP-GCSCJA7R\\Desktop\\web\\plaintxt_yahoo.txt","r",stdin);
	freopen("C:\\Users\\wensh.LAPTOP-GCSCJA7R\\Desktop\\web\\yahoo_input.txt","w",stdout);
	int cnt=0;
	/*while(scanf("%s%s%s%s%s",s[1],s[2],s[3],s[4],s[5])){
		//cnt++;
		printf("%s %s %s %s %s\n",s[1],s[2],s[3],s[4],s[5]);
		//if(cnt>100000) break;;
	}*/

	while(gets(s)){
		len=strlen(s);
	//	printf("%s\n",s);
		a[1]=find_x(0,1);
	//	printf("A:%d\n",a[1]);
	//	system("pause");
		a[2]=a[1]+1;
		a[4]=find_x(a[2],1);
		a[3]=a[4]-1;
		/*for(int i=0;i<a[1];i++){
			printf("%c",s[i]);
		}
		printf("#########");
		*/
		for(int i=a[4]+1;i<len;i++){
			printf("%c",s[i]);
		}
		/*printf("#########");
		for(int i=a[2];i<=a[3];i++){
			printf("%c",s[i]);
		}
		*/
		printf("\n");
		
		cnt++;
		//if(cnt>10000000	) break;
		
	}
	return 0;
} 
