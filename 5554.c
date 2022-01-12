#include <stdio.h>

#pragma warning (disable : 4996)

int main() {
	int a[4];
	int b = 0;

	for (int i = 0; i < 4; i++) {
		scanf("%d", &a[i]);
		b += a[i];
	}
	printf("%d\n%d", b/60, b%60);
}