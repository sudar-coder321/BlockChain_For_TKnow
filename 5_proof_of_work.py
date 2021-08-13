from blockchain import Blockchain
from random import randint
import hashlib
testchain = Blockchain()

previous_block = testchain.chain[0]

previous_hash = testchain.hash(previous_block)
previous_proof = previous_block['proof']

proof = 0


def valid_proof(previous_proof, proof, previous_hash):
    guess = f'{previous_proof}{proof}{previous_hash}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[:4] == "0000"


while valid_proof(previous_proof, proof, previous_hash) is False:
    proof += 1

print(proof)
