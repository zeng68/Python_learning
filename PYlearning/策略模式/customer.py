from 支付策略 import *

payment_strategy = CreditCardPayment()
payment_strategy2 = PayPalPayment()

cart = ShoppingCart(payment_strategy2)
cart.checkout(100)
