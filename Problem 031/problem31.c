#include <stdlib.h>
#include <stdio.h>

/* In England the currency is made up of pound, £, and pence, p, 
and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can £2 be made using any number of coins? */

long denombre(int goal, int coin);


const int coinValue[8] = {1, 2, 5, 10, 20, 50, 100, 200};
int memo[199][7] = {0};

int main(){
	int amount = 200;
	
	printf("%d\n", denombre(amount,7));
	
	return 0;
}

long denombre(int goal, int coin){
	int value = coinValue[coin];
	if(goal == 0 || value == 1){
		return 1;
	}
	
	if(memo[goal-2][coin-1]){
		return memo[goal-2][coin-1];
	}
	
	long sum = 0, tmp;
	int max = goal/value;
	for(int i = 0 ; i <= max ; i++){
		sum += denombre(goal - i*value, coin-1);
	}
	
	memo[goal-2][coin-1] = sum;
	return sum;
}