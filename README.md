# Delivery System Assignment

## Approach

1. Read warehouse, agent and package data from JSON files.
2. For each package, find the nearest agent to the package warehouse.
3. Calculate:
   - Agent → Warehouse distance
   - Warehouse → Destination distance
4. Assign package to the nearest agent.
5. Generate delivery statistics:
   - Packages delivered
   - Total distance traveled
   - Efficiency
6. Determine the best performing agent.

## Assumptions

1. The nearest available agent is always selected.
2. If two agents are at the same distance, the first agent encountered in the data is selected.
3. Agents have unlimited delivery capacity.
4. Agents become instantly available after completing a delivery.
5. No traffic, delay, or delivery time constraints are considered.
6. Euclidean distance is used for all distance calculations.
7. All coordinates provided in input files are valid.
8. Efficiency is calculated as:

   Efficiency = Total Distance / Packages Delivered

9. Agent with the lowest efficiency value is considered the best agent.

## Output

A report JSON file is generated for every test case containing:
- Packages delivered
- Total distance
- Efficiency
- Best agent
