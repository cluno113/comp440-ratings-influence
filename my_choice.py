"""
Your choice rule, for Part 3.

You design the rule. Claude asks you questions about it, writes it here from your answers, and
shows you the code. Then `uv run python hand_check.py` shows each step of your rule on a
two-artist case, so you can say whether each step does what you meant.
"""

from artists import TRUE_POPULARITY
from choose import normalize, step


def my_choice(shown, counts, social_influence):
    """Return the chance that a user picks each shown artist: a list of numbers, one per artist
    in `shown` and in the same order, summing to 1.

    shown              the artists on the list, top first (positions 0, 1, 2, ...)
    counts             the download counts shown with the artists, artist -> number; an artist
                       shown without a count is missing, so read it as counts.get(artist, 0)
    social_influence   from 0 (users ignore the counts) to 1 (users go by the counts alone)

    The rule may use `normalize`, which scales a list of weights so they sum to 1, and
    TRUE_POPULARITY, which gives each artist its hidden true popularity. `step` labels each
    stage of the rule, so that hand_check.py can show it.
    """
    taste = step("taste share: true popularity scaled to sum to 1",
                 normalize([TRUE_POPULARITY[artist] for artist in shown]))

    # Rank the shown artists by count, lowest first (0, 1, 2, ...). Artists with the same count
    # share a rank: the average of the places they fill.
    shown_counts = [counts.get(artist, 0) for artist in shown]
    ranks = []
    for count in shown_counts:
        below = sum(1 for c in shown_counts if c < count)
        same = sum(1 for c in shown_counts if c == count)
        ranks.append(below + (same - 1) / 2)
    ranks = step("rank by count: 0 for the fewest downloads, ties share a rank", ranks)

    # The 30th percentile sits 30% of the way from the lowest rank to the highest.
    target = 0.3 * (len(shown) - 1)
    distance = step("places from the 30th percentile rank: |rank - 0.3 * (number shown - 1)|",
                    [abs(r - target) for r in ranks])

    # Each place further from the 30th percentile keeps 0.9 of the pull.
    pulls = step("count pull: 0.9 ** places from the 30th percentile",
                 [0.9 ** d for d in distance])
    social = step("social share: the count pulls scaled to sum to 1", normalize(pulls))

    # An even mix: social_influence of the social share, the rest from taste.
    mixed = step("mix: (1 - social_influence) * taste + social_influence * social",
                 [(1 - social_influence) * t + social_influence * s
                  for t, s in zip(taste, social)])

    # Position pull is the same for every spot on the list.
    position = step("position pull: 1 for every spot", [1 for _ in shown])
    weighted = step("mix times position pull", [m * p for m, p in zip(mixed, position)])
    return step("chance: the weighted mix scaled to sum to 1", normalize(weighted))
