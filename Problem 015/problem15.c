#include <stdio.h>
#include <stdlib.h>

// https://projecteuler.net/problem=15

unsigned long long  euler(int n);
unsigned long long  euler2(int x, int y,  int n);


//tres bourrin et pas efficace, se resout a la calculatrice
int main()
{
    printf("Euler15\n");

    int i = 0;
	unsigned long long tmp = 0;
    for(i = 2 ; i <= 20 ; i++){
		tmp = euler(i);
        printf("%2d: %llu\n",i, tmp);
		if(!tmp)
			printf("caca\n");
    }
		
	// printf("%d\n", euler(20));

    return 0;
}

unsigned long long  euler(int  n){
    return euler2(0, 0, n);
}

unsigned long long  euler2(int x, int y,  int n){
    if(x == n || y == n){
        return 1;
    }
    else{
        return euler2(x + 1, y, n) + euler2(x, y + 1, n);
    }
}
