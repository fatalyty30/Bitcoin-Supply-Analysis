def bitcoinMaxSupply(genesis_block=50,
                     reward_per_block=50,
                     halving_interval=210_000,
                     halvings=33):
  current_reward_per_block = reward_per_block
  supply = genesis_block

  for i in range(halvings):
    supply += halving_interval * current_reward_per_block
    current_reward_per_block /= 2
  return supply - genesis_block


max_supply = bitcoinMaxSupply()
print("Bitcoin supply at the end of the last halving:", max_supply)
