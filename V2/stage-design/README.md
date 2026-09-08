# Construct of Time — Stage Design Handoff

## A101 source of truth

The current design-development source of truth is `COT_A101_Geometry_v1_0.json` plus `COT_A101_Screen_Coordinates_v1_0.csv`.

Coordinate system: origin at the centre of S4; +X is stage right; +Y is upstage; audience/downstage is negative Y. Units are millimetres.

### Locked screen geometry

- 7 upright rectangular LED screens total.
- S1–S3 and S5–S7: 1500 mm W × 5000 mm H.
- S4 centre: 3000 mm W × 5000 mm H, fixed at 0°.
- Nominal open-state clear gap between every adjacent screen: 500 mm.
- Open array overall width: 15000 mm.
- S3/S5 are 500 mm downstage of S4.
- S2/S6 are 1000 mm downstage of S4.
- S1/S7 are 1500 mm downstage of S4.
- Converged state: S1–S3 rotate +30°; S5–S7 rotate −30° around a vertical axis through each screen centre.
- In top view with audience downstage, the left screens read `/` and the right screens read `\`.
- No forward/backward tilt.

### Supplier scope

The staging supplier is to engineer and certify the rotating bases/platforms, pivot/drive system, support structure, ballast or rigging, loads, movement limits, safety interlocks, emergency stops and venue/local compliance. The CAD files define design intent and movement envelope, not the mechanical solution.

## Files

- `COT_A101_Stage_Floor_Plan_v1_0.dxf` — CAD exchange drawing; intended for import into Vectorworks Spotlight, AutoCAD or equivalent.
- `COT_A101_Stage_Floor_Plan_v1_0.svg` — vector preview / reference drawing.
- `COT_A101_Screen_Coordinates_v1_0.csv` — exact screen coordinate schedule.
- `COT_A101_Geometry_v1_0.json` — machine-readable design geometry and supplier-scope notes.

## Current stage envelope

An 18000 × 10000 mm stage envelope is shown as a preliminary working recommendation only. Performer zones are also provisional. These are the next items to validate against access, PA, lighting, monitor, cable, sightline and festival-production requirements.

**Status: DESIGN DEVELOPMENT — NOT FOR CONSTRUCTION.**
