#!/usr/bin/env python3
"""
Example 4: Random Clifford+T Circuit Optimization

This script generates a large random quantum circuit and demonstrates
how ZX-calculus optimizes it, focusing on T-count reduction.
"""

import pyzx as zx
import sys


def main():
    """Demonstrate optimization on random Clifford+T circuits."""
    
    print("=" * 70)
    print("ZX-CALCULUS: RANDOM CLIFFORD+T CIRCUIT OPTIMIZATION")
    print("=" * 70)
    print()
    
    # Configuration
    n_qubits = 5
    depth = 100
    p_t = 0.2
    
    print("Generating random circuit...")
    print(f"  Qubits: {n_qubits}")
    print(f"  Depth: {depth}")
    print(f"  T-gate probability: {p_t * 100:.0f}%")
    print()
    
    # Generate circuit
    c = zx.generate.cliffordT(qubits=n_qubits, depth=depth, p_t=p_t)
    
    orig_gates = len(c.gates)
    orig_t = c.tcount()
    
    print("Original Circuit Statistics:")
    print("-" * 70)
    print(f"Total gates: {orig_gates}")
    print(f"T-count: {orig_t}")
    print()
    print("Gate breakdown:")
    print(c.stats())
    
    # Optimize
    print("\n" + "=" * 70)
    print("OPTIMIZING WITH ZX-CALCULUS")
    print("=" * 70)
    print()
    print("Converting to ZX graph...")
    g = c.to_graph()
    
    print("Applying full_reduce...")
    print("(This may take a few seconds for large circuits)")
    print()
    
    zx.full_reduce(g)
    
    print("✓ Optimization complete!")
    print("\nExtracting optimized circuit...")
    
    opt_c = zx.extract_circuit(g.copy())
    
    opt_gates = len(opt_c.gates)
    opt_t = opt_c.tcount()
    
    print("✓ Extraction complete!")
    
    # Results
    print("\n" + "=" * 70)
    print("OPTIMIZATION RESULTS")
    print("=" * 70)
    print()
    
    print("Gate Count:")
    print(f"  Original:  {orig_gates}")
    print(f"  Optimized: {opt_gates}")
    print(f"  Change:    {opt_gates - orig_gates:+d} gates")
    
    if orig_gates > 0:
        gate_pct = 100 * (opt_gates - orig_gates) / orig_gates
        print(f"  ({gate_pct:+.1f}%)")
    
    print()
    print("T-Count (Critical for FTQC):")
    print(f"  Original:  {orig_t}")
    print(f"  Optimized: {opt_t}")
    print(f"  Removed:   {orig_t - opt_t} T-gates")
    
    if orig_t > 0:
        t_pct = 100 * (orig_t - opt_t) / orig_t
        print(f"  ({t_pct:.1f}% reduction)")
        
        if orig_t > opt_t:
            print()
            print("🎉 SUCCESS: Reduced T-count!")
            print()
            saved = orig_t - opt_t
            print(f"In Fault-Tolerant QC, this saves:")
            print(f"  • ~{saved * 15:,} physical qubits")
            print(f"  • ~{saved * 1000:,} physical operations")
            print()
            
            if opt_gates > orig_gates:
                print("Note: Total gate count increased.")
                print("This is OK! CNOTs are ~1000× cheaper than T-gates.")
                print(f"Trading {orig_gates - opt_gates} extra CNOTs for")
                print(f"{saved} fewer T-gates is a massive win.")
    else:
        print()
        print("⚠ Original circuit had no T-gates.")
    
    # Verification
    print()
    print("=" * 70)
    print("VERIFYING CORRECTNESS")
    print("=" * 70)
    print()
    print("Comparing quantum operations...")
    
    try:
        valid = zx.compare_tensors(c, opt_c, preserve_scalar=False)
        
        if valid:
            print("✓ VERIFIED: Circuits are mathematically identical!")
            print("  Optimization preserved correctness.")
        else:
            print("✗ FAILED: Circuits differ!")
            print("  This may indicate a bug.")
            
    except Exception as e:
        print(f"⚠ Verification error: {e}")
        print("  (Often due to circuit size - verification is expensive)")
    
    print()
    print("=" * 70)
    print("Optimized circuit breakdown:")
    print(opt_c.stats())
    print("=" * 70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
