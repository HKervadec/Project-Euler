#include <stdio.h>
#include <stdlib.h>
#include <math.h>



/*A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written 
as the sum of two abundant numbers.*/

int type(int n);
int divisorSum(int n);
int test(int n, int *tab, int card);


int main(void){
	int limit = 28123;
	int tab[limit], card = 0;
	
	/*Calcul de tout les nombres abondants */
	for(int i = 1 ; i <= limit ; i++){
		if(type(i) == 1){
			tab[card++] = i;
		}
	}
	
	
	int sum = 0;
	
	for(int i = 1 ; i <= limit ; i++){
		if(!test(i, tab, card)){
			// printf("%d\n", i);
			sum += i;
		}
	}
	
	
	printf("%d\n", sum);
	
	return 0;
}


int divisorSum(int n){
	int sum = 1, tmp = 0;
	int lim = sqrt(n);
	
	for(int i = 2 ; i <= lim ; i++){
		if(!(n % i)){
			sum += i;
			
			tmp = n/i;
			if(tmp != i){
				sum += tmp;
			}
		}
	}
	
	return sum;
}


/**	Deficient : -1
	perfect : 0
	abundant : 1*/
int type(int n){
	int sumDiv = divisorSum(n);
	
	if(sumDiv < n)
		return -1;
	if(sumDiv == n)
		return 0;
		
	// printf("%d: %d\n", n, sumDiv);
	return 1;
}


/**Teste si l'entier n est la somme de deux nombres abondants*/
int test(int n, int *tab, int card){
	int i = 0, j = card - 1, tmp = 0;
	// printf("%d %d %d\n", i, j, length);
	
	if(n <= tab[0])
		return 0;
	
	while(i <= j){
		tmp = tab[i] + tab[j];
	
		if(tmp == n){
			// printf("%d = %d + %d\n", n, tab[i], tab[j]);
			// printf("%d %d\n", i, j);
			return 1;
		}else if(tmp > n){
			j--;
		}else{ 
			i++;
		}
	}
	
	return 0;
}