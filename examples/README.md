# ZX-Calculus Standalone Examples

This directory contains standalone Python scripts demonstrating various aspects of ZX-calculus optimization.

## Prerequisites

Ensure you have installed the package dependencies:

```bash
pip install -r ../requirements.txt
```

Or use the virtual environment created by `setup.sh`.

## Examples

### 01_hidden_identity.py

**Purpose**: Detect when complex circuits are actually identity operations.

**What it demonstrates**:
- Converting circuits to ZX graphs
- Applying simplification rules
- Detecting complete gate cancellation

**Usage**:
```bash
python 01_hidden_identity.py
```

**Expected output**: The script shows how a 7-gate circuit collapses to pure wires.

---

### 02_teleportation.py

**Purpose**: Visualize quantum teleportation as a "bent wire".

**What it demonstrates**:
- Topological insight into quantum protocols
- Before/after visualization
- QASM generation from optimized graphs

**Usage**:
```bash
python 02_teleportation.py
```

**Expected output**: 
- Console output showing circuit simplification
- `teleportation_visualization.png` showing the bent wire

**Requirements**: matplotlib (included in requirements.txt)

---

### 03_t_count_reduction.py

**Purpose**: Demonstrate T-gate optimization for fault-tolerant quantum computing.

**What it demonstrates**:
- Why T-gates are expensive
- Phase gadget cancellation
- Resource savings calculation

**Usage**:
```bash
python 03_t_count_reduction.py
```

**Expected output**: Shows how T and T† gates cancel through a CNOT.

---

### 04_random_clifford_t.py

**Purpose**: Stress-test ZX optimization on large random circuits.

**What it demonstrates**:
- Real-world compilation scenarios
- T-count reduction at scale
- Correctness verification

**Usage**:
```bash
python 04_random_clifford_t.py
```

**Expected output**: 
- Statistics for random circuit optimization
- Typical T-count reduction of 30-50%
- Verification that optimization preserves correctness

**Note**: This script may take 10-30 seconds to complete due to tensor verification.

---

## Running All Examples

To run all examples in sequence:

```bash
cd examples
for script in *.py; do
    echo "Running $script..."
    python "$script"
    echo ""
done
```

Or on Windows:
```cmd
cd examples
for %f in (*.py) do (
    echo Running %f...
    python %f
    echo.
)
```

## Modifying Examples

All examples are self-contained and heavily commented. Feel free to:

- Change circuit parameters (qubit counts, depths)
- Try different gate sequences
- Add visualization code
- Experiment with different ZX optimization strategies

## Common Issues

### Import Error: No module named 'pyzx'

**Solution**: Install dependencies
```bash
pip install -r ../requirements.txt
```

### Matplotlib Backend Error

**Solution**: Set backend explicitly
```python
import matplotlib
matplotlib.use('Agg')  # For non-interactive backend
import matplotlib.pyplot as plt
```

### Memory Error on Large Circuits

**Solution**: Reduce circuit size
```python
# In 04_random_clifford_t.py, reduce parameters:
n_qubits = 3  # Instead of 5
depth = 50    # Instead of 100
```

## Integration with Notebook

These examples complement the Jupyter notebook (`../zx_calculus_demo.ipynb`):

- **Notebook**: Interactive exploration with visualizations
- **Scripts**: Batch processing, automation, benchmarking

You can copy code from these scripts into the notebook or vice versa.

## Further Experiments

Try modifying the examples to:

1. **Implement Grover's Algorithm** and see how it simplifies
2. **Compare optimization strategies** (full_reduce vs. individual passes)
3. **Benchmark performance** on circuits of varying sizes
4. **Integrate with Qiskit** for hardware execution

## Documentation

For theoretical background, see:
- `../INTRODUCTION-TO-ZX-CALCULUS.md` - Comprehensive theory guide
- `../README.md` - Package overview
- [PyZX Documentation](https://pyzx.readthedocs.io/) - Full API reference

---

Happy optimizing! 🎉
