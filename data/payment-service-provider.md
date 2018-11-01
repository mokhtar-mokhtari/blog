# Payment service provider

A **payment service provider** (PSP) offers shops online services for accepting electronic payments by a variety of payment methods including credit card, bank-based payments such as direct debit, bank transfer, and real-time bank transfer based on [online banking](https://en.wikipedia.org/wiki/Online_banking). Typically, they use a [software as a service](https://en.wikipedia.org/wiki/Software_as_a_service). model and form a single payment gateway for their clients (merchants) to multiple payment methods.

Typically, a PSP can connect to multiple acquiring banks, card, and payment networks. In many cases, the PSP will fully manage these technical connections, relationships with the external network, and bank accounts. This makes the merchant less dependent on financial institutions and free from the task of establishing these connections directly, especially when operating internationally. Furthermore, by negotiating bulk deals they can often offer cheaper fees.

Furthermore, a full-service PSP can offer risk management services for card and bank based payments, transaction payment matching, reporting, fund remittance and fraud protection in addition to multi-currency functionality and services. Some PSPs provide services to process other next generation methods (payment systems) including cash payments, wallets, prepaid cards or vouchers, and even paper or e-check processing.

A PSP is thus a much broader term than a payment gateway which is how the payment card industry refers to them.

PSP fees are typically levied in one of two ways: as a percentage of each transaction or a fixed cost per transaction.

US-based on-line payment service providers are supervised by the Financial Crimes Enforcement Network (or FinCEN), a bureau of the United States Department of the Treasury that collects and analyzes information about financial transactions in order to combat money laundering, terrorist financiers, and other financial crimes.

There are more than 900 payment providers in the world. More than 300 offer services for Europe and North America.

## Payment gateway

A **payment gateway** is a merchant service provided by an e-commerce application service provider that authorizes credit card or direct payments processing for e-businesses, online retailers, bricks and clicks, or traditional brick and mortar. The payment gateway may be provided by a bank to its customers, but can be provided by a specialised financial service provider as a separate service, such as a payment service provider.

A payment gateway facilitates a payment transaction by the transfer of information between a payment portal (such as a website, mobile phone or interactive voice response service) and the front end processor or acquiring bank.

### Typical transaction processes

When a customer orders a product from a payment gateway-enabled merchant, the payment gateway performs a variety of tasks to process the transaction.

1. A customer places an order on website by pressing the 'Submit Order' or equivalent button, or perhaps enters their card details using an automatic phone answering service.
1. If the order is via a website, the customer's web browser encrypts the information to be sent between the browser and the merchant's webserver. In between other methods, this may be done via SSL (Secure Socket Layer) encryption. The payment gateway may allow transaction data to be sent directly from the customer's browser to the gateway, bypassing the merchant's systems. This reduces the merchant's Payment Card Industry Data Security Standard (PCI DSS) compliance obligations without redirecting the customer away from the website.
1. The merchant then forwards the transaction details to their payment gateway. This is another (SSL) encrypted connection to the payment server hosted by the payment gateway.
1. The payment gateway converts the message from XML to ISO 8583 or a variant message format (format understood by EFT Switches) and then forwards the transaction information to the payment processor used by the merchant's acquiring bank.
1. The payment processor forwards the transaction information to the card association (I.e.: Visa/MasterCard/American Express). If an American Express or Discover Card was used, then the card association also acts as the issuing bank and directly provides a response of approved or declined to the payment gateway. Otherwise, the card association routes the transaction to the correct card issuing bank.
1. The credit card issuing bank receives the authorization request, verifies the credit or debit available and then sends a response back to the processor (via the same process as the request for authorization) with a response code (I.e.:: approved, denied). In addition to communicating the fate of the authorization request, the response code is also used to define the reason why the transaction failed (I.e.: insufficient funds, or bank link not available). Meanwhile, the credit card issuer holds an authorization associated with that merchant and consumer for the approved amount. This can impact the consumer's ability to spend further ( because it reduces the line of credit available or it puts a hold on a portion of the funds in a debit account).
1. The processor forwards the authorization response to the payment gateway
1. The payment gateway receives the response, and forwards it on to the website (or whatever interface was used to process the payment) where it is interpreted as a relevant response then relayed back to the merchant and cardholder. This is known as the Authorization or "Auth"
1. The entire process typically takes 2–3 seconds.
1. The merchant then fulfills the order and the above process can be repeated but this time to "Clear" the authorization by consummating the transaction. Typically, the "Clear" is initiated only after the merchant has fulfilled the transaction (I.e.: shipped the order). This results in the issuing bank 'clearing' the 'auth' (i.e.: moves auth-hold to a debit) and prepares them to settle with the merchant acquiring bank.
1. The merchant submits all their approved authorizations, in a "batch" (end of the day), to their acquiring bank for settlement via its processor. This typically reduces or "Clears" the corresponding "Auth" if it has not been explicitly "Cleared".
    The acquiring bank makes the batch settlement request of the credit card issuer.
1. The credit card issuer makes a settlement payment to the acquiring bank (the next day in most cases)
1. The acquiring bank subsequently deposits the total of the approved funds into the merchant's nominated account (the same day or next day). This could be an account with the acquiring bank if the merchant does their banking with the same bank, or an account with another bank.
1. The entire process from authorization to settlement to funding typically takes 3 days.