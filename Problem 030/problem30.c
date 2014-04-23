#include <stdlib.h>
#include <stdio.h>
#include <math.h>

/* Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their 
digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of 
fifth powers of their digits. */

int sumFifthPower(long n);

int main (){
	long sum = 0, limit = 325511;
	
	for(int i = 2 ; i < limit ; i++){
		if(sumFifthPower(i)){
			sum += i;
		}
	}
	
	printf("%d\n", sum);	
	
	return 0;
}

int sumFifthPower(long n){
	int sum = 0, tmp = n;
	
	while(tmp > 0){
		sum += pow(tmp%10, 5);
		tmp /= 10;	
	}
	
	return sum == n;
}