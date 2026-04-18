from rapidfuzz import fuzz


def duration_score(local_duration, remote_duration):
    diff = abs(local_duration - remote_duration)

    if diff <= 2:
        return 1.0
    elif diff <= 5:
        return 0.7
    elif diff <= 10:
        return 0.4
    else:
        return 0.0


def compute_score(local_meta, candidate):
    title_score = fuzz.ratio(
        local_meta["title"],
        candidate.get("title", "")
    ) / 100

    artist_remote = candidate.get("artist-credit")[0]["name"]

    artist_score = fuzz.ratio(
        local_meta["artist"],
        artist_remote
    ) / 100

    remote_duration = int(candidate.get("length", 0)) // 1000

    dur_score = duration_score(
        local_meta["duration"],
        remote_duration
    )

    final_score = (
        title_score * 0.4 +
        artist_score * 0.3 +
        dur_score * 0.3
    )

    return round(final_score, 3)
