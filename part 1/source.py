import hashlib
import math

#Do not change the name of this class
class MerkleTreeCalculator:
    #use this function for hashing a file
    def sha256sum(self, filename):
        h = hashlib.sha256()
        with open(filename, 'rb', buffering=0) as f:
            for b in iter(lambda: f.read(128 * 1024), b''):
                h.update(b)
        return h.hexdigest()
    
    def myHash(self, text):
        n = hashlib.sha256(str(text).encode('utf-8'))
        return n.hexdigest()

	#Do not change the name of this function
    
    def calculate_merkle_root(self):
        n = 20
        d = int(math.log2(20))
        height = int(n/2)
        myhash = [None for _ in range(height)]
        for i in range(height):
            myhash[i] = self.myHash(self.sha256sum('file'+str(2*i+1)+'.txt') +
                self.sha256sum('file'+str(2*i+2)+'.txt'))
        
        height = int(height/2)
        while(d!=0):
            for i in range(height):
                myhash[i] = self.myHash(myhash[2*i] + myhash[2*i+1])
            if(height%2 == 1):
                myhash[height] = myhash[height - 1]
                height+=1

            height = int(height/2)
            d-=1
        return(myhash[0])
                
    
#
#mymerkle = MerkleTreeCalculator()
#A = mymerkle.calculate_merkle_root()
#print(A)   