#include <stdio.h>

#pragma warning (disable:4996)

int main() {
	int a[4];

	for (int i = 0; i < 4; i++) {
		scanf("%d", &a[i]);
	}

	printf("%d", a[0] * a[1] + a[2] * a[3]);
}