# iQuHACK 2023 - Quantinuum Challenge

![logo image](wordmark-01.png)



[<img src="https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qBraid_white.png" width="150">](https://account.qbraid.com?gitHubUrl=https://github.com/iQuHACK/2023_Quantinuum.git)
1. If you're working on qBraid, first fork this repository and click the above `Launch on qBraid` button. It will take you to your qBraid Lab with the repository cloned.
2. Once cloned, open terminal (first icon in the **Other** column in Launcher) and `cd` into this repo. Set the repo's remote origin using the git clone url you copied in Step 1, and then create a new branch for your team:
```bash
cd  2023_Quantinuum
git remote set-url origin <url>
git branch <team_name>
git checkout <team_name>
```

# The Quantum Approximate Optimisation Algorithm (QAOA)
QAOA is a widely discussed quantum algorithm for optimisation problems. In one part of the Quantinuum challenge you will be given an implenmentation of QAOA applied to the maxcut problem and asked to improve upon the code exploring different features of TKET and the QuantinuumBackend. There is also a bonus question on qubit reuse compilation.

For the QAOA challenges click [here](https://github.com/iQuHACK/2023_planning_quantinuum/tree/main/qaoa_challenge).


# Exploiting Mid-circuit Measurement and Qubit Reuse using the Quantinuum H1-2 Emulator

The ability to perform measurements between, or simultaneous with, the application of quantum gates is known as mid-circuit measurement. Specifically in this process, you measure a qubit, reset it, and use it again in the middle of a circuit. Mid-circuit measurements important in several quantum information computing protocols. Mid-circuit measurements and resets can be used to:

 - Enable Quantum Error Correction
 - Measurement based quantum computing (MBQC)
 - Enables qubit reuse compilation - reduces the number of qubits required to execute some quantum algorithms.

Several commercially available quantum computers, such as Quantinuuum’s trapped-ion quantum computer, can perform mid-circuit measurements and qubit resets. 


#### In this part of the challenge, you can use mid circuit measurements and resets to reduce the number of qubits required to implement a quantum algorithm. Qubit reuse allows you to execute circuits wider than the number of available qubits on the device at the expense of adding more depth.

To get started you can follow [this paper recently published by Quantinuum](https://arxiv.org/pdf/2210.08039.pdf) where a 80-qubit QAOA MaxCut circuit was successfully run on the 20-qubit Quantinuum H1-1 trapped ion quantum processor using qubit-reuse compilation algorithms. Another quantum algorithm you can experiment with is the [Bernstein-Vazirani (BV) algorithm](https://en.wikipedia.org/wiki/Bernstein%E2%80%93Vazirani_algorithm). In case you want to get started with mid-circuit measurement and qubit reuse without needing to develop an algorithm, you can use sample circuits in this folder [here](https://github.com/iQuHACK/2023_planning_quantinuum/tree/main/sample%20circuits).


## H1-2 Emulator access

You’ll be able to test your project on the [H1-2 emulator (12-qubits)](https://assets.website-files.com/62b9d45fb3f64842a96c9686/6398c899bb181e5138578789_Quantinuum%20H1%20Emulator%20Product%20Data%20Sheet%20v6%2001DEC22.pdf). Our System Model H1-2 Emulator is a cloud-based classical CPU simulator using identical I/O pathways, compilers, and high-fidelity error modeling. The emulator has the most accurate noise model of the 12-qubit Quantinuum H1-2 trapped ion quantum processor and features all-to-all connectivity and qubit reuse after mid-circuit measurement. Another important note is that just as for a real backend your submitted job will be in a queue since the emulator is cloud-based. Hence you need to plan for emulator queue times when submitting your final jobs for this challenge.

Quantinuum challenge participants need to provide kathrin.spendier@quantinuum.com with an email address and their team’s name to set up their emulator account. (The iQuHACK team will help with this step.) Once your email is added to the system, you will receive an invitation email from QCadmin@quantinuum.com, which you have to open and follow the steps outlined. You will be asked to accept the Quantinuum “Policy & Terms of USE” https://um.qapi.quantinuum.com/static/media/user_terms_and_conditions.46957d35.pdf. 
You need to accept the terms and conditions to unlock access to the Quantinuum emulator. Please make sure that you have access to the emulator by Saturday morning. If you have issues signing up, please find a Quantinuum staff member for help or email kathrin.spendier@quantinuum.com.
#### Note: please check you spam/junk email folder for the invitation email from QCadmin@quantinuum.com



## TKET: Quantinuum’s Quantum SDK
To access the [Quantinuum](https://www.quantinuum.com/) H1-2 emulator, you will be using [TKET](https://www.quantinuum.com/developers/tket), more specifically pyTKET, the python wrapper of TKET. To access the emulator, you will use the [pytket-quantinuum extension](https://cqcl.github.io/pytket-quantinuum/api/) in your python environment (i.e., jupyter notebook, qBraid). Since TKET is language agnostic, you can develop your project using other languages like Qiskit, Criq, or Q# and then convert your circuit written in your favorite language to a pyTKET circuit to submit your job to the H1-2 emulator.

### Useful Links to get you started are:
 - [pyTKET User manual](https://cqcl.github.io/pytket/manual/index.html)
 - [pyTKET API docs](https://cqcl.github.io/tket/pytket/api/)
 - [pyTKET Notebook Examples](https://github.com/CQCL/pytket/tree/main/examples)
 - [pytket-quantinuum extension](https://cqcl.github.io/pytket-quantinuum/api/)

 
## Challenge-specific TKET tutorials
This repository has a few sample notebooks you can use to get started. 

- [Here](https://github.com/iQuHACK/2023_planning_quantinuum/tree/main/TKET%20and%20Emulator%20tutorial) you will find a sample notebook that goes over the basics of circuit preparation and submission with pyTKET, outlines how to convert between pyTKET and other quantum SDKs like qiskit, as well as how to perform the mid-circuit measurement and qubit reuse on the H1-2 emulator.

- [Here](https://github.com/iQuHACK/2023_planning_quantinuum/tree/main/sample%20circuits) you will find a folder with sample circuits you can use to get started with mid-circuit measurement and qubit reuse without needing to develop an algorithm.

- [Here](https://github.com/iQuHACK/2023_planning_quantinuum/tree/main/qaoa_challenge) you will find a notebook that covers QAOA in detail and some exercises to help you explore the details of QAOA.


## TKET help
In case you need help please reach out to Kathrin Spendier (in-person mentor) or Callum Macpherson (in-person mentor). For online help, we have created a [public slack channel](https://tketusers.slack.com/join/shared_invite/zt-18qmsamj9-UqQFVdkRzxnXCcKtcarLRA#/shared-invite/email) (#iquhack_2023) for support and discussion.

## Judging
We'll be evaluating the projects based on several criteria, as detailed in this rubric:
[Evaluation Guidelines Quantinuum iQuHACK 2023.xlsx](https://quantinuum-my.sharepoint.com/:x:/p/kathrin_spendier/EbJDhezbdtVPm_x10GPQb4cBhoNUwrl2DeqlIoIbIlz8lA?e=1JzVCF)


## Documentation

This year’s iQuHACK challenges require a write-up/documentation portion that is heavily considered during
judging. The write-up is a chance for you to be creative in describing your approach and describing
your process. It can be in the form of a blog post, a short YouTube video or any form of
social media. It should clearly explain the problem, the approach you used, your implementation with results
from simulation and hardware, and how you accessed the quantum hardware (total number of shots used, 
backends used, etc.).

Make sure to clearly link the documentation into the `README.md` and to include a link to the original challenge 
repository from the documentation!


## Submission

To submit the challenge, do the following:
1. Place all the code you wrote in one folder with your team name under the `team_solutions/` folder (for example `team_solutions/quantum_team`).
2. Create a new entry in `team_solutions.md` following the format shown that links to the folder with your solution and your documentation.
3. Create a Pull Request from your repository to the original challenge repository
4. Submit the "challenge submission" form

Project submission forms will automatically close on Sunday at 10am EST and won't accept late submissions.

## Eligibility
Quantinuum employees are not eligible to participate in this challenge.
For the general rules on eligibility and hackathon participation, please refer to the official rules
