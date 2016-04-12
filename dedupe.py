# dedupe.py
'''
This is the dedupe Module!

We have functions being defined.
If we are the developer we can test our code right here
We also expose a "test_dedupe" method to others...


We have successfully made it easier to maintain this code!

We made it easier to develop, we made so other developers
don't have to worry about the dirty details of how
stuff gets deduped. They just call us!

'''
def dedupe(list_one, list_two):
    return list(set(list_one + list_two))


def test_dedupe():
        l_one = [1,2,3,4]
        l_two = [2,5,6,7]
        deduped = dedupe(l_one, l_two)
        if (deduped.count(2) > 1) or len(deduped) < 7:
            raise
        else:
            print('Dedupe tests Passed')

if __name__ == '__main__':
    try:
        test_dedupe();
    except Exception as ex:
        print('Fail, error',ex)
