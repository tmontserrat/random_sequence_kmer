import random
import itertools
import numpy as np

class Sequence:
    """
    A class to represent a random DNA sequence and work with kmers.
    """
    def __init__(self, length):
        """
        Create a random DNA sequence with the specified length.
        """

        # Create the sequence
        # Empty string to store the DNA sequence
        sequence = ""
        # Create the random sequence
        for nucleotide in range(0, length):
            sequence += random.choice("AGTC")

        self.sequence = sequence
        self.length = len(self.sequence)
    
    def split_dna(self, kmers_length):
        """
        Split a DNA sequence into a list of kmers 
        of a determined length.
        """
        # Emtpy list to store the sequence splitted
        kmers = []
        for start in range(0, len(self.sequence)-kmers_length+1):
            kmers.append(self.sequence[start:start+kmers_length])
        return kmers
    
    def kmers_counting(self, kmers_length):
        """
        Generate a random DNA sequence with a desired length
        and count how many observed kmers there are with a determined
        length. It returns a dictionary kmer: count.
        """
        
        # Create an empty dictionary to store the paired data kmer: count
        kmers_count_dict = {}
        
        # Iterate over the kmers of the DNA sequence once splitted
        # and count each of them
        for kmer in self.split_dna(kmers_length):
            kmers_count_dict[kmer] = kmers_count_dict.get(kmer, 0) + 1

        return kmers_count_dict

    def kmer_distribution(self, kmers_length):
        """
        Find the probability distribution of the 
        observed kmers from a simulated DNA sequence.
        """
        # Create a dictionary with the frequencies of all observed kmers
        kmers_count_dictionary = self.kmers_counting(kmers_length)
        # Empty list to store frequencies
        frequencies = []
        for value in kmers_count_dictionary.values():
            frequencies.append(value)
        
        # Create all possible kmers
        all_possible_kmers = itertools.product("ACGT", repeat=kmers_length)
        # Count how many possible kmers are not observed
        count = 0
        for kmer in all_possible_kmers:
            if ''.join(kmer) not in kmers_count_dictionary:
                count += 1
        frequence_zero = count

        # Return a tupple: frequencies of observed kmers and
        # number of kmers not observed
        return (frequencies, frequence_zero)

    def frequencies_histogram(self, kmers_length, bins):
        distribution = self.kmer_distribution(kmers_length)[0]    
        hist, edges = np.histogram(
            distribution,
            bins=bins,
            range=(min(distribution), max(distribution)),
            density=False)
        
        return (hist, edges)

    def calculate_tail_probability(self, kmer_length, threshold):
        """
        Calculate the two tails probability for the 
        observed kmers in a random genome for a given
        count threshold.
        """
        # Observed kmers count frequencies
        distribution = self.kmer_distribution(kmer_length)[0]

        # Calculate the probability
        count = 0
        for frequency in distribution:
            if frequency < threshold:
                count += 1
        lower_tail = count/len(distribution)
        upper_tail = 1-lower_tail

        # Return a tupple with the lower and upper tail probabilities
        return (lower_tail, upper_tail)

dna = Sequence(5000)

print(sum(dna.kmer_distribution(3)[0]))
print(dna.kmer_distribution(3))
print(dna.calculate_tail_probability(3, 90))
print(dna.frequencies_histogram(3, 8)[0])
print(dna.frequencies_histogram(3, 8)[1])