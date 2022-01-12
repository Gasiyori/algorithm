#include <stdio.h>

#pragma warning (disable:4996)

int main() {

	int a, b = 0;

	for (int i = 0; i < 5; i++) {
		scanf("%d", &a);
		b += a;
	}

	printf("%d", b);
}