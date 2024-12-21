USERS_FIXTURE_1 = [
    {'username': 'user01', 'email': 'user01@test.com', 'password': 'user01Pw'},
    {'username': 'user02', 'email': 'user02@test.com', 'password': 'user02Pw'},
]

USERS_FIXTURE_2 = [
    {'username': 'admin', 'email': 'admin@test.com', 'password': 'adminPw'},
    {'username': 'staff', 'email': 'staff@test.com', 'password': 'staffPw'},
    {'username': 'guest', 'email': 'guest@test.com', 'password': 'guestPw'},
]

USERS_FIXTURE_LARGE = [
    {'username': f'user{i}', 'email': f'user{i}@test.com', 'password': f'securyPw{i}'}
    for i in range(100)
]
