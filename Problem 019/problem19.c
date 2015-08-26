#include <stdio.h>
#include <stdlib.h>

// You are given the following information, but you may prefer to do some research for yourself.

    // 1 Jan 1900 was a Monday.
    // Thirty days has September,
    // April, June and November.
    // All the rest have thirty-one,
    // Saving February alone,
    // Which has twenty-eight, rain or shine.
    // And on leap years, twenty-nine.
    // A leap year occurs on any year evenly divisible by 4, but not on a century unless it is 
	// divisible by 400.

// How many Sundays fell on the first of the month during the twentieth century 
// (1 Jan 1901 to 31 Dec 2000)?

void nextDayWeek(int *n);
void nextDay(int *day, int *month, int *year);
int leapYear(int year);
void printDay(int dayWeek, int day, int month, int year);

int monthLength[] = {31,28,31,30,31,30,31,31,30,31,30,31};
char *jour[] = {"lundi", "mardi", "mercredi", "jeudi", "vendred", "samedi", "dimanche"};
char *mois[] = {"janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout"
				, "septembre", "octobre", "novembre", "decembre"};
	
				
int main(void){
	int dayMonth = 1;
	int dayWeek = 1;
	int month = 1;
	int year = 1901;
	
	int counter = 0;
	
	while(year < 2001){
		if(dayMonth == 1 && dayWeek == 7){
			counter++;
		}
		nextDayWeek(&dayWeek);
		nextDay(&dayMonth, &month, &year);
		// printDay(dayWeek, dayMonth, month, year);
	}
	
	printf("Result: %d\n", counter);
	
	return 0;
}

void nextDayWeek(int *n){
	if(*n >= 7){
		*n = 1;
	}
	else{
		(*n)++;
	}
}

void nextDay(int *day, int *month, int *year){
	if(*month != 2){
		if(*day < monthLength[*month - 1]){
			(*day)++;
		}
		else{
			*day = 1;
			
			if(*month == 12){
				*month = 1;
				(*year)++;
			}
			else{
				(*month)++;
			}
		}
	}
	else{
		if(*day < (monthLength[2] + leapYear(*year))){
			(*day)++;
		}
		else{
			*day = 1;
			(*month)++;
		}
	}
}

int leapYear(int year){
	if(!(year%400))
		return 1;
	
	if(!(year%4) && year%100)
		return 1;
		
	return 0;
}

void printDay(int dayWeek, int day, int month, int year){
	printf("%s %d %s %d\n", jour[dayWeek - 1], day, mois[month - 1], year);
}
