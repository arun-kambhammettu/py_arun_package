# add.py
'''
This is the addition Module!
'''
def add(number1, number2):
    '''
    It accepts two numbers and returns their sum.
    '''
    return number1 + number2


def test_add():
    result = add(3,7)
    if result == 10:
        print('Add test is Passed...')
    else:
        print('Add test Failed...')


if __name__ == '__main__':
    try:
        test_add()

    except Exception as ex:
        print('Fail, error',ex)
