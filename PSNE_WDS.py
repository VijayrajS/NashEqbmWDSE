import numpy as np

"""#Input transformation"""

n = int(input())
n_strat = [int(u) for u in input().split()]

U_i = np.reshape(np.array([float(u) for u in input().split()]), n_strat[::-1]+[n])
# to access the value from the payoff matrix, the strategy profile is reversed, e.g. S = 1121 == U_np[0,1,0,0]

# stores whether each strategy profile is a psne
status_psne = np.ones(n_strat[::-1])

# << WDS
wds_out = list()          # store final WDS for each player
# WDS >>

for player in range(n):
  # obtain max payoff of current player for every strategy profile S_-i
  maxes = np.max(U_i, axis=n-player-1)
  n_pp = list(n_strat)
  n_pp.pop(player)
  # list of all S_-i for the player
  indices = [list(i) for i in list(np.ndindex(tuple(n_pp[::-1])))]

  # << WDS
  status_wds = np.ones(n_strat[player])
  # WDS >>

  for index in indices:
    # obtaining max payoff for each S_-i
    max_i = maxes[tuple(index)][player]
    index.insert(n-player-1, 0)

    # iterating through all the strategies of the current player
    for i in range(n_strat[player]):
      index[n-player-1] = i
      strat_profile = tuple(index)

      # only present if maximal profile for all players, hence 'and'
      check = (max_i == U_i[strat_profile][player])
      # psne
      status_psne[strat_profile] = status_psne[strat_profile] and check
      # wds
      status_wds[i] = status_wds[i] and check

  # << WDS
  wds_i = []

  for idx in range(len(status_wds)):
    # check if count for strategy s_i is equal to number of s_-i strategies
    if status_wds[idx]:
      wds_i.append(idx)

  wds_out.append(str(len(wds_i)) + ' ' + ' '.join([str(u+1) for u in wds_i]))
  # WDS >>

# number of true (=1) values gives the number of psne
n_psne = np.sum(status_psne)
print(int(n_psne))
psne = np.ndindex(np.shape(status_psne))
for eq in psne:
  if status_psne[eq]:
    print(' '.join([str(u+1) for u in eq[::-1]]))

# << WDS
for out in wds_out:
  print(out)
# WDS >>