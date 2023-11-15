from embit import bip32
from embit.script import p2wpkh

def generate_addresses(zpub, num_addresses=5):
    # Create a BIP32 key from the zpub
    key = bip32.HDKey.from_string(zpub)
    
    # Generate and store the addresses
    addresses = []
    for i in range(num_addresses):
        # Derive the child key at the specified index
        child_key = key.derive([0, i])  # 0 for external chain
        
        # Get the address from the child key
        address = p2wpkh(child_key).address()
        addresses.append(address)

    return addresses

# Get the zpub from the user
zpub = input("Enter your zpub key: ")
addresses = generate_addresses(zpub)

# Print the generated addresses
print("Generated Bitcoin Addresses:")
for address in addresses:
    print(address)
