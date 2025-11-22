# ZX Calculus and Tensor Networks
This file: `ZX_CALCULUS_VS_TENSOR_NETWORKS.md`

See repos:
* [tensor_networks_finance](https://github.com/roguetrainer/tensor_networks_finance/)
* [zx-calculus-demo](https://github.com/roguetrainer/zx-calculus-demo)

## Relationship Between the ZX Calculus and Tensor Networks

ZX Calculus & Tensor Networks are **intimately related**. In fact, **ZX Calculus is a specialized dialect of Tensor Networks.**

Both belong to the field of **Graphical Linear Algebra** (using pictures to do matrix math), but they serve slightly different purposes in the computational pipeline.

Here is the breakdown of how they connect, how they differ, and why they are often used together in high-performance computing (including finance).

---

### 1. The Fundamental Link: Everything is a Tensor
At their core, both systems represent the exact same mathematical objects:
* **Tensor Networks (TN):** A generic graphical language where **Nodes** are tensors (multi-dimensional arrays of numbers) and **Edges** are indices to be summed over (contracted).
* **ZX Calculus:** A specific type of Tensor Network where the **Nodes** are strictly limited to two specific types of tensors (called "Z Spiders" and "X Spiders").

**The Hierarchy:**
> *Every ZX Diagram is a Tensor Network, but not every Tensor Network is easily written as a ZX Diagram.*

### 2. The Rosetta Stone: Comparing the Vocabularies

| Feature | Tensor Networks (TN) | ZX Calculus |
| :--- | :--- | :--- |
| **The Atom** | **Generic Tensor ($T$).** A black box full of numbers. | **Spiders (Z and X).** Specific sparse tensors defined by phase angles. |
| **The Wire** | **Index.** Represents a dimension in a vector space (size $N$). | **Qubit.** Represents a specific 2-dimensional space (Hilbert space). |
| **The Goal** | **Contraction.** "Crunch the numbers" to get a final value (Price, Probability). | **Rewriting.** "Simplify the diagram" to make the calculation cheaper *before* you crunch. |
| **Universality** | Universal for **Linear Algebra**. (Can represent any matrix). | Universal for **Quantum Computing**. (Can represent any Unitary gate). |

### 3. Key Difference: Contraction vs. Simplification

This is the most important distinction for implementation.

#### Tensor Networks are for **Calculation** (Arithmetic)
In applications to finance, say, Tensor Networks are used to **calculate a number**.
* We have a grid of numbers.
* We perform `tt.dot(A, B)` (Contraction).
* We get a float result.

#### ZX Calculus is for **Simplification** (Algebra)
ZX Calculus is a set of **Rewrite Rules** (axioms) that allow you to change the shape of the tensor network *without* changing the result.
* **The Spider Fusion Rule:** If two "Z" tensors are connected, they merge into one Z tensor.
    $$Z(\alpha) - Z(\beta) \rightarrow Z(\alpha + \beta)$$
* **The Benefit:** If you have a massive financial model represented as a quantum circuit, you can use ZX Calculus to "cancel out" redundant gates and reduce the size of the graph.

### 4. How They Work Together (The Pipeline)
In advanced "Quantum-Inspired" Finance, the workflow often looks like this:

1.  **Model Definition:** You define your derivative pricing algorithm as a **Quantum Circuit** (a specific structure of gates).
2.  **ZX Optimization:** You convert that circuit into a **ZX Diagram**. You apply ZX rewrite rules to delete redundant nodes and simplify the topology. (This reduces the "Bond Dimension" we discussed earlier).
3.  **TN Conversion:** You convert the simplified ZX diagram back into a standard **Tensor Network** (like a Tensor Train or PEPS).
4.  **Contraction:** You run the Tensor Network algorithm (on a GPU) to get the final price.

**Why do this?**
Directly contracting a raw quantum circuit as a Tensor Network is often inefficient because standard circuits (like `CNOT` gates) can artificially inflate the bond dimension. ZX Calculus exposes the "hidden flows" of information, allowing you to smash the graph into a smaller, more efficient shape before you spend compute power calculating it.

### 5. Summary Visual

* **Tensor Network:** Like a generic map of cities (tensors) and roads (indices). You just want to drive the route (sum the values).
* **ZX Calculus:** A traffic engineer who looks at the map and says, "These two intersections are actually the same intersection, and this road is a loop that does nothing." They redraw the map to be simpler so the drive takes less time.

