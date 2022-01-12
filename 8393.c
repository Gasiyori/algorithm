#include <stdio.h>

#pragma warning (disable:4996)

int main() {
	int a, tmp = 0;
	scanf("%d", &a);

	for (int i = 0; i <= a; i++) {
		tmp += i;
	}
	
	printf("%d", tmp);
}