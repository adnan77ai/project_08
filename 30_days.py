print("30 Days Down - What did you think?")
print()
for i in range (1,31):
  thought = input (f'Day {i}:\n')
  print()
  feeling = (f'You think that Day {i} was {thought}')
  print()
  print(f'{feeling:^35}')
  print(f'{thought:^35}')