# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "exif>=1.6.1",
# ]
# ///

import json
from glob import glob

from exif import Image


def to_decimal(degrees, minutes, seconds):
    return degrees + minutes / 60 + seconds / 3600


def main() -> None:
    output = []

    paths = glob("images/*.JPG")
    for path in paths:
        with open(path, "rb") as file:
            bytes_ = file.read()
        image = Image(bytes_)
        if not hasattr(image, "gps_latitude"):
            continue
        data = {
            "path": path,
            "latitude": to_decimal(*image.gps_latitude),
            "longitude": to_decimal(*image.gps_longitude),
        }
        print(path, data)
        output.append(data)

    with open("geolocations.json", "w") as file:
        file.write(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
