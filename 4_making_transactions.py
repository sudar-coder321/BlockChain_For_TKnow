from blockchain import Blockchain

testchain = Blockchain()
testchain.new_transaction("Alice", "Bob", 50)
testchain.new_transaction("Alice", "Catyln", 25)
testchain.new_transaction("Catyln", "Dave", 10)
testchain.new_transaction("Dave", "Bob", 15)
testchain.new_transaction("Catyln", "Alice", 65)

print(*testchain.current_transactions, sep="\n")
