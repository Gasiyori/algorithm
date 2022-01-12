#include <stdio.h>
#include <math.h>

#pragma warning (disable : 4996)

int main() {
	float b, c;

	scanf("%f %f", &b, &c);

	int a = (b * (c - 1)) + 1;

	printf("%d", a);
}

/*



a 멜로디의 개수

b 수록곡 개수

c 평균값(항상 올림되어 만들어짐)

ex) b(38개 곡이 수록되어 있고), a(앨범에 저작권이 있는 멜로디가 894개라면) c(평균값은 23.53이고 올림하여 24가 됨.)

a / b = c(올림)

주어지는건 수록곡 개수와 평균값
즉, b와 c
구해야 하는건 a
a = b * c

23을 곱하면 23에 대한 평균값을 구한 것임 >> 874
여기서 1을 더하면 24에 대한 평균값 중 가장 작은 값이 됨 >> 875

*/