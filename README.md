# random_sequence_kmer
A class to represent a random DNA sequence and work with kmers.

Example:

Let's generate a random DNA sequence of 50000 nucleotides long for later study the distribution of the different observed kmers:

```
>>> from random_sequence_kmers import Sequence
>>> dna = Sequence(5000)
```
We can access to some attributes like the whole sequence and its length:

```
>>> dna.sequence
TCATTCGCCGCAATTGTGACGCATCTAACATATATTGAACGT (...)
```

```
>>> dna.length
5000
```

It is possible to split the DNA sequence that has been generated into its kmers, specifying the length of each kmer. For doing that, we have to use the `split_dna()` method with the length of the kmer as unique argument. The method returns a list:    

```
>>> dna.split_dna(3))
>>> ['TCC', 'CCA', 'CAG', 'AGG', 'GGC', 'GCC', 'CCA', (...)]
```

The method `kmers_counting()` returns a dictionary with each kmer found and its absolute frequency. The unique argument is, again, the desired kmer length:    

```
>>> dna.kmers_counting(3)
{'TGT': 86, 'GTC': 81, 'TCG': 76, 'CGT': 77, 'GTA': 75, 'TAG': 77, 'AGC': 64, 'GCC': 75, 'CCG': 89, 'CGA': 83, 'GAT': 85, 'ATT': 82, 'TTG': 83, 'GTT': 77, 'TGG': 84, 'GGC': 71, 'GCA': 82, 'CAC': 79, 'ACC': 78, 'CCA': 82, 'CAA': 79, 'AAT': 83, 'ATC': 78, 'TCA': 70, 'AAG': 67, 'AGG': 68, 'GGG': 69, 'GCT': 64, 'CTG': 77, 'GGA': 84, 'TTA': 79, 'TAT': 75, 'ATG': 86, 'TGC': 81, 'CGC': 81, 'AAC': 81, 'GAC': 97, 'ACG': 81, 'GTG': 87, 'TGA': 83, 'GAG': 60, 'AGT': 79, 'TTC': 74, 'CAG': 73, 'AGA': 66, 'TCT': 81, 'CTA': 77, 'TAC': 71, 'ACA': 71, 'AAA': 101, 'GGT': 78, 'TTT': 72, 'CGG': 81, 'ATA': 70, 'GAA': 74, 'TCC': 86, 'ACT': 98, 'CCT': 68, 'TAA': 78, 'CTC': 80, 'CAT': 74, 'GCG': 76, 'CTT': 77, 'CCC': 77}
```

With the method `kmer_distribution()` we can get a list with the absolute distributions (the values of the latter dictionary). Actually, we get a tupple where the first element is the mentioned list and the second element is the number of possible kmer of the same length not founded and, therefore, with a frequency of zero:  

```
>>> dna.kmer_distribution(3)
([86, 81, 76, 77, 75, 77, 64, 75, 89, 83, 85, 82, 83, 77, 84, 71, 82, 79, 78, 82, 79, 83, 78, 70, 67, 68, 69, 64, 77, 84, 79, 75, 86, 81, 81, 81, 97, 81, 87, 83, 60, 79, 74, 73, 66, 81, 77, 71, 71, 101, 78, 72, 81, 70, 74, 86, 98, 68, 78, 80, 74, 76, 77, 77], 0)
```

In the last output we can see that all possible kmers (all possible 3 nucelotides combinations) have been found. That's the reason of the 0. For example:  

```
>>> dna2 = Sequence(30)
>>> dna.kmer_distribution(5)
([5, 4, 3, 4, 2, 9, 7, 3, 7, 6, 8, 5, 8, 9, 7, 4, 6, 6, 5, 8, 8, 8, 9, 4, 5, 5, 3, 8, 4, 3, 5, 4, 3, 3, 6, 7, 4, 1, 3, 8, 5, 5, 7, 5, 3, 3, 5, 9, 5, 5, 3, 6, 5, 5, 7, 2, 5, 3, 5, 8, 7, 4, 5, 7, 4, 5, 10, 9, 4, 4, 7, 6, 9, 10, 8, 6, 6, 13, 7, 7, 7, 8, 5, 3, 6, 3, 1, 3, 4, 3, 3, 3, 6, 8, 7, 4, 6, 5, 1, 7, 5, 4, 5, 8, 3, 4, 4, 6, 4, 7, 5, 3, 5, 7, 4, 5, 1, 2, (...)], 9)
```

There are 9 possible kmers not found.  


