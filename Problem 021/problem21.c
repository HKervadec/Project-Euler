#include <stdio.h>
#include <stdlib.h>
#include <math.h>



/* Let d(n) be defined as the sum of proper divisors of n (numbers less than 
n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and 
each of a and b are 
called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000. */

int d(int n);


int main(void){
	puts("Euler21");
	
	
	int tab[10001];
	tab[0] = 0;
	
	for(int i = 1 ; i <= 10000 ; i++){
		tab[i] = d(i);
	}
	
	
	int sum = 0;
	
	for(int i = 1 ; i <= 10000 ; i++){
		if(tab[i] < 10000 && tab[tab[i]] == i && tab[i] != i){
			// printf("%d %d %d\n", i, tab[i], tab[tab[i]]);
			sum += i;
		}
	}
	
	
	printf("%d\n", sum);

	return 0;
}

int d(int n){
	int root = sqrt(n);
	int sum = 1;
	
	for(int i = 2 ; i <= root ; i++){
		if(!(n % i)){
			sum += i;
			sum += (n / i);
		}
	}

	return sum;
}