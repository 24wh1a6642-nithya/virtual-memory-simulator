#!/usr/bin/env python3
"""
Test script for Virtual Memory Simulator
Demonstrates the simulator with predefined test cases.
"""

from virtual_memory_simulator import PageReplacementSimulator, print_algorithm_results, print_comparison_table


def run_test_case(name: str, num_frames: int, reference_string: list):
    """Run a test case with given parameters and improved formatting."""
    print(f"\n╔{'═' * 78}╗")
    print(f"║{f'  TEST CASE: {name}':^78}║")
    print(f"╚{'═' * 78}╝")
    print(f"📋 Configuration: {num_frames} frames")
    print(f"📄 Reference String: {' → '.join(map(str, reference_string))}")
    
    # Create simulator and run algorithms
    simulator = PageReplacementSimulator(num_frames, reference_string)
    results = simulator.run_all_algorithms()
    
    # Print results for each algorithm
    for algo_name in ['FIFO', 'LRU', 'Optimal']:
        print_algorithm_results(results[algo_name], num_frames)
    
    # Print comparison
    print_comparison_table(results)


def main():
    """Run predefined test cases with improved presentation."""
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "VIRTUAL MEMORY SIMULATOR - TEST SUITE" + " " * 19 + "║")
    print("║" + " " * 78 + "║")
    print("║  Comprehensive testing of FIFO, LRU, and Optimal algorithms     ║")
    print("╚" + "═" * 78 + "╝")
    
    # Test Case 1: Classic example
    run_test_case(
        "Classic Example (Textbook Case)",
        3,
        [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    )
    
    # Test Case 2: Simple sequence
    run_test_case(
        "Simple Sequential Access",
        4,
        [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    )
    
    # Test Case 3: Repeated pattern
    run_test_case(
        "Repeated Pattern (High Locality)",
        2,
        [1, 2, 1, 2, 1, 2, 3, 1, 2]
    )
    
    print(f"\n🎯 All test cases completed successfully!")
    print(f"💡 Notice how Optimal consistently performs best, followed by LRU, then FIFO")


if __name__ == "__main__":
    main()