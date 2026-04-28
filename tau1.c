#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	srand(time(NULL)); // To be sure the random numbers are not the same

	long long a = (long long)rand() * rand(); // First large random number
	long long b = (long long)rand() * rand(); // Second large number

	long long c = a * b; // Product

	return 0;
}
