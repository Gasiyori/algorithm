#include <stdio.h>

//100 자리수 예제(입력받아서 출력)

//19283746564738291828374658492190203821743674268423148347343187
//6459673984658736478136478126129038124728952734589374823641782481

//6478957731223474769964852784621228328550696408857797971989125668
#define CNT 100

int main(){
    char num_a[CNT];
    char num_b[CNT];
    char num_a_[CNT];
    char num_b_[CNT];
    char result[CNT+1] = ""; // 이거 초기화 안해주면 결과 뒤에 이상한게 붙는다
    int carry = 0;
    int sum = 0;
    int i = 0;

// sprintf_s: (대상버퍼, 사이즈, 서식 지정자, 소스버퍼)
// sprintf와의 차이점: 사이즈 지정 (기존 sprintf는 사이즈 지정이 없어 잘못하면 버퍼 오버플로우)

// %099s의 의미: %s (문자열) 로 출력하되 99자가 될때까지 0을 앞에 채운다는 뜻
// %0100s로 하면 화면에 아무것도 안뜸. sprintf의 결과는 끝에 NULL을 채우기 때문에 길이 초과

    scanf_s("%s %s", num_a, CNT, num_b ,CNT);

    sprintf_s(num_a_, sizeof(num_a_), "%099s", num_a); //100자리라서 99까지임. 여기도 최대 CNT-1 숫자로 바꿔줘야 함
    sprintf_s(num_b_, sizeof(num_b_), "%099s", num_b);
    
    printf("%s\n", num_a_);
    printf("%s\n", num_b_);

    for (i=sizeof(num_a_)-2; i>=0; i--){ //num_a의 최대 사이즈부터 내려가서 0이 아닌 구간 찾기, 2는 널 문자를 고려해서 추가해줌.
    // 각 자리는 아스키 코드표의 숫자로 처리, '0' 을 빼면 문자로서의 숫자값이 된다
    // 다시 결과배열에 넣을때는 반대로 '0' 을 더해줘야 문자가 됨
    sum = (num_a_[i]-'0') + (num_b_[i]-'0') + carry; //각 자리 수 숫자 + 캐리, 각 배열 위치에 해당하는 숫자끼리 연산
    carry = sum / 10;  // 캐리는 더한 값에서 10을 나누어서 계산함

    sum = sum % 10; //올라간 수 말고 남은 수는 해당 자리수에 남겨둠
    result[i+1] = sum + '0';
  }

    result[0] = carry + '0';

    for (i=0; result[i] == '0'; i++);

    printf("%s\n", result + i); // 배열 시작주소 + i칸. 여기서 i를 써먹기 위해서는 i를 위에서 선언

    return 0;
}