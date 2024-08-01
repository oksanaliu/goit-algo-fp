import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків двох кубиків
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

# Функція для проведення симуляції методом Монте-Карло
def monte_carlo_simulation(num_rolls):
    sums = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        dice1, dice2 = roll_dice()
        dice_sum = dice1 + dice2
        sums[dice_sum] += 1
    
    probabilities = {s: (count / num_rolls) * 100 for s, count in sums.items()}
    return probabilities

num_rolls = 1000000

probabilities = monte_carlo_simulation(num_rolls)

analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

print("Ймовірності за методом Монте-Карло:")
for sum_val, prob in probabilities.items():
    print(f"Сума {sum_val}: {prob:.2f}%")

print("\nАналітичні ймовірності:")
for sum_val, prob in analytical_probabilities.items():
    print(f"Сума {sum_val}: {prob:.2f}%")

# Побудова графіку
sums = list(range(2, 13))
mc_probs = [probabilities[sum_val] for sum_val in sums]
analytical_probs = [analytical_probabilities[sum_val] for sum_val in sums]

plt.plot(sums, mc_probs, label='Монте-Карло', marker='o')
plt.plot(sums, analytical_probs, label='Аналітичні', marker='x')
plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірності сум при киданні двох кубиків')
plt.legend()
plt.grid(True)
plt.show()