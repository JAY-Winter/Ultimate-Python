import hashlib



def getHash(file_path, blocksize):

    sha_1 = hashlib.sha1()
    

    try:
        f = open(file_path, "rb")
        
    except IOError as e:
        print("file open error", e)
        return

    while True:
        buf = f.read(blocksize)

        if not buf:
            break

        sha_1.update(buf)

    return sha_1.hexdigest()





