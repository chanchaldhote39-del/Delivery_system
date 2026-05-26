import json
import math


def calculate_distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


def process_file(filename):

    with open(filename, "r") as file:
        data = json.load(file)

    warehouses = data["warehouses"]
    agents = data["agents"]
    packages = data["packages"]

    report = {}

    # Initialize report
    for agent_id in agents:
        report[agent_id] = {
            "packages_delivered": 0,
            "total_distance": 0
        }

    # Process packages
    for package in packages:

        warehouse_name = package["warehouse"]
        warehouse_location = warehouses[warehouse_name]

        destination = package["destination"]

        nearest_agent = None
        min_distance = float("inf")

        for agent_id, agent_location in agents.items():

            d = calculate_distance(
                agent_location,
                warehouse_location
            )

            if d < min_distance:
                min_distance = d
                nearest_agent = agent_id

        delivery_distance = calculate_distance(
            warehouse_location,
            destination
        )

        total_trip = min_distance + delivery_distance

        report[nearest_agent]["packages_delivered"] += 1
        report[nearest_agent]["total_distance"] += total_trip

    # Efficiency
    for agent_id in report:

        delivered = report[agent_id]["packages_delivered"]

        if delivered > 0:
            report[agent_id]["efficiency"] = round(
                report[agent_id]["total_distance"] / delivered,
                2
            )
        else:
            report[agent_id]["efficiency"] = 0

        report[agent_id]["total_distance"] = round(
            report[agent_id]["total_distance"],
            2
        )

    # Best Agent
    best_agent = min(
        [a for a in report if report[a]["packages_delivered"] > 0],
        key=lambda x: report[x]["efficiency"]
    )

    report["best_agent"] = best_agent

    output_file = (
        filename.replace(".json", "_report.json")
    )

    with open(output_file, "w") as file:
        json.dump(report, file, indent=4)

    print(f"\nReport Generated: {output_file}")
    print(json.dumps(report, indent=4))


# Run Test Case 1
# process_file("test_cases/test_case_1.json")


for i in range(1, 11):
    process_file(f"test_cases/test_case_{i}.json")