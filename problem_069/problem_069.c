#include <stdlib.h>
#include <stdio.h>

#include "prime.h"

long solve();
double phi(long n); 

PrimeList *pl;

int main (void){
	printf("%d\n", solve());	

	return 0;
}

long solve(){
	long lim = 1000000;

	pl = init_p(lim / 10);
	if(pl == NULL){
		return -1;
	}

	long max_n = 0;
	double max_r = 0, r = 0;

	for(long n = 2 ; n <= lim ; n++){
		double tmp = phi(n);

		// printf("%d %2.0f\n", n, tmp);

		r = n / tmp;

		if(r > max_r){
			max_r = r;
			max_n = n;
		}
	}

	del_p(pl);

	return max_n;
}

double phi(long n){
	if(prime(n)){
		add_p(pl, n);
		return n - 1;
	}

	double r = n;
	for(int i = 0 ; i < pl->i ; i++){
		long p = pl->list[i];

		if(!(n % p)){
			r *= (1 - 1./p);
			while(!(n % p)){
				n /= p;
			}
		}

		if(n == 1){
			break;
		}
	}

	return r;
}