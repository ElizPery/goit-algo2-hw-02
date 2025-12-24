from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    def __init__(self, id: str, volume: float, priority: int, print_time: int):
        self.id = id
        self.volume = volume
        self.priority = priority
        self.print_time = print_time

@dataclass
class PrinterConstraints:
    def __init__(self, max_volume: float, max_items: int):
        self.max_volume = max_volume
        self.max_items = max_items

def optimize_printing(print_jobs: List[PrintJob], constraints: PrinterConstraints) -> Dict:
    """
    Optimizes the 3D printing queue according to priorities and printer constraints

    Args:
        print_jobs: List of print jobs
        constraints: Printer constraints

    Returns:
        Dict with print order and total time
    """

    # Sort jobs by priority (ascending)
    sorted_jobs = sorted(print_jobs, key=lambda job: job.priority)

    # Apply constraints
    selected_jobs = []
    current_volume = 0
    total_time = 0

    for job in sorted_jobs:
        if current_volume + job.volume <= constraints.max_volume and len(selected_jobs) <= constraints.max_items:
            selected_jobs.append(job.id)
            current_volume += job.volume
            if job.print_time > total_time:
                total_time = job.print_time
        else:
            selected_jobs.append(job.id)
            total_time += job.print_time


    return {
        "print_order": selected_jobs,
        "total_time": total_time
    }

# Testing the function
def test_printing_optimization():
    # Test 1: Models with the same priority
    test1_jobs = [
        PrintJob("M1", 100, 1, 120),
        PrintJob("M2", 150, 1, 90),
        PrintJob("M3", 120, 1, 150)
    ]

    # Test 2: Models with different priorities
    test2_jobs = [
        PrintJob("M1", 100, 2, 120),
        PrintJob("M2", 150, 1, 90), 
        PrintJob("M3", 120, 3, 150)
    ]

    # Test 3: Overriding volume constraints
    test3_jobs = [
        PrintJob("M1", 250, 1, 180),
        PrintJob("M2", 200, 1, 150),
        PrintJob("M3", 180, 2, 120)
    ]

    constraints = PrinterConstraints(max_volume=300, max_items=2)

    print("Test 1 (the same priority):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Queue order: {result1['print_order']}")
    print(f"Total time: {result1['total_time']} minutes")

    print("\\nTest 2 (different priorities):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Queue order: {result2['print_order']}")
    print(f"Total time: {result2['total_time']} minutes")

    print("\\nTest 3 (overriding volume constraints):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Queue order: {result3['print_order']}")
    print(f"Total time: {result3['total_time']} minutes")

if __name__ == "__main__":
    test_printing_optimization()

