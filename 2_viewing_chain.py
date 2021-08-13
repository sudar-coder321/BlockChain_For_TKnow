from blockchain import Blockchain

if __name__ == '__main__':
    testchain = Blockchain()
    for i in range(5):
        proof = testchain.proof_of_work(testchain.last_block)
        hashval = testchain.hash(testchain.last_block)
        block = testchain.new_block(proof,hashval)
    print (*testchain.chain,sep="\n")
