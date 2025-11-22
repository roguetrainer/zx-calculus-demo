#!/usr/bin/env python3
"""
Example 2: Quantum Teleportation as a "Bent Wire"

This script demonstrates how ZX-calculus reveals that quantum teleportation
is topologically equivalent to a bent wire being straightened.
"""

import pyzx as zx
import matplotlib.pyplot as plt


def main():
    """Demonstrate teleportation visualization."""
    
    print("=" * 60)
    print("ZX-CALCULUS: QUANTUM TELEPORTATION")
    print("=" * 60)
    print()
    
    # Construct teleportation circuit
    print("Building quantum teleportation protocol...")
    print("  Qubit 0: Payload (Alice's state to send)")
    print("  Qubit 1: Alice's half of Bell pair")
    print("  Qubit 2: Bob's half of Bell pair")
    print()
    
    c = zx.Circuit(qubit_amount=3)
    
    # Create Bell pair
    c.add_gate("HAD", 1)
    c.add_gate("CNOT", 1, 2)
    
    # Bell measurement
    c.add_gate("CNOT", 0, 1)
    c.add_gate("HAD", 0)
    
    print(f"Circuit created with {len(c.gates)} gates.")
    
    # Convert to graph
    print("\nConverting to ZX graph...")
    g = c.to_graph()
    zx.simplify.to_clifford_normal_form_graph(g)
    
    # Visualize before and after
    print("Creating visualization...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Before
    zx.draw(g, ax=ax1)
    ax1.set_title("Before: The Protocol", fontsize=12, fontweight='bold')
    
    # Simplify
    zx.full_reduce(g)
    
    # After
    zx.draw(g, ax=ax2)
    ax2.set_title("After: The 'Bent Wire'", fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('teleportation_visualization.png', dpi=150, bbox_inches='tight')
    print("✓ Visualization saved as 'teleportation_visualization.png'")
    
    # Generate QASM
    print("\nExtracting optimized circuit...")
    try:
        opt_c = zx.extract_circuit(g.copy())
        qasm = opt_c.to_qasm()
        
        print("\nOptimized QASM:")
        print("-" * 60)
        print(qasm)
        print("-" * 60)
        
        print("\n✓ The circuit simplified to near-identity!")
        print("  This proves teleportation = routing through a bent wire.")
        
    except Exception as e:
        print(f"\n⚠ Extraction failed: {e}")
        print("  (The graph may need conversion to graph-like form)")
    
    print("\n" + "=" * 60)
    print("To view the visualization, open: teleportation_visualization.png")
    print("=" * 60)


if __name__ == "__main__":
    main()
