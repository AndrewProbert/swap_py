from uniswap import Uniswap

address = "0xb63b9616F641641e8dA67eaF1bEc0A4bE55431E2"          #should be the address of the wallet you're using to make transactions
private_key = "0"  # or None if you're not going to make transactions
version = 3                       # specify which version of Uniswap to use
provider = "https://mainnet.infura.io/v3/b931e338739a41d7a537c683bb2f21d5"    # can also be set through the environment variable `PROVIDER`
uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)

# Some token addresses we'll be using later in this guide
token_1 = "0x0000000000000000000000000000000000000000"
token_2 = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"

amount = 1


# Get the price of ETH in DAI
price = uniswap.get_price_output(token_1, token_2, amount * 10**18)
print(f"price: {price}")



