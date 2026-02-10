# 1st Time Payments Analysis

About 40% of our transactions are cashless—meaning we are charging clients and paying the majority of the charge to the driver every week (withholding our 15-25% commissions).

We always pay the driver and take the risk of collecting funds from the client.

Luckily, we have basic filters to block users from making multiple fraudulent transactions and can identify groups of fraudulent users using the same devices or cards. The next step is to prevent fraudulent transactions from users on their first attempt.

## Outcome and Task Description

Based on the sample data, please propose the top 2-5 developments that should be implemented to reduce the percentage of failed payments (where `is_successful_payment` is 0). Keep in mind that our developer team is small (3-4 people), so please explain why you selected these specific developments.

If any parameters are missing from the list below, assume we collect all reasonable data available from platform use by riders and drivers.

When describing the top developments, please explain your process and reasoning—we are interested in both the outcome and how you approach problems.

## Sample Data

Below is a dump of first-time credit card orders (worldwide): [ZIP](1st_adyen_rides-success-and-fail.csv.zip)

The data includes metadata on users who make their first completed order with a credit card as a payment method, as well as metadata on the transaction itself.

### Field Legend

* **created**: Time when the first-time order request was created.
* **device_name**: Name of the device used to make the order.
* **device_os_version**: Version of the device's OS.
* **country**: 2-character country code.
* **city_id**: Internal system city ID (not relevant which one is which).
* **lat**: Latitude of the pickup location for the order.
* **lng**: Longitude of the pickup location for the order.
* **real_destination_lat**: Latitude of the destination for the order.
* **real_destination_lng**: Longitude of the destination for the order.
* **user_id**: Internal user ID.
* **order_id**: Internal order ID.
* **order_try_id**: Internal order try ID (order tries occur before a client and driver are matched to an order).
* **distance**: Driver distance to the client’s pickup location, in meters.
* **ride_distance**: Trip distance in meters.
* **price**: Price charged to the client, which may be lower than `ride_price` if the client had a discount; currencies vary and are undefined.
* **ride_price**: Calculated price of the final trip; currencies vary and are undefined.
* **price_review_status**: Status of the price review. "Price review" occurs when `ride_price` is sent for human audit to check for system errors. 99% of orders are final and should have "ok" set. Some might be in pending states, which you can likely disregard.
* **price_review_reason**: Automatic or manual reason for the price review request.
* **is_successful_payment**: `1` indicates the order was charged successfully, while `0` indicates it failed (including after all attempts to re-charge).
* **name**: Card details, irrelevant.
* **card_bin**: Details on the card's BIN.
* **failed_attempts**: Number of failed order attempts before this first completed order.
