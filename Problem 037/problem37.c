#include <stdlib.h>
#include <stdio.h>
#include <math.h>

/* The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each 
stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left 
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes. */

long removeRight(long n);
long removeLeft(long n);
long pow2(long x, int n);
int prime(long n);
int primeSens(long (*remove)(long n), long n);


int main(void){
	long (*right)(long), (*left)(long);
	right = &removeRight;
	left = &removeLeft;
	
	
	int counter = 0, max = 11;
	long start = 11, sum = 0, i = start;
	
	while(counter < max){
		if(primeSens(right, i) && primeSens(left, i)){
			// printf("%d, %d\n", i, counter);
			counter++;
			sum += i;
		}
		
		i += 2;
	}
	
	printf("Sum = %d\n", sum); 
	
	return 0;
}


long removeRight(long n){
	return n/10;
}


long removeLeft(long n){
	int numberOfDigits = 0;
	long save = n;
	
	while(save > 10){
		save /= 10;
		numberOfDigits++;
	}
	
	return n - save*pow2(10, numberOfDigits);
}


long pow2(long x, int n){
	long result = 1;
	
	for(int i = 0 ; i < n ; i++){
		result *= x;
	}
	
	return result;
}


int prime(long n){
	if(n < 2 || ( !(n%2) && n != 2 )){
		return 0;
	}
	
	long lim = sqrt(n);
	for(long i = 3 ; i <= lim ; i += 2){
		if(!(n%i)){
			return 0;
		}
	}
	
	return 1;
}


int primeSens(long (*remove)(long n), long n){
	while(n > 0){
		if(!prime(n)){
			return 0;
		}
		
		n = (*remove)(n);
	}
	
	return 1;
}