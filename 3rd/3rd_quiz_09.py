#문제9
#관공서 주차장에서는 차량 2부제를 실시합니다. 차량 2부제는 차량 번호 끝자리가 홀수인 차량은 홀수 일에만, 짝수인 차량은 짝수 일에만 주차장에 들어올 수 있도록 하는 제도입니다.
#며칠인지를 나타내는 day와 그날 주차장에 들어오려고 하는 차들의 번호를 담고 있는 리스트 numbers가 매개변수로 주어질 때, 주차장에 들어올 수 있는 차량의 수를 return 하도록 solution 함수를 작성했습니다. 그러나, 코드 일부분이 잘못되어있기 때문에, 코드가 올바르게 동작하지 않습니다. 주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.
#단, 중복되는 번호판 번호는 주어지지 않습니다.

#---
#####매개변수 설명
#며칠인지를 나타내는 day와 그날 주차장에 들어오려고 하는 차들의 번호를 담고 있는 리스트 numbers가 solution 함수의 매개변수로 주어집니다.

#* day는 1 이상 31이하의 자연수입니다.
#* numbers의 길이는 1 이상 9,000 이하입니다.
##* numbers의 원소는 1,000 이상 9,999 이하의 자연수입니다.
#* numbers에는 차량 번호가 중복되어 들어있지 않습니다.

#---
#####return값 설명
#주차장에 들어올 수 있는 차량의 수를 return 해주세요.

#---
#####예시
#| day | numbers | return |
#|---|---|---|
#| 17 | [3285, 1724, 4438, 2988, 3131, 2998] | 2 |

#---
#####예시 설명
#17일은 홀수 일이므로 홀수 번호 차량인 1724, 3131 총 2대의 차량만 주차장에 들어올 수 있습니다.




def solution(day, numbers):
    count = 0
    for number in numbers:
        if number%2 != day%2:
            count += 1
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
day = 17
numbers = [3285, 1724, 4438, 2988, 3131, 2998]
ret = solution(day, numbers)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
