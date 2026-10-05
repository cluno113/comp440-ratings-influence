"""
Your recommender, for Part 4.

Describe your rule to Claude in words first. Claude writes it here, and part4_recommender.py
compares it with top_five and random_five from recommender.py, which are written the same way.
"""

from sim import ARTISTS, NUM_SHOWN


def my_recommender(counts, rng):
    """Return two things: five different artist names in display order (position 0 is the top of
    the list), and the download counts to show with them, artist -> number.

    counts  downloads so far in this world, artist -> int; an artist with no downloads yet is
            missing, so read it as counts.get(artist, 0)
    rng     a numpy random generator; use it for anything random, so that runs repeat exactly

    The counts you return are the counts the user sees, and they are what the choice rule reads.
    Return `counts` to show the real counts, `{}` to show no counts at all, or a dict of your own
    to show changed numbers.

    A recommender may use the counts and the list of artists (sim.ARTISTS). It must never use
    TRUE_POPULARITY: a real recommender cannot see how much users truly like each artist.
    """
    # "Slightly underground": show the five artists whose download ranks are closest to the
    # 30th percentile, closest at the top.
    all_counts = {artist: counts.get(artist, 0) for artist in ARTISTS}

    # Rank all artists by downloads, 0 for the fewest. Artists with the same count share a
    # rank: the average of the places they fill.
    ranks = {}
    for artist, count in all_counts.items():
        below = sum(1 for c in all_counts.values() if c < count)
        same = sum(1 for c in all_counts.values() if c == count)
        ranks[artist] = below + (same - 1) / 2

    # The 30th percentile sits 30% of the way from the lowest rank to the highest.
    target = 0.3 * (len(ARTISTS) - 1)

    # Closest to the 30th percentile first; among equally close artists, more downloads first;
    # among artists still tied, a random order.
    tiebreak = {artist: rng.random() for artist in ARTISTS}
    order = sorted(ARTISTS, key=lambda artist: (abs(ranks[artist] - target),
                                                -all_counts[artist], tiebreak[artist]))
    return order[:NUM_SHOWN], counts
