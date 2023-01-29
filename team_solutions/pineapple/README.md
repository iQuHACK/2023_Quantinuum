## Challenges on QAOA 

1. This QAOA [(Quantum Approximate Optimisation algorithm)](https://arxiv.org/abs/1411.4028) implementaion uses the most naive possible classical optimisation strategy. Parameters are sampled from a uniform distribution and if a list of parameters increases the value of the cost function these values are stored as the best guess so far. Can you improve on this using a more sophisticated optimisation strategy? COBAYLA and SPSA are two possible methods.

2. The maxcut problem is one very common application of QAOA. Can you create an implementation of QAOA applied to a different problem? Examples of such problems included 3SAT and the maximum clique problem. Perhaps try and create and implementation which works for a more general Hamiltonian that could contain non-commuting Pauli terms like those found in Quantum Chemistry. Think about what additonal complexity would be added by a Hamiltonian with non-commuting terms. Interesting Hamiltonians to consider could be the Transverse Field Ising Model (TFIM), diatomic Hydrogen or a simple compound like lithium hydride. 

3. The given code implements QAOA on the idealised AerBackend simulator. Try instead to use a device/emulator with noise (i.e. the H1-2 emulator with the pytket-quantinuum extension). Can you optimise your circuit with pytket passes to improve performance in the presence of noise?

4. Currently the circuits have to be recompiled on every iteration leading to a non-trivial compilation overhead if we use a large number of iterations. Can you think of a way to improve this? 

5. Implement a qubit reuse strategy to allow for the execution of a large QAOA instance on a small quantum device/emulator. See [this paper](https://arxiv.org/abs/2210.08039) for ideas.

## Resources

1. QAOA original paper (Farhi et al) -> https://arxiv.org/abs/1411.4028
2. Quantinuum Qubit reuse paper (DeCross et al) -> https://arxiv.org/abs/2210.08039
3. pytket API documentation -> https://cqcl.github.io/tket/pytket/api/
4. User manual -> https://cqcl.github.io/pytket/manual/index.html
5. Notebook examples -> https://github.com/CQCL/pytket/tree/main/examples
6. Qiskit textbook section on QAOA -> https://qiskit.org/textbook/ch-applications/qaoa.html
7. Recent QAOA/qiskit review -> https://arxiv.org/abs/2301.09535
