#ifndef PRIME
#define PRIME

int prime(long n);

typedef struct PrimeList{
	long *list;
	int i;
	int size;
} PrimeList;

PrimeList *init_p(int size);
void del_p(PrimeList *pl);
void add_p(PrimeList *pl, long n);

#endif