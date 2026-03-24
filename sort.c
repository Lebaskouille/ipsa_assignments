#include <stdio.h>
#include "sort.h"

void sort(int arr[], int size){
	for (int i = 0; i < size-1 ; i++){
		int plus_petit = i;
		for (int j = i+1; j < size; j++){
			if (arr[j] < arr[plus_petit]){
				plus_petit = j;
			}
		}
		int copie = arr[i];
		arr[i] =  arr[plus_petit];
		arr[plus_petit] = copie;
	}
}
