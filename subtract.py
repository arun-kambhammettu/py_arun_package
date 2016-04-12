#subtract.py
'''
This is the subtraction Module! It takes two numbers and returns their difference.
'''

def sub(number1, number2):
    '''
    Subtract num2 from num1
    '''
    return number1 - number2

def test_sub():
    result = sub(8,4)
    if result == 4:
        print('Subtraction tests Passed...')
    else:
        print('Subtraction Failed...')

if __name__ == '__main__':
    try:
        test_sub()
    except Exception as ex:
        print('Fail, error',ex)
