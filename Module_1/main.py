from Module_1.crypto_utils import Wallet

my_wallet = Wallet("Joseph")
my_wallet.deposit("Eth", 0.7)
my_wallet.deposit("BTC", 1)
print(my_wallet.view_balance())

# wallet = CryptoWallet("Joseph")
# wallet.deposit("ETH", 0.7)
# wallet.deposit("BTC", 0.1)

# print(wallet.view_balance())
