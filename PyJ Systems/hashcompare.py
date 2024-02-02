import glob
import hashlib
Log= []
filenames = glob.glob("PyJ Systems/*")

for filename in filenames:
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        print(filename, hashlib.md5(data).hexdigest())
        print(filename.rsplit("/"), hashlib.md5(data).hexdigest())
        print(filename.strip("/"), hashlib.md5(data).hexdigest())
        print(filename.splitlines(True))