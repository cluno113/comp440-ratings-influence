# Ratings and social influence: writeup

Claude writes your answers into the slots below as you say them. You may ask it to change any of
your answers at any time, except the Part 0 predictions. Every `XXXX` in Parts 0 to 5 needs an
answer; the follow-up slots at the end are optional.

**Name:** Claire Kuno
**Date:** 2026-09-24

## Part 0. Predictions

Answered before anything runs. Claude writes them in as you said them, and they stay as written.

**1. Once people can see the counts, which artist wins most often?** Once people can see the download counts, the inequality of downloads of the most popular (100) and the least, will be drastic with most downloads going towards the top 100.

**2. Does inequality rise or fall with social influence?** Inequality will rise with social influence as people tend to trust what gets recommended to them. The stand out songs will be streamed more commonly.

**3. Does the best artist ever lose a world?** Yes, it is possible for a best artist to lose a world because music taste is subjective, but out of 100 artists there will be a clear more popular, versus least popular. I doubt that a top artist will ever be the least popular in any world.

**4. Can a recommender lower inequality without lowering fidelity to true taste?** A recommender rule can lower inequality without making the outcome track less well by highlighting popular artists from a variety of genres.

## Part 1. Users on their own

Code: `part1_independent.py`. Figure: `figures/part1_strip.png`.

**What Gini and unpredictability each show, in your own words:** Gini and unpredicability both measure the inequality between a popular artist and an unpopular artist's streams. The Gini index reveals the inequality of streams distributed across artists within a world. The unpreditability is how much an artist's share differs between worlds. The Gini of .277 shows that there is variability with streams across artists. But the unpredictability goes to show how a popular artist remains popular across different worlds.

**What the figure shows, one sentence:** The figure shows how the top artists ranked in artist popularity receive more downloads while less popular artists receive less downloads.

## Part 2. The recommender

Code: `recommender.py`, `part2_recommender.py`. Figure: `figures/part2_strip.png`.

**The capabilities and limitations of `top_five`, in your words:** top_five shows the five most-downloaded artists with the most downloaded first (based on download counts). Then, it adds random artists only while fewer than five artists have any downloads. After that, its just the top five in order. The limitations are that it will keep the most popular artist in its mix, making it hard for allowing artists that are close to the top to be considered in the shuffle.

**What Claude corrected in your reading, in your words, or "nothing":** It corrected my interpretation of how top_five incorporated the randomizing aspect.

**What changed against Part 1, one sentence:** The inequality got worse as well as the unpredictability between other worlds.

## Part 3. Social influence

Code: `my_choice.py`, `hand_check.py`, `part3_influence.py`. Figures: `figures/part3_gini.png`,
`figures/part3_unpredictability.png`.

**Your rule in your words:** XXXX

**Hand check, before the table: which artist your rule should favor, and by a little or a lot:** XXXX

**Hand check: whether the table matched what you said:** XXXX

**The shape you expect the two curves to have, as you told Claude before the run:** XXXX

**What you changed in your rule, at the hand check or after the run, or "nothing":** XXXX

**What the two curves show against the paper's Figures 1 and 2, in one or two sentences:** XXXX

**Revisited: which of your Part 0 predictions you would now change, and why:** XXXX

## Part 4. Your recommender

Code: `my_recommender.py`, `part4_recommender.py`. Figure: `figures/part4_recommenders.png`.

**Your rule in words, before any code:** XXXX

**What you expect it to do to inequality, unpredictability and fidelity, as you told Claude before the run:** XXXX

**What it bought and what it cost, one sentence:** XXXX

## Part 5. Reflection

**Where this shows up in data you have already handled, or in an interface you use, one sentence:** XXXX

**A moment Claude was wrong or overconfident, or a judgment you kept for yourself, one sentence:** XXXX

## Follow-ups

Optional, and not graded. Nothing under this heading is ever counted as missing: leave a slot as
`XXXX` if you did not do that follow-up.

**What is shown (`followup_shown.py`): which market moved success further from quality:** XXXX

**One assumption (`followup_assumption.py`): the assumption you changed:** XXXX

**One assumption: whether the Part 3 conclusion survived:** XXXX

**Anything else you tried:** XXXX

**Anything else: what it showed:** XXXX
