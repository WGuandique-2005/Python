import bcrypt

password = "12345"
pw_encoded = password.encode()

#? SALT determina la fuerza de hasheo
salt = bcrypt.gensalt(18)
hash_pw = bcrypt.hashpw(pw_encoded,salt)
print(hash_pw)