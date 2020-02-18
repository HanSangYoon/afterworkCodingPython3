#Tuple: 능
# >>> 추가, 삭제, 수정이 불가
# >>> tuple 끼리는 연산이 가능
# >>> 따라서 tuple을 정의할 때 값을 같이 지정해 줘야 함.
# >>> list, dic, tuple 정의할 때에는 마지막에 , 콤마를 넣는다.  예) [1,2,3,]

def quot_and_rem(a, b):
    quot = a // b   # 몫
    rem = a % b     # 나머지

    return (quot, rem)


(quot, rem) = quot_and_rem(10, 3)
print(quot, rem)