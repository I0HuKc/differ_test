import sys
import random
import io
import os

from typing import List, Tuple

from place import Place


def read_file(f_path: str) -> List[Place]:
    data: List[Place] = []

    with open(f_path, 'rb') as f:
        CHUNK_SIZE = 1024

        fi = io.FileIO(f.fileno())
        fb = io.BufferedReader(fi)

        while True:
            block = fb.read(CHUNK_SIZE)
            if block:
                # 1. convert byte to string
                csv_data = str(block)[2:-1]
                # 2. convert string to csv
                for row in csv_data.split('\\n')[1:]:
                    if len(row.split(",")) == 3:
                        nm, lt, lg = row.split(",")
                        data.append(Place(nm, float(lt), float(lg)))
            else:
                break

    return data


def main():
    file_path = 'places.csv'

    if os.path.exists(file_path):
        data: List[Place] = read_file(file_path)

        # Checking if the specified argument exists
        n = 0
        if len(sys.argv) > 1:
            try:
                n = int(sys.argv[1])
            except ValueError:
                print(
                    "Invalid argument type, expect `int`. Received `{at}`"
                    .format(
                        at=type(sys.argv[1]).__name__
                    )
                )
        else:
            n = random.randint(0, len(data)-1)

        # Define a reference point
        departure_p: Place = data[n]
        data_nd: List[Tuple[str, float]] = []

        for place in data:
            if place != departure_p:
                distance = departure_p.distance(place)

                data_nd.append((place.name, distance))

        # Sorting
        print("\n--- ALL PAIRS OF PLACES AND DISTANCES IN ASCENDING ORDER ---\n")
        data_nd.sort(key=lambda x: x[1])
        avg_sum = 0

        for row in data_nd:
            avg_sum += row[1]
            print("Distance from {n1} to {n2} >> {d} km.".format(
                n1=departure_p.name,
                n2=row[0],
                d=row[1]
            ))

        # Arithmetic mean and nearest pair
        avg = round(avg_sum / len(data_nd), 2)
        nearest = min(data_nd, key=lambda x: abs(x[1] - avg))

        print("Average distance: {avg} km. Closest pair: {n1} – {n2} {d} km.".format(
            avg=avg,
            n1=departure_p.name,
            n2=nearest[0],
            d=nearest[1],
        ))

    else:
        print("Error: file `{fp}` is not found.".format(fp=file_path))
        sys.exit()


if __name__ == '__main__':
    main()
