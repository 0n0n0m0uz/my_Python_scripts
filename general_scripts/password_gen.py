import string
import secrets

''.join(
    secrets.choice(string.ascii_uppercase + string.digits +
                   string.punctuation + string.ascii_lowercase)
    for _ in range(20))
