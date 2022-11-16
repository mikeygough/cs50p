from validator_collection import validators, checkers, errors

if checkers.is_email(input('input: ')):
    print('Valid')
else:
    print('Invalid')