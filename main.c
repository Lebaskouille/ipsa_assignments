#include <stdio.h>
#include "sort.h"
#include <time.h>

int main(){
	int tab[] = {10, 3, 7, 1, 8, 2, 5, 4, 9, 6};
	int taille = 10;

	clock_t debut = clock();
	sort(tab, taille);
	for(int i = 0; i < taille; i++) {
        	printf("%d ", tab[i]);
    	}
	clock_t fin = clock();
	double sec = (double)(fin-debut)/ CLOCKS_PER_SEC;
	double ms = sec*1000.0;
	double us = sec*1000000.0;

	printf(" %-10d %-14.6f %-14.3f %-14.1f\n", taille, sec, ms, us);

	return 0;
}
