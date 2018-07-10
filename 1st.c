#include <stdio.h>
#include <string.h>
 
int main()
{
  	char S[100], RevS[100];
  	int i, j, len;
 
  	printf("\n Please Enter any String :  ");
  	gets(S);
  	
  	j = 0;
  	len = strlen(S);
 
  	for (i = len - 1; i >= 0; i--)
  	{
  		RevS[j++] = S[i];
  	}
  	RevS[i] = '\0';
 
  	printf("\n String after Reversing = %s", RevS);
  	
  	return 0;
}
