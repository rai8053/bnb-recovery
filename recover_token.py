from web3 import Web3
import json

# Step 1: Connect to BSC Mainnet
w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))

# Step 2: Wallet and Contract Info
private_key = "your_private_key"
from_address = w3.to_checksum_address("your_compromised_wallet_address")
to_address = w3.to_checksum_address("your_deposit_address")  # CEX deposit address
token_address = w3.to_checksum_address("your_token_contract_address")  # Token contract

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

# Step 7: Send when BNB is available
# tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# print(f"Transaction sent: {w3.to_hex(tx_hash)}")
