from zope import interface

from pyramid_stripe import interfaces


@interface.implementer(interfaces.IStripe)
class Stripe(object):
    def __init__(self, request):
        self.request = request


@interface.implementer(interfaces.ICharge)
class Charge(Stripe):
    pass


@interface.implementer(interfaces.IChargeSucceeded)
class ChargeSucceeded(Charge):
    pass


@interface.implementer(interfaces.IChargeFailed)
class ChargeFailed(Charge):
    pass


@interface.implementer(interfaces.IChargeRefunded)
class ChargeRefunded(Charge):
    pass


@interface.implementer(interfaces.IChargeDisputed)
class ChargeDisputed(Charge):
    pass


@interface.implementer(interfaces.IChargeFailed)
class ChargeFailed(Charge):
    pass


@interface.implementer(interfaces.ICustomer)
class Customer(Stripe):
    pass


@interface.implementer(interfaces.ICustomerCreated)
class CustomerCreated(Customer):
    pass


@interface.implementer(interfaces.ICustomerUpdated)
class CustomerUpdated(Customer):
    pass


@interface.implementer(interfaces.ICustomerDeleted)
class CustomerDeleted(Customer):
    pass


@interface.implementer(interfaces.ICustomerSubscription)
class CustomerSubscription(Customer):
    pass


@interface.implementer(interfaces.ICustomerSubscriptionCreated)
class CustomerSubscriptionCreated(CustomerSubscription):
    pass


@interface.implementer(interfaces.ICustomerSubscriptionUpdated)
class CustomerSubscriptionUpdated(CustomerSubscription):
    pass


@interface.implementer(interfaces.ICustomerSubscriptionDeleted)
class CustomerSubscriptionDeleted(CustomerSubscription):
    pass


@interface.implementer(interfaces.ICustomerSubscriptionTrialWillEnd)
class CustomerSubscriptionTrialWillEnd(CustomerSubscription):
    pass


@interface.implementer(interfaces.ICustomerDiscount)
class CustomerDiscount(Customer):
    pass


@interface.implementer(interfaces.ICustomerDiscountCreated)
class CustomerDiscountCreated(CustomerDiscount):
    pass


@interface.implementer(interfaces.ICustomerDiscountUpdated)
class CustomerDiscountUpdated(CustomerDiscount):
    pass


@interface.implementer(interfaces.ICustomerDiscountDeleted)
class CustomerDiscountDeleted(CustomerDiscount):
    pass


@interface.implementer(interfaces.IInvoice)
class Invoice(Stripe):
    pass


@interface.implementer(interfaces.IInvoiceCreated)
class InvoiceCreated(Invoice):
    pass


@interface.implementer(interfaces.IInvoiceUpdated)
class InvoiceUpdated(Invoice):
    pass


@interface.implementer(interfaces.IInvoicePayment)
class InvoicePayment(Invoice):
    pass


@interface.implementer(interfaces.IInvoicePaymentSucceeded)
class InvoicePaymentSucceeded(InvoicePayment):
    pass


@interface.implementer(interfaces.IInvoicePaymentFailed)
class InvoicePaymentFailed(InvoicePayment):
    pass


@interface.implementer(interfaces.IInvoiceItem)
class InvoiceItem(Stripe):
    pass


@interface.implementer(interfaces.IInvoiceItemCreated)
class InvoiceItemCreated(InvoiceItem):
    pass


@interface.implementer(interfaces.IInvoiceItemUpdated)
class InvoiceItemUpdated(InvoiceItem):
    pass


@interface.implementer(interfaces.IInvoiceItemDeleted)
class InvoiceItemDeleted(InvoiceItem):
    pass


@interface.implementer(interfaces.IPlan)
class Plan(Stripe):
    pass


@interface.implementer(interfaces.IPlanCreated)
class PlanCreated(Plan):
    pass


@interface.implementer(interfaces.IPlanUpdated)
class PlanUpdated(Plan):
    pass


@interface.implementer(interfaces.IPlanDeleted)
class PlanDeleted(Plan):
    pass


@interface.implementer(interfaces.ICoupon)
class Coupon(Stripe):
    pass


@interface.implementer(interfaces.ICouponCreated)
class CouponCreated(Coupon):
    pass


@interface.implementer(interfaces.ICouponUpdated)
class CouponUpdated(Coupon):
    pass


@interface.implementer(interfaces.ICouponDeleted)
class CouponDeleted(Coupon):
    pass


@interface.implementer(interfaces.ITransfer)
class Transfer(Stripe):
    pass


@interface.implementer(interfaces.ITransferCreated)
class TransferCreated(Transfer):
    pass


@interface.implementer(interfaces.ITransferFailed)
class TransferFailed(Transfer):
    pass


@interface.implementer(interfaces.IPing)
class Ping(Stripe):
    pass