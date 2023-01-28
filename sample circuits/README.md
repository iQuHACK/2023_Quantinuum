In this folder you will find some sample circuits you can use to explore mid-ciruit measurement and qubit reuse without developing your own algorithm. The circuits are avalbale as .qasm files. QASM is a simple text-format language for describing quantum circuits.

- circuit1.qasm: 12-qubit Bernstein Vazirani (BV) algorithm circuit that can be rewritten using 2 qubits. 
- circuit2.qasm: Quantum error correction sample circuit that can be reduced from two auxiliary qubits to one auxiliary qubit.
- circuit3.qasm: [8-bit quantum ripple-carry adder example](https://arxiv.org/pdf/quant-ph/0410184.pdf) where the circuit that has initial 18 qubits (8xA, 8xB, 2xcarry) can be reduced to 10 qubits (4xA, 4xB, 2xcarry). This is a more difficult circuit to apply mid-circuit measurement and qubit reuse.
- circuit4.qasm: QAOA sample circuit that can be reduced from 7 qubits to 5 qubits. 
