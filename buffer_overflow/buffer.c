#include <stdio.h>
#include <string.h>

int main (int argc, char*argv[])
{
	int naoacessa = 0;
	char buff[8];
	printf("variavel = %s\n",naoacessa);
	strcpy(buff, argv[1]);

	if(naoacessa == 0){
		printf("acesso negado\n");
	}else{
		printf("variavel = %c\n",naoacessa);
		printf("acessou\n");
		
	}
	return 0;
}
