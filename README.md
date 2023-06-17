# Stardew Valley Crop Profit Calculator

This program can take a hypothetical crop field and tell you the expected harvest and profit. It can take into account things like the player's farming level, whether the crop has regrowth, fertilizer use, etc.

It can be used to see how much profit a crop field will produce once it is harvested, but it can also be used to compare crops to see which is more profitable as well make informed decisions about what crops should be planted and when to make the maximal amount of money in a year.

Profits can be calculated as total gold or—when comparing profitability of crops—as gold per day. There are a lot of probabilities involved, so the numbers generated are average expected gold from the given crop field.

## Rationale

There are a lot of questions I had such as: what crop is the most profitable in the game under any circumstances and what those circuistances are; which crop is the most profitable during any given season; is it better to buy seeds or use a seed maker and if so when; and more.

Enough clues to reverse engineer the game's calculations can be pulled from the wiki, but there is at least a dozen different variables to consider and when you want to compare many different scenarios or answer very many questions at all, it quickly becomes a bit too much calculating for such a casual game. So instead, the computer can do all the calculations.