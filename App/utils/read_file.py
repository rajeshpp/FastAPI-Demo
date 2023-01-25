def get_all_users(file):
    with open(file) as f:
        return [user.strip('\n\r') for user in f.readlines()]


def get_specific_user(file, user):
    with open(file) as f:
        return user in [user.strip('\n') for user in f.readlines()]
