🧱 PHASE 1 — Architecture Design (No Code Yet)
1️⃣ Define Core Modules

You will have 7 modules:

Scanner

Metadata Extractor

Fingerprint Engine

Search Service

Scoring Engine

Genre Resolver

Tag Writer

Draw this flow on paper.

2️⃣ Define Your Internal Data Model

Implement your Track schema as a Python class or dataclass.

This is your truth layer.

Everything must convert into this model before writing tags.

3️⃣ Define Matching Strategy

Write down:

Weights

Confidence threshold

Duration tolerance

Apple compatibility rules

This avoids rewriting logic later.

🛠 PHASE 2 — Core MVP Implementation
STEP 1 — Folder Scanner

Goal:

Recursively scan folder

Detect supported audio formats

Send file path to pipeline

Keep it simple.

STEP 2 — Metadata Extractor

Use mutagen.

Extract:

Title

Artist

Album

Duration

Do NOT write anything yet.

Just print results to console.

STEP 3 — Integrate MusicBrainz

Use:

MusicBrainz API

Implement:

search_track(title, artist)

Return structured results.

Still no writing.

STEP 4 — Build Scoring Engine

Implement:

Fuzzy matching (rapidfuzz)

Duration comparison

Weighted scoring

Test manually with 5–10 files.

Print:

File → Best candidate → Confidence score

If confidence < threshold → skip.

This is where most intelligence lives.

STEP 5 — Tag Writing

Now implement:

Remove old ID3

Write ID3v2.4 fresh

Embed:

TIT2

TPE1

TPE2

TALB

TDRC

TCON

TRCK

APIC

Test with 1 file first.

Open it in:

iTunes / Apple Music

VLC

Confirm:

No artist duplication

Artwork displays correctly

🧠 PHASE 3 — Robustness Upgrade

Now make it professional.

STEP 6 — Add Fingerprinting

Integrate:

AcoustID

Flow:

If metadata match < 0.5
    → fingerprint
    → retry search

Now your tool can handle broken files.

STEP 7 — Add Artwork Fallback

If no artwork in primary result:

Query Cover Art Archive

Resize image before embedding (avoid 10MB covers).

STEP 8 — Genre Strategy

Collect genres from source

Select primary

Store secondary in custom tag

Test Apple compatibility again.

🎵 PHASE 4 — Lyrics Integration

Now add:

LRCLIB for synced lyrics

Genius for fallback

Embed:

USLT

SYLT

Test:

VLC

Apple Music

Note: Apple may ignore SYLT.

⚙️ PHASE 5 — Performance & Scaling

Now optimize.

For large libraries:

Add SQLite cache:

Store MBID

Store ISRC

Store fingerprint hash

This avoids re-querying APIs.

Add:

Rate limiting

Retry logic

Error logging

🧪 PHASE 6 — Testing Strategy

Create test folder:

Clean file

No metadata

Wrong metadata

Live version

Remastered version

Multi-genre

Featuring artist

Run pipeline and verify results.

Keep logs.

🧼 PHASE 7 — Stability & Safety

Add:

Automatic file backup before writing

Dry-run mode (preview changes without writing)

Manual review export (CSV)

Never write blindly.

📦 PHASE 8 — Packaging

Options:

CLI tool

Add progress bar

Add configuration file:

Threshold

Genre strategy

Apple mode on/off

Later:

GUI with PyQt

Or local web UI