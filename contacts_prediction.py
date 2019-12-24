def contacts_prediction(budget, cpm, avg_discount, min_budget=50000):
    if budget >= min_budget:
        contacts_prediction = (budget/(cpm*avg_discount))*1000
    else:
        raise ValueError("Недостаточный бюджет для планирования кампании")
    return (contacts_prediction)


if __name__ == "__main__":
    print(contacts_prediction(1000000, 100, 0.4, 50))
    # print(contacts_prediction (100000, 100, 0.4, 50))