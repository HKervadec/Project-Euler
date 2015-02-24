#include <stdio.h>
#include <stdlib.h>

/*The following iterative sequence is defined for the set of positive 
integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
Using the rule above and starting with 13, we generate the following sequence:

It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

unsigned long long next(unsigned long long n);
long chain(unsigned long long start);

int main()
{
    printf("Euler 14\n");

    long max = 0, startingMax = 0, length = 0;

    for(long i = 1 ; i <= 1000000 ; i++){
        length = chain(i);

        if(length > max){
            max = length;
			startingMax = i;
        }
    }
	
	printf("%d\n", startingMax);

    return 0;
}


long chain(unsigned long long start){
	long length = 1;

    while(start != 1){
        //printf("Start: %d| Length: %d\n", start, length);
        start = next(start);
        length++;
    }

    return length;
}

unsigned long long next(unsigned long long n){
    if(!(n % 2)){
        return n / 2;
    }

    return 3*n + 1;
}
