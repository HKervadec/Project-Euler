#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "prime.h"


int prime(long n){
	if(n == 2){
		return 1;
	}

	if(n < 2 || !(n % 2)){
		return 0;
	}

	long lim = sqrt(n);
	for(long i = 3 ; i <= lim ; i+=2){
		if(!(n % i)){
			return 0;
		}
	}

	return 1;
}

PrimeList * init_p(int size){
	PrimeList *pl = malloc(sizeof(PrimeList));
	if(pl == NULL){
		return NULL;
	}

	pl->list = malloc(size * sizeof(long));
	pl->i = 0;
	pl->size = size;

	return pl;
}

void del_p(PrimeList *pl){
	free(pl->list);
	free(pl);
}

void add_p(PrimeList *pl, long n){
	if(pl->i == pl->size){
		pl->size *= 2;
		long *tmp = malloc(pl->size * sizeof(long));

		for(int i = 0 ; i < pl-> i ; i++){
			tmp[i] = pl->list[i];
		}

		free(pl->list);
		pl->list = tmp;
	}

	pl->list[pl->i] = n;
	pl->i++;
}