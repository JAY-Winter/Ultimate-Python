import hashlib

def sha1_for_largefile(filepath, blocksize):
    sha_1 = hashlib.sha1()
    try:
        f = open(filepath, "rb")
    except IOError as e:
        print("file open error", e)
        return
    while True:
        buf = f.read(blocksize)
        if not buf:
            break
        sha_1.update(buf)
    return print(sha_1.hexdigest())


filepath = "/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/수학/09  10/확통2 문제7번.PNG"
blocksize = 8192

sha1_for_largefile(filepath, blocksize)


# 6d0ebf05c06f03ad86fe7dc534d7cb2fee235354
# b7915c5244b9f47dc3101998e453131aa499b7a9
# 91dd127a867f9099c2056007ec6baa45595ff6b8


# fe167cad4d38f947da2117da558aee9bd5c2c24e
# fe167cad4d38f947da2117da558aee9bd5c2c24e