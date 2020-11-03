#include<cstdio>
#include<cstring>
using namespace std;
char s[100];
int a[100];
int len=0;
int find_x(int start,int j){
	while(s[start]==' '||s[start]=='#'){
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
	freopen("C:\\Users\\wensh.LAPTOP-GCSCJA7R\\Desktop\\web\\www.csdn.net.txt","r",stdin);
	freopen("C:\\Users\\wensh.LAPTOP-GCSCJA7R\\Desktop\\web\\csdn_input.txt","w",stdout);
	int cnt=0;
	/*while(scanf("%s%s%s%s%s",s[1],s[2],s[3],s[4],s[5])){
		//cnt++;
		printf("%s %s %s %s %s\n",s[1],s[2],s[3],s[4],s[5]);
		//if(cnt>100000) break;;
	}*/
	int flag=0; 
	while(gets(s)){
		if(flag==0){
			 flag=1;
			 continue ; 
		} 
		len=strlen(s);
		a[1]=find_y(0,1);
		a[2]=find_x(a[1],1);
		a[4]=find_y(len-1,-1);
		a[3]=find_x(a[4],-1);
		/*for(int i=0;i<a[1];i++){
			printf("%c",s[i]);
		}
		//printf("#########");
		printf(" "); 
		*/
		for(int i=a[2];i<=a[3];i++){
			printf("%c",s[i]);
		}
		//printf("#########");	
		/*printf(" ");
		for(int i=a[4]+1;i<len;i++){
			printf("%c",s[i]);
		}
		*/
		printf("\n");
		cnt++;
		//if(cnt>100000) break;
		
	}
	return 0;
} 
