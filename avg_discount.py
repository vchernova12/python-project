import camp_duration


def avg_discount(discounts, camp_days_in_month, duration):
    # discounts = float(discounts)
    discount_per_month = 0
    if len(discounts) == len(camp_days_in_month):
        for i in range(len(camp_days_in_month)):
            discount_per_month += discounts[i]*camp_days_in_month[i]
        avg_discount = discount_per_month/duration
    else:
        raise ValueError("Не хватает данных")
    return (avg_discount)


if __name__ == "__main__":
    print(avg_discount([0.5, 0.3, 0.4], [10, 31, 15], 56))
    print(avg_discount([0.2, 0.3, 0.4, 0.2], [10, 31, 30, 5], 76))
    print(avg_discount([0.5, 0.3], [23, 31, 10], 56))
