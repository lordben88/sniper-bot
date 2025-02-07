import json

# Load configuration from config.json
with open("config.json") as config_file:
    config = json.load(config_file)

# Example: Print the default buy amount and RPC URL
print(f"Default Buy Amount: {config['default_buy_amount']}")
print(f"RPC URL: {config['rpc_url']}")

# TODO: Implement Solana wallet connection and trading logic

