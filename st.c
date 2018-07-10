#include <stdio.h>
#include <string.h>
 
void main()
{
  	char S[100], revS[100];
  	int i, j, len;
 
  	gets(S);
  	
  	j = 0;
  	len = strlen(S);
 
  	for (i = len - 1; i >= 0; i--)
  	{
  		revS[j++] = S[i];
  	}
  	revS[i] = '\0';
 
  	printf("%s", revS);
  
}
