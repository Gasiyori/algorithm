#include <stdio.h>
#include <time.h>

int main() {
	struct tm *t;
	time_t timer; 

	timer = time(NULL);   
	t = gmtime(&timer);
    //한국 시간을 원하면 gmtime이 아니라 localtime을 쓰면 됨.

	printf("%d-%02d-%02d",t->tm_year + 1900, t->tm_mon + 1, t->tm_mday);

}