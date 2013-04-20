#include <stdlib.h>
#include <stdio.h>

/*145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.*/

long factorial(int n);
int equals(unsigned long long n, int* factorielles);


int main(){
	int factorielles[10] = {0};
	
	for(int i = 0 ; i < 10 ; i++){
		factorielles[i] = factorial(i);
	}
	
	unsigned long long sum = 0;
	for(unsigned long long i = 3 ; i <= 2310000 ; i++){
		if(equals(i,factorielles)){
			sum += i;
		}
	}

	printf("%llu\n", sum);

	return 0;
}


long factorial(int n){
	if(n < 2){
		return 1;
	}
	
	return n*factorial(n-1);
}


int equals(unsigned long long n, int* factorielles){
	unsigned long long sum = 0, tmp = n;
	
	while(tmp > 0){
		if(sum > n){
			return 0;
		}
		sum += factorielles[tmp%10];
		tmp /= 10;
	}
	
	return sum == n;
}