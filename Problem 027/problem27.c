#include <stdlib.h>
#include <stdio.h>
#include <math.h>


/*Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values 
n = 0 to 39. 
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly 
when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n² - 79n + 1601 was discovered, which 
produces 80 primes for the consecutive values n = 0 to 79. The product of 
the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.*/

int length(int a, int b);
int prime(int n);

int main(){
	// printf("%d\n", length(1,41)); //return 40
	// printf("%d\n", length(-79,1601)); //return 80
	
	int product = 0;
	int max = 0;
	int tmp = 0;
	
	for(int a = -999 ; a <= 999 ; a++){
		for(int b = -999 ; b <= 999 ; b++){
			tmp = length(a,b);
			if(tmp > max){
				max = tmp;
				product = a*b;
			}
		}
	}
	
	printf("%d\n", product);
	
	
	return 0;
}


int length(int a, int b){
	int n = 0;
	int tmp = b;
	
	while(prime(tmp)){
		n++;
		tmp = n*n + a*n + b;
	}
	
	return n;
}

int prime(int n){
	if(n < 2){
		return 0;
	}
	
	int lim = sqrt(n);
	for(int i = 2 ; i <= lim ; i++){
		if(!(n%i)){
			return 0;
		}
	}
	
	return 1;
}