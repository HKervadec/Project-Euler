#include <stdio.h>
#include <stdlib.h>


/*Using names.txt , a 46K text file 
containing over five-thousand first names, begin by sorting it into 
alphabetical order. 
Then working out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain 
a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?*/


int worth(char str[]);
int sup(char str1[], char str2[]);
void permute(char** str, int a, int b);


int main(void){
	/*Affichage des char de 0 a 127 */
	// for(int i = 0 ; i < 128 ; i++){
		// printf("%d: %c\n", i, i);
	// }
	
	FILE* names = NULL;
	names = fopen("names.txt", "r");
	
	if(names == NULL){
		exit(0);
	}
	
	char *str[5500];
	int tab[5500];
	int nbName = 0;
	
	
	/*Remplissage du tableau */
	for(int i = 0 ; i < 5500 ; i++){
		str[i] = malloc(20*sizeof(char));
	}
	
	
	/*Extraction des noms*/
	char carac = 0;
	int i = 0, bool = 1;
	do{
		carac = fgetc(names);
		
		if(carac >= 65 && carac <= 90){
			if(bool){
				str[nbName][i] = '\0';
				// printf("\n");
				nbName++;
				bool = 0;
				i = 0;
			}
				
			// printf("%c", carac);
			str[nbName][i] = carac;
			i++;
		}
		else{
			bool = 1;
		}
	}while(carac != EOF);
	
	
	/*Tri */
	char* tmp = 0;
	for(int j = nbName ; j > 0 ; j--){
		for(i = 0 ; i < j ; i++){
			if(sup(str[i], str[i+1])){
				permute(str, i, i+1);
			}
		}
	}
	
	
	/*Affichage des noms tries */
	// for(i = 0 ; i <= nbName ; i++){
		// printf("%4d: %s, %d\n", i, str[i], worth(str[i]));
	// }
	
	
	/*Calcul des valeurs */
	for(i = 0 ; i <= nbName ; i++){
		tab[i] = worth(str[i]);
		// printf("%s: %d\n", str[i], tab[i]);
	}
	
	
	// /*Affichage valeurs */
	// for(i = 0 ; i <= nbName ; i++){
		// printf("%4d: %3d\n", i, tab[i]);
	// }
	
	
	/*Calcul final */
	int sum = 0;
	for(i = 0 ; i <= nbName ; i++){
		sum += tab[i] * i;
	}
	
	printf("%d\n", sum);
	
	fclose(names);
	return 0;
}

/**Retourne la valeur alphabetique de la chaine de caractere passee en parametre */
int worth(char str[]){
	// printf("%s\n", str);
	
	int sum = 0;
	int index = 64;
	
	for(int i = 0 ; str[i] != '\0' ; i++){
		// printf("%c: %d\n", str[i], str[i] - index);
		sum += str[i] - index;
	}
	
	// printf("Sum: %d\n", sum);
	
	return sum;
}

/**Retourne 0 si str1 est placé avant str2 dans l'ordre alphabétique, 1 sinon*/
int sup(char str1[], char str2[]){
	int i = 0;
	
	while(str1[i] == str2[i] 
			&& str1[i] != '\0' 
			&& str2[i] != '\0'){
		i++;
	}
	
	if(str1[i] == '\0'){
		return 0;
	}
	if(str2[i] == '\0'){
		return 1;
	}
	
	return str1[i] > str2[i];
}

void permute(char** str, int a, int b){
	char* tmp = str[b];
	str[b] = str[a];
	str[a] = tmp;
}