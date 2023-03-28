class UnexpectedRSPValue(Exception):
    '''가위, 바위, 보 중 포함되지 않는 값인 경우 발생하는 에러'''

value = input('가위, 바위, 보 중 하나를 입력해주세요. > ')

try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print('에러가 발생했습니다.')