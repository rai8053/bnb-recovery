# 🛡️ BSC Token Sweep Script (Web3.py)

This script helps you **safely sweep tokens** from a compromised wallet on the **Binance Smart Chain (BSC Mainnet)** and send them to your own **CEX deposit address**.  
It generates a **signed raw transaction (HEX)** that you can broadcast manually once you add BNB for gas.

---

## 🚀 Features
- Connects to BSC Mainnet  
- Reads ERC-20 token balance  
- Builds a token transfer transaction  
- Signs it offline using your private key  
- Outputs **RAW HEX** (safe to broadcast later)

---

## 📦 Requirements
Install Web3:

```bash
pip install web3
```

---

## 🔧 Setup
Edit the following fields in the script:

```python
private_key = "your_private_key"
from_address = "your_compromised_wallet_address"
to_address = "your_cex_deposit_address"
token_address = "your_token_contract_address"
```

---

## ▶️ Running the Script
Run normally:

```bash
python sweep.py
```

If your wallet has tokens, the script prints:

```
Signed Transaction (RAW HEX):
0x....
```

Copy that hex for later broadcasting.

---

## ⛽ Important: Gas Requirement
You must send **a small amount of BNB** (0.001–0.005 BNB) to the compromised wallet BEFORE your sweep transaction can be broadcast.

Once BNB arrives, uncomment:

```python
# tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# print(w3.to_hex(tx_hash))
```

Then run again to automatically broadcast.

---

## ⚠️ Security Warning
- NEVER share your private key.  
- ONLY use this script on your own wallets.  
- Always store private keys offline.  

---

## 📄 Minimal ERC-20 ABI Used
Only `transfer` and `balanceOf` are included for safety and simplicity.

---

## ✔️ Done
Your script is ready.  
Paste and run it to sweep tokens from compromised wallets securely.
