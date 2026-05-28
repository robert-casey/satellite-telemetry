import json

def parse_gp_data(gp_record):
    return {
        "object_name": gp_record.get("OBJECT_NAME"),
        "norad_id": gp_record.get("NORAD_CAT_ID"),
        "epoch": gp_record.get("EPOCH"),
        "inclination": float(gp_record.get("INCLINATION", 0)),
        "eccentricity": float(gp_record.get("ECCENTRICITY", 0)),
        "mean_motion": float(gp_record.get("MEAN_MOTION", 0)),
        "apoapsis": float(gp_record.get("APOAPSIS", 0)),
        "periapsis": float(gp_record.get("PERIAPSIS", 0)),
        "period": float(gp_record.get("PERIOD", 0)),
        "tle_line1": gp_record.get("TLE_LINE1"),
        "tle_line2": gp_record.get("TLE_LINE2"),
    }

if __name__ == "__main__":
    with open("data/tle_raw.json") as f:
        raw = json.load(f)

    parsed = [parse_gp_data(record) for record in raw]

    for satellite in parsed:
        print(json.dumps(satellite, indent=2))
        print("---")