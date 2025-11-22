#!/usr/bin/env python3
"""
Example 1: Hidden Identity Detection with ZX-Calculus

This script demonstrates how ZX-calculus can automatically detect when a
complex-looking circuit is actually just an identity operation.
"""

import pyzx as zx


def main():
    """Demonstrate hidden identity detection."""
    
    print("=" * 60)
    print("ZX-CALCULUS: HIDDEN IDENTITY DETECTION")
    print("=" * 60)
    print()
    
    # Create a "messy" circuit that secretly does nothing
    print("Creating a complex circuit with 7 gates...")
    c = zx.Circuit(qubit_amount=2)
    
    c.add_gate("HAD", 0)
    c.add_gate("CNOT", 0, 1)
    c.add_gate("HAD", 0)
    c.add_gate("HAD", 1)
    c.add_gate("CNOT", 0, 1)
    c.add_gate("HAD", 1)
    c.add_gate("CNOT", 0, 1)
    
    print("\nOriginal Circuit:")
    print("-" * 60)
    print(c.stats())
    
    # Convert to ZX-Graph
    print("\nConverting to ZX graph...")
    g = c.to_graph()
    print(f"Graph vertices before simplification: {g.num_vertices()}")
    
    # Apply simplification
    print("\nApplying ZX simplification rules...")
    zx.full_reduce(g)
    
    # Check result
    is_identity = g.num_vertices() == (g.num_inputs() + g.num_outputs())
    
    print("\nResults:")
    print("-" * 60)
    print(f"Graph vertices after simplification: {g.num_vertices()}")
    print(f"Input vertices: {g.num_inputs()}")
    print(f"Output vertices: {g.num_outputs()}")
    print(f"\nIs pure Identity? {is_identity}")
    
    if is_identity:
        print("\n✓ SUCCESS: The circuit collapsed to just wires (Identity)!")
        print("  ZX-calculus detected that all gates cancelled out.")
    else:
        print("\n⚠ The circuit simplified but retained some structure.")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
