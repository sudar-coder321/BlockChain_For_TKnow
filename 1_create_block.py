from blockchain import Blockchain  
if __name__ == '__main__':s
    testchain = Blockchain()

    #Proof of work :)
    proof = testchain.proof_of_work(testchain.chain[0])

    #Generating hash value for the data
    hashval = testchain.hash(testchain.chain[0])

    # Creating new block
    block = testchain.new_block(proof,hashval)

    #Printing the values in the block
    print (block)
