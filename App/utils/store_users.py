def post_user(file, user):
    with open(file, 'a') as f:
        f.write(f"{user}\n")
