from web3 import Web3
import json

# Step 1: Connect to BSC Mainnet
w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))

# Step 2: Wallet and Contract Info
private_key = "274320f79bb53daf6ee6f1dbf854c21e648c4ee70cebfb68bf43f73bb8306329"
from_address = w3.to_checksum_address("0x60eBf48C80c6b540F712F2aF4Aad0175ED5Ab08d")
to_address = w3.to_checksum_address("0x1b713b14cd3a813366524a1e82864bd064d839a6")  # CEX deposit address
token_address = w3.to_checksum_address("0x899357E54C2c4b014ea50A9A7Bf140bA6Df2eC73")  # Token contract

# Step 3: Minimal ERC-20 ABI
token_abi = json.loads('[{"name":"transfer","type":"function","inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"outputs":[{"name":"","type":"bool"}],"stateMutability":"nonpayable"},{"name":"balanceOf","type":"function","inputs":[{"name":"_owner","type":"address"}],"outputs":[{"name":"balance","type":"uint256"}],"stateMutability":"view"}]')
contract = w3.eth.contract(address=token_address, abi=token_abi)

# Step 4: Check token balance
token_balance = contract.functions.balanceOf(from_address).call()
print(f"Token Balance: {token_balance}")

if token_balance == 0:
    print("No tokens to transfer.")
    exit()

# Step 5: Build transaction
nonce = w3.eth.get_transaction_count(from_address)
gas_price = w3.to_wei("5", "gwei")  # low gas price
txn = contract.functions.transfer(to_address, token_balance).build_transaction({
    "chainId": 56,
    "gas": 100000,
    "gasPrice": gas_price,
    "nonce": nonce,
})

# Step 6: Sign the transaction
signed_txn = w3.eth.account.sign_transaction(txn, private_key)
raw_tx_hex = w3.to_hex(signed_txn.rawTransaction)

print("\nSigned Transaction (RAW HEX):")
print(raw_tx_hex)

# Step 7: Wait for BNB to arrive, then send manually:
# Uncomment once you’ve funded wallet:
# tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# print(f"Transaction sent: {w3.to_hex(tx_hash)}")

