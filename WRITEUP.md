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

**Your rule in your words:** I initially wanted popularity in download counts and position to matter, but the artists chosen in the hand-check left me with insane biase towards Justin Bieber. So, I changed my rule to ensure that my rule would pick Justin.

**Hand check, before the table: which artist your rule should favor, and by a little or a lot:** My ryle should favor Justin Bieber. By a lot.

**Hand check: whether the table matched what you said:** No it does not.

**The shape you expect the two curves to have, as you told Claude before the run:** I think that it would be more equal because my rule gives music underdogs a chance.

**What you changed in your rule, at the hand check or after the run, or "nothing":** I changed the most influential artist pool by moving from considering popularity, to targetting the 30th percentile.

**What the two curves show against the paper's Figures 1 and 2, in one or two sentences:** It is doing the opposite now where social influence decreases inequality because I am highlighting artist who would have typically gotten extremely unpopular with a rise in social influence.

**Revisited: which of your Part 0 predictions you would now change, and why:** I would change 2. as inequality will fall with social influence. 3. because a best artist is chosen at the 30th percentile.

## Part 4. Your recommender

Code: `my_recommender.py`, `part4_recommender.py`. Figure: `figures/part4_recommenders.png`.

**Your rule in words, before any code:** My rule looks at artists closest to the 30th percentile in popularity of downloads.

**What you expect it to do to inequality, unpredictability and fidelity, as you told Claude before the run:** I believe it will decrease inequality by highlighting those who are not given recognition when social influences hikes up the downloads of already popular artists. It will be unpredictable in its randomness in choosing between artists. But, will consistently produce the same range of artists.

**What it bought and what it cost, one sentence:** My rule actively pushes against social influence with a higher Gini score than the random_five. But, it cost is seen in the fidelity where highlighting only the 30th percentile misses out on good popular artists.

## Part 5. Reflection

**Where this shows up in data you have already handled, or in an interface you use, one sentence:** This shows up consistently across every app I use. From depop to instagram, I feel like cycling through different parcels of content reveals patterns that I can detect by looking at number of likes or time things are posted

**A moment Claude was wrong or overconfident, or a judgment you kept for yourself, one sentence:** A moment Claude was overconfident was when it kept asking me to answer questions with one word or sentence. Whenever I would do so, it would never be enough context for claude to build an algorithm.

## Follow-ups

Optional, and not graded. Nothing under this heading is ever counted as missing: leave a slot as
`XXXX` if you did not do that follow-up.

**What is shown (`followup_shown.py`): which market moved success further from quality:** XXXX

**One assumption (`followup_assumption.py`): the assumption you changed:** XXXX

**One assumption: whether the Part 3 conclusion survived:** XXXX

**Anything else you tried:** XXXX

**Anything else: what it showed:** XXXX
