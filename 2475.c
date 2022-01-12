#include <stdio.h>

#pragma warning(disable: 4996)

int main() {
	int A[6];
	int result = 0;

	for (int i = 0; i < 5; i++)
		scanf("%d", &A[i]);

	for (int i = 0; i < 5; i++)
		result += A[i]*A[i];

	printf("%d", result % 10);	
}