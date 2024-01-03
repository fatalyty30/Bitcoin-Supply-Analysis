import matplotlib.pyplot as plt


def bitcoinSupply(genesis_block=50,
                  reward_per_block=50,
                  halving_interval=210_000,
                  halvings=33):
  current_reward_per_block = reward_per_block
  supply = genesis_block
  supply_values = [supply]

  for i in range(halvings):
    supply += halving_interval * current_reward_per_block
    current_reward_per_block /= 2
    supply_values.append(supply)
  return supply_values


supply_values = bitcoinSupply()

genesis_block = 50
halving_interval = 210000
x_axis = [i * halving_interval / 1000000 for i in range(len(supply_values))]
y_axis = [(value - genesis_block) / 1000000 for value in supply_values]

plt.plot(x_axis, y_axis)
plt.xlabel('Number of Blocks (Millions)')
plt.ylabel('Number of Bitcoins (Millions)')
plt.title('Bitcoin Supply')
plt.show()
