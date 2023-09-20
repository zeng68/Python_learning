# 抽象基类
class PaymentStrategy:
    def pay(self, amount):
        pass


# 支付策略1
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using credit card.")


# 支付策略2
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")


# 支付
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)


""""
使用策略模式有以下好处：
1. **可扩展性**：策略模式使得系统可以轻松添加新的支付策略，只需创建一个新的支付策略类并实现其`pay`方法即可。不需要修改现有代码，遵循了开闭原则。
2. **代码复用**：通过将支付策略封装在独立的类中，可以在不同的场景中重复使用这些策略类。不同的对象可以共享相同的支付策略，提高了代码的复用性。
3. **可维护性**：将不同的支付策略分离到独立的类中，使得每个类的职责清晰明确。当需要修改或调试某个支付策略时，可以集中在相应的类中进行修改，不会对其他类产生影响，提高了代码的可维护性。
4. **可配置性**：通过将支付策略作为参数传递给需要使用支付功能的类，可以在运行时动态地选择不同的支付策略。这种灵活性使得系统更具可配置性，可以根据需求轻松切换不同的支付方式。
5. **单一职责原则**：策略模式将不同的支付策略封装到独立的类中，每个类负责实现一种支付策略。这样每个类的职责更加明确，符合单一职责原则，代码更加清晰和可读。
总而言之，策略模式提供了一种灵活、可扩展和可维护的设计方案，使得系统中的算法或行为可以独立于使用它们的对象进行变化。它提高了代码的可复用性、可维护性和可配置性，同时使系统更加灵活和易于扩展。

"""
