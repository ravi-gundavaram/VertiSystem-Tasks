import os
import json
import random
from datetime import datetime, timedelta
from collections import defaultdict
import numpy as np

# Constants
NUM_FILES = 5000
MIN_RECORDS = 50
MAX_RECORDS = 100
CITIES = [f"City_{i}" for i in range(100, 300)]
NULL_PROBABILITY = 0.001  # Between 0.5%-0.1%
OUTPUT_DIR = "/tmp/flights/"

def generate_flights_data():
    """Generates random flight records."""
    records = []
    for _ in range(random.randint(MIN_RECORDS, MAX_RECORDS)):
        record = {
            "date": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
            "origin_city": random.choice(CITIES),
            "destination_city": random.choice(CITIES),
            "flight_duration_secs": random.randint(1800, 43200),  # 30 minutes to 12 hours
            "passengers_on_board": random.randint(50, 300),
        }
        # Introduce null values with probability
        if random.random() < NULL_PROBABILITY:
            record[random.choice(list(record.keys()))] = None
        records.append(record)
    return records

def generate_files():
    """Generates JSON files with random flight data."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for i in range(NUM_FILES):
        origin_city = random.choice(CITIES)
        file_name = f"{datetime.now().strftime('%m-%Y')}-{origin_city}-flights.json"
        file_path = os.path.join(OUTPUT_DIR, file_name)
        with open(file_path, "w") as f:
            json.dump(generate_flights_data(), f)

def analyze_files():
    """Analyzes and cleans the generated files."""
    total_records = 0
    dirty_records = 0
    city_stats = defaultdict(lambda: {"in": 0, "out": 0, "durations": []})
    start_time = datetime.now()

    for file_name in os.listdir(OUTPUT_DIR):
        file_path = os.path.join(OUTPUT_DIR, file_name)
        with open(file_path, "r") as f:
            data = json.load(f)
            total_records += len(data)
            for record in data:
                if None in record.values():
                    dirty_records += 1
                    continue
                origin = record["origin_city"]
                destination = record["destination_city"]
                duration = record["flight_duration_secs"]
                passengers = record["passengers_on_board"]
                city_stats[destination]["in"] += passengers
                city_stats[origin]["out"] += passengers
                city_stats[destination]["durations"].append(duration)

    top_cities = sorted(
        city_stats.items(),
        key=lambda x: sum(x[1]["durations"]),
        reverse=True
    )[:25]
    avg_and_p95 = {
        city: {
            "AVG_duration": np.mean(stats["durations"]),
            "P95_duration": np.percentile(stats["durations"], 95)
        } for city, stats in top_cities
    }
    max_arrived = max(city_stats.items(), key=lambda x: x[1]["in"])
    max_left = max(city_stats.items(), key=lambda x: x[1]["out"])

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    return {
        "total_records": total_records,
        "dirty_records": dirty_records,
        "duration": duration,
        "avg_and_p95": avg_and_p95,
        "max_arrived_city": max_arrived,
        "max_left_city": max_left
    }

if __name__ == "__main__":
    print("Generating files...")
    generate_files()
    print("Analyzing files...")
    results = analyze_files()
    print("Analysis Results:")
    print(json.dumps(results, indent=4))
