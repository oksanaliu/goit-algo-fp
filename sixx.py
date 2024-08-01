def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            chosen_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return chosen_items, total_cost, total_calories

def dynamic_programming(items, budget):
    # Ініціалізація таблиці dp
    dp = [0] * (budget + 1)
    chosen_items = [None] * (budget + 1)
    
    for item, details in items.items():
        for cost in range(budget, details['cost'] - 1, -1):
            if dp[cost] < dp[cost - details['cost']] + details['calories']:
                dp[cost] = dp[cost - details['cost']] + details['calories']
                chosen_items[cost] = item
    
    total_calories = max(dp)
    total_cost = dp.index(total_calories)
    selected_items = []
    remaining_budget = total_cost
    
    while remaining_budget > 0 and chosen_items[remaining_budget]:
        selected_items.append(chosen_items[remaining_budget])
        remaining_budget -= items[chosen_items[remaining_budget]]['cost']
    
    return selected_items, total_cost, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Виклик жадібного алгоритму
greedy_result = greedy_algorithm(items, budget)
print("Обрані страви (жадібний алгоритм):", greedy_result)

# Виклик алгоритму динамічного програмування
dp_result = dynamic_programming(items, budget)
print("Обрані страви (динамічне програмування):", dp_result)