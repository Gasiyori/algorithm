#include <stdio.h>

#pragma warning (disable : 4996)

int main() {

	int a;
	int b;// a는 사람, b는 넓이

	scanf("%d %d", &a, &b);

	int p[5]; //참가자 수

	for (int i = 0; i < 5; i++) {
		scanf("%d", &p[i]);
	}

	for (int i = 0; i < 5; i++) {
		printf("%d ", p[i] - a * b);
	}
}