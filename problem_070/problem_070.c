#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

long solve(long lim);
void gen_primes(long lim);
void gen_phi(long lim);
bool are_perm(long a, long b);

bool *primes;
float *phi;


int main (void){
	printf("%d\n", solve(10000000));	

	return 0;
}

void gen_primes(long lim){
	primes = malloc(lim * sizeof(primes));

	for(long i = 2 ; i < lim ; i++){
		primes[i] = true;
	}
	
	primes[0] = false;
	primes[1] = false;

	for(long n = 2 ; n < lim ; n++){
		if(primes[n]){
			long k = 2;
			
			while(true){
				long tmp = k * n;

				if(tmp >= lim){
					break;
				}

				primes[tmp] = false;

				k += 1;
			}
		}
	}
}

void gen_phi(long lim){
	phi = malloc(lim * sizeof(phi));

	for(long n = 0 ; n < lim ; n++){
		phi[n] = n;
	}

	for(long p = 2 ; p < lim ; p++){
		if(primes[p]){
			phi[p] = p - 1;

			long k = 2;
			float r = 1 - 1./p;
			while(true){
				long tmp = p * k;
				if(tmp >= lim){
					break;
				}

				phi[tmp] *= r;

				k += 1;
			}
		}
	}
}

long solve(long lim){
	lim += 1;

	gen_primes(lim);
	gen_phi(lim);

	float min_r = 2;
	long min_n = 0;
	for(long n = 2 ; n < lim ; n++){
		float r = n / phi[n];

		if(r < min_r && are_perm(n, (int)phi[n])){
			min_r = r;
			min_n = n;
		}
	}

	return min_n;
}

bool are_perm(long a, long b){
	int l[10] = {0};

	while(a > 0){
		l[a % 10] += 1;
		a /= 10;
	}
	while(b > 0){
		l[b % 10] -= 1;
		b /= 10;
	}

	for(int i = 0 ; i < 10 ; i++){
		if(l[i] != 0){
			return false;
		}
	}

	return true;
}