# stream-sampler
Task by ResearchGate

This solution is based on the algorithm method "Reservoir Sampling".  This algorithm is used when there is an endless stream of data and our goal is to sample a small item with uniform probability.

Given a sample size of K with N items processed in a stream, the chance for any items selected is K/N. When the N+1 item enter, current samples have a choice to survive K/N*N/(N+1)=K/(N+1) while the new item has a chance of K/(N+1) to be selected.

Assumptions Made:
1. It is assumed that the sample size K is always less than N, else the program would return the input string
2. The programming environment used is python3.5

Sample Run:

<img width="1436" alt="screen shot 2018-07-21 at 12 13 17 am" src="https://user-images.githubusercontent.com/3582757/43019696-7ff4211e-8c7b-11e8-9440-50560ab75b1b.png">

