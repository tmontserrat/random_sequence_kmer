# random_sequence_kmer
A class to represent a random DNA sequence and work with kmers.

Example:

Let's generate a random DNA sequence of 50000 nucleotides long for later study the distribution of the different observed kmers:

```
from random_sequence_kmers import Sequence
dna = Sequence(5000)
```
We can access to some attributes like the whole sequence and its length:

```
print(dna.sequence)
## TCATTCGCCGCAATTGTGACGCATCTAACATATATTGAACGT (...)
```

```
print(dna.length)
## 5000
```

It is possible to split the DNA sequence that has been generated into its kmers, specifying the length of each kmer. For doing that, we have to use the `split_dna()` method with the length of the kmer as unique argument. The method returns a list:    

```
print(dna.split_dna(3))
## ['TCC', 'CCA', 'CAG', 'AGG', 'GGC', 'GCC', 'CCA', (...)]
```

