#!/usr/bin/env python3
"""
Vibe Coding W2-2 Test Application
간단한 계산기 애플리케이션 (의도적 버그 포함)
"""

def divide_numbers(a, b):
    """두 숫자를 나누는 함수"""
    # 버그: 0으로 나누기 예외 처리가 없음
    result = a / b
    return result

def calculate_average(numbers):
    """숫자 리스트의 평균을 계산하는 함수"""
    # 버그: 빈 리스트에 대한 처리가 없음
    total = sum(numbers)
    average = total / len(numbers)
    return average

def process_user_input(user_input):
    """사용자 입력을 처리하는 함수"""
    # 버그: 문자열을 숫자로 변환할 때 예외 처리가 없음
    number = int(user_input)
    return number * 2

def main():
    """메인 함수"""
    print("=== Vibe Coding W2-2 Calculator ===")
    
    # 테스트 케이스 1: 0으로 나누기
    print("\n1. Division Test:")
    try:
        result1 = divide_numbers(10, 0)  # 이것은 ZeroDivisionError를 발생시킴
        print(f"10 / 0 = {result1}")
    except Exception as e:
        print(f"Error in division: {e}")
    
    # 테스트 케이스 2: 빈 리스트 평균
    print("\n2. Average Test:")
    try:
        result2 = calculate_average([])  # 이것은 ZeroDivisionError를 발생시킴
        print(f"Average of empty list = {result2}")
    except Exception as e:
        print(f"Error in average calculation: {e}")
    
    # 테스트 케이스 3: 잘못된 입력 타입
    print("\n3. Input Processing Test:")
    try:
        result3 = process_user_input("hello")  # 이것은 ValueError를 발생시킴
        print(f"Processed input: {result3}")
    except Exception as e:
        print(f"Error in input processing: {e}")
    
    # 테스트 케이스 4: 정상 동작
    print("\n4. Normal Operation Test:")
    try:
        result4 = divide_numbers(10, 2)
        result5 = calculate_average([1, 2, 3, 4, 5])
        result6 = process_user_input("42")
        print(f"10 / 2 = {result4}")
        print(f"Average of [1,2,3,4,5] = {result5}")
        print(f"Process '42' = {result6}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main() 