#!/usr/bin/env python3
"""
Example 3: T-Count Reduction with ZX-Calculus

This script demonstrates how ZX-calculus can cancel expensive T-gates
that are separated by other quantum operations.
"""

import pyzx as zx


def main():
    """Demonstrate T-count reduction."""
    
    print("=" * 60)
    print("ZX-CALCULUS: T-COUNT REDUCTION")
    print("=" * 60)
    print()
    print("In Fault-Tolerant Quantum Computing:")
    print("  • Clifford gates (H, CNOT, S) are 'cheap'")
    print("  • T-gates require expensive magic state distillation")
    print("  • Reducing T-count = massive resource savings")
    print()
    
    # Create circuit with separated T-gates
    print("Creating circuit with T-gates separated by CNOT...")
    c = zx.Circuit(qubit_amount=2)
    
    c.add_gate("T", 0)                # T-gate (expensive)
    c.add_gate("CNOT", 0, 1)          # Blocking structure
    c.add_gate("T", 0, adjoint=True)  # T-dagger (expensive)
    
    print("\nOriginal Circuit:")
    print("-" * 60)
    print(f"T-count: {c.tcount()}")
    print(f"Total gates: {len(c.gates)}")
    print(c.stats())
    
    # Convert and optimize
    print("\nConverting to ZX graph and optimizing...")
    g = c.to_graph()
    zx.full_reduce(g)
    
    # Extract result
    print("Extracting optimized circuit...")
    opt_c = zx.extract_circuit(g.copy())
    
    print("\nOptimized Circuit:")
    print("-" * 60)
    print(f"T-count: {opt_c.tcount()}")
    print(f"Total gates: {len(opt_c.gates)}")
    print(opt_c.stats())
    
    # Analysis
    t_removed = c.tcount() - opt_c.tcount()
    
    print("\nResults:")
    print("=" * 60)
    print(f"T-gates removed: {t_removed}")
    
    if t_removed > 0:
        reduction = 100 * t_removed / c.tcount()
        print(f"T-count reduction: {reduction:.1f}%")
        print()
        print("✓ SUCCESS: ZX-calculus cancelled the expensive gates!")
        print()
        print("How it worked:")
        print("  1. T and T† are phase spiders (π/4 and -π/4)")
        print("  2. CNOT control is also a Z-spider (green)")
        print("  3. Spiders of same color fuse: π/4 + (-π/4) = 0")
        print("  4. Zero phase = Identity = free!")
        print()
        print(f"In FTQC, this saves:")
        print(f"  • ~{t_removed * 15} physical qubits")
        print(f"  • ~{t_removed * 1000} physical operations")
    else:
        print("\n⚠ No T-gates were removed.")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
