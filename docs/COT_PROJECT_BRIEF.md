# Construct of Time — Shared Project Brief

Status: working brief for website, live stage performance and immersive installation
Updated: 2026-09-08
Owner: Tony Funiciello / DJ Aureal

## 1. Purpose

Construct of Time is one artistic world expressed through two presentation formats:

- **Live Performance** — an audiovisual stage work for festivals, concerts, clubs and live presenters.
- **Immersive Installation** — a spatial work for museums, galleries, exhibitions and art institutions.

The website should communicate one coherent Construct of Time identity while allowing each audience to enter the format most relevant to them without being forced through one very long combined scroll.

## 2. Repository and safety state

Repository: `djaureal/shape-of-now-`
Default branch: `main`

### Protected rollback baseline

Branch: `backup/pre-stage-installation-split-2026-09-08`
Commit: `63cf874989e724deb465d549b8b33632b3601332`
Message: `Replace three stage gallery stills`

This branch is the authoritative rollback point for the pre-split website and must not be modified or deleted.

### Current main at audit time

Commit: `ebfc032606a581ba29c21e3b5f9436d9cb76e40d`
Message: `Refine installation research layout`

`main` is 17 commits ahead of the protected rollback branch. It already contains a new root landing page plus `stage/index.html` and `installation/index.html`. This newer split implementation is to be treated as **existing work to review**, not as automatically approved final architecture.

### Working branch for shared brief

Branch: `project/cot-development`

No site-design implementation should be published from this branch without Tony's explicit approval.

## 3. Authoritative artistic identity

The established COT visual world should be preserved unless Tony explicitly changes it.

- Serious, underground, elegant, intelligent and contemporary.
- Dark, near-monochrome, cold desaturated silver / blue-grey palette.
- Brutalist / architectural rather than decorative.
- Real, tactile, believable environments; avoid a generic sci-fi temple or cyberpunk aesthetic.
- Raw concrete, monumental geometry, black reflective surfaces, restrained white architectural light-lines, natural shadow falloff, subtle grain and bloom.
- Avoid warm neon, fantasy spectacle, excessive haze, commercial EDM aesthetics and generic futuristic UI decoration.
- The website should feel cinematic but remain legible, calm and intentional.

## 4. Authoritative narrative tone

- Human and accessible first; scientific detail later.
- Real, down-to-earth, almost poetic, but grounded in common sense.
- The site should read like one story, not blocks of disconnected information.
- The central idea is that past and future profoundly shape us, but both are experienced only through the present.
- The research supports the artwork rather than overwhelming the opening.
- Avoid abstract language that sounds impressive without being understandable.

## 5. Approved / established website assets

### Film fragments

The web project contains the established film world around:

- `We Measure`
- `You're the Wave`
- `Beyond the End`

Web-ready HLS/poster assets are present under `media/video/hls/` and are already referenced by the site.

### Shared motion-background assets

Repository-hosted clips currently available:

- `media/video/a1.mp4`
- `media/video/a2.mp4`
- `media/video/b1.mp4`
- `media/video/b2.mp4`
- `media/video/c1.mp4`
- `media/video/c2.mp4`
- `media/video/d1.mp4`
- `media/video/d2.mp4`

### Stage imagery

The pre-split approved site includes the three audience-view stage images selected by Tony on 2026-09-08. That approved state is preserved on the rollback branch at commit `63cf874...`.

Current split-stage work should be checked against those approved images before finalising the new Stage journey.

### Stage demo

The current website references the established `We Measure` live-stage demo via CloudFront.

### Audio / score currently represented on the Stage page

Available / playable in the current implementation:

- We Measure
- You're the Wave
- Beyond the End
- Pattern
- The Arrival
- CloK

Currently marked in development / unavailable in the player:

- Threshold
- Drift
- The Return

This is implementation state, not confirmation that the final nine-work score or titles are locked.

## 6. Live stage design — current source of truth

The repository's `stage-design/README.md` identifies the following as the current design-development source of truth:

- `stage-design/COT_A101_Geometry_v1_0.json`
- `stage-design/COT_A101_Screen_Coordinates_v1_0.csv`
- `stage-design/COT_A101_Stage_Floor_Plan_v1_0.dxf`
- `stage-design/COT_A101_Stage_Floor_Plan_v1_0.svg`

Locked screen geometry recorded there:

- Seven upright rectangular LED screens.
- S1–S3 and S5–S7: 1500 mm W × 5000 mm H.
- S4 centre: 3000 mm W × 5000 mm H.
- Nominal 500 mm clear gaps in open state.
- Overall open-array width: 15000 mm.
- Progressive downstage offsets toward the outer screens.
- Converged state: left screens rotate +30°, right screens −30°.
- No forward/backward tilt.

Status remains **DESIGN DEVELOPMENT — NOT FOR CONSTRUCTION**. Mechanical engineering, support, ballast/rigging, interlocks, emergency stops and venue compliance remain supplier scope.

## 7. Immersive installation — current development state

The current `main` installation page contains:

- a dedicated immersive-installation hero;
- chapters around entering a work with no fixed beginning, multiple simultaneous presents, and the perceptual field;
- unique installation background films;
- research framing around biological / experienced time versus linear / clock time;
- an interactive real-time 3D spatial preview;
- calm and compression perceptual states with a photosensitivity warning.

The most recent repository commits specifically refine the installation research layout and restore the immersive 3D spatial visualiser. These are the latest implementation files available, but their final artistic approval status should be confirmed during review.

## 8. Website architecture — proposal for review

### Core principle

The visitor should understand the shared Construct of Time idea before choosing a format, but should not have to scroll through the entire research narrative before reaching that choice.

### Recommended shared opening

**0 · HERO**

`CONSTRUCT OF TIME`
A work by Tony Funiciello
Live Performance · Immersive Installation

Purpose: establish the world, mood and authorship immediately.

**I · ELSEWHERE**

A short human proposition: we move constantly between what happened and what might happen, yet both are being experienced now.

Purpose: make the central question understandable without explanation-heavy text.

**II · THE QUESTION / THE THRESHOLD**

A short bridge: what exactly is now, and why does lived time behave so differently from clock time?

Purpose: signal that the work is grounded in research without forcing the visitor through the full research dossier.

**III · CHOOSE THE EXPERIENCE**

Two full experiential portals:

- **LIVE PERFORMANCE** — Many people. One shared present.
- **IMMERSIVE INSTALLATION** — One work. Many presents.

Each portal should use authentic material from its respective format rather than generic UI artwork.

### Why the portal should come earlier

The current split root page already has the right conceptual direction, but it places the portal after six substantial shared chapters plus the research findings. That still reproduces part of the original length problem. The recommended new root should function as a concise cinematic prologue, then let the visitor choose.

## 9. Proposed Live Performance journey

Direct route: `/stage/`

1. **Live hero** — Many people. One shared present.
2. **Together** — the audience and shared attention.
3. **The Stage** — seven-screen architecture, three performers, approved stage imagery and demo.
4. **The Work / Score** — the nine-part audiovisual arc and available audio.
5. **Fragments from the Film World** — We Measure / You're the Wave / Beyond the End.
6. **Why Live** — embodiment, sub-bass, anticipation, darkness, silence, disappearance.
7. **Presentation / Touring layer** — format, venue flexibility, production status and booking information once confirmed.
8. **Shared artist / research / contact layer** — concise and reusable rather than duplicating the whole website.

The Stage page should feel like a performance proposition for festivals and presenters, not an installation page with stage content swapped in.

## 10. Proposed Immersive Installation journey

Direct route: `/installation/`

1. **Installation hero** — One work. Many presents.
2. **Enter** — the work is already happening when the visitor arrives.
3. **Many Presents** — different visitors construct different durations and sequences.
4. **The Field** — image, spatial sound, light and architecture become the artwork.
5. **Perceptual research** — biological / experienced time versus linear / clock time.
6. **Spatial preview / installation states** — retain the real-time 3D visualiser if approved.
7. **Research findings relevant specifically to installation behaviour** — attention, duration, prediction, sensory density, arousal, repetition.
8. **Site-responsive / institutional layer** — spatial requirements, adaptability, audience flow and presentation model once confirmed.
9. **Shared artist / research / contact layer**.

The Installation page should read as an artwork for museums and galleries, not as a concert-show page without performers.

## 11. Navigation proposal

Persistent control on both journeys:

`LIVE  /  INSTALLATION`

- Current route clearly indicated.
- One click to switch formats at any time.
- Project title links back to the shared opening.
- Both routes remain directly linkable for targeted outreach.
- Optional shared `RESEARCH`, `ARTIST` and `CONTACT` access can remain consistent across both journeys.

Do not make two independent sites or duplicate the shared foundation unnecessarily.

## 12. Development tracks

### A. Website

Status: architecture review

Next decision: approve / revise the concise shared opening and the two journey structures before further implementation.

### B. Stage design

Status: separate design-development track

Source of truth: A101 geometry files in `stage-design/`.

Do not alter locked geometry as part of website work.

### C. Immersive installation

Status: separate artistic / spatial development track

Current website visualiser and research framing are implementation references. Spatial, technical and institutional requirements should be developed independently from the Stage design.

## 13. Missing / unresolved information

- Confirm whether the current split implementation on `main` is approved work, experimental work, or simply the latest draft from another task.
- Confirm the exact amount of shared material before the Stage / Installation portal. Recommendation: hero + two short conceptual chapters only.
- Confirm whether the six scientific findings should live on a dedicated shared Research page, be selectively reused inside each journey, or both.
- Confirm final Stage track list, order and availability for Threshold, Drift and The Return.
- Confirm final installation technical requirements: room envelope, screen/projection configuration, sound system, lighting, visitor capacity/flow and minimum/ideal venue conditions.
- Confirm live-performance technical/presentation information for festival and touring buyers.
- Confirm which CloudFront-hosted stage and installation assets are considered permanent production assets versus temporary references.
- Confirm whether the approved three stage images should be reinstated prominently in the new Stage route.
- Confirm final artist/contact presentation and whether sales/presenter information should differ between Stage and Installation routes.
- Complete mobile and accessibility review, including motion/video fallbacks and photosensitivity handling.

## 14. Change-control rule

- The protected backup branch is never modified.
- `main` is not to be changed by this development task until Tony explicitly approves implementation / publishing.
- Architecture and copy changes are reviewed before implementation.
- Website, stage design and installation remain separate development tracks.
- This brief is updated when Tony explicitly approves a decision, so approved work and unresolved questions remain distinguishable.
