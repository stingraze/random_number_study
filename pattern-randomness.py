#(C)Tsubasa Kato - Inspire Search Corporation - 2025/1/4 11:00AM JST
#Referred to this paper: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/tops.12345 and used Perplexity and ChatGPT o1 to create this script. 
#Tested to work on Mac environment with Python 3.11.5
import random
import math

class ImprovedRandomGenerator:
    def __init__(self, seed=None):
        """
        Initialize the ImprovedRandomGenerator.
        
        :param seed: Optional seed for the random number generator.
                     If None, the default system-based seeding is used.
        """
        self.random = random.Random(seed)  # Create an instance of Python's random.Random with the given seed
        self.history = []                  # Store a history of generated numbers
        self.max_history = 100            # Maximum size of the history list; older entries are discarded

    def random_number(self, start, end):
        """
        Generate a number in the range [start, end] that passes the 'is_random_enough' checks.
        
        :param start: Lower bound for the random number (inclusive).
        :param end: Upper bound for the random number (inclusive).
        :return: A number that meets the "random enough" criteria.
        """
        while True:
            # Generate a candidate random integer in [start, end]
            candidate = self.random.randint(start, end)
            
            # If the candidate passes all the randomness checks, return it.
            if self.is_random_enough(candidate, start, end):
                # Update the history before returning
                self.update_history(candidate)
                return candidate

    def is_random_enough(self, candidate, start, end):
        """
        Determine whether the candidate number is 'random enough' based on several checks:
         1. Ignore the checks if the history has fewer than 3 elements.
         2. Check for simple arithmetic progression.
         3. Check for immediate repeating sequences.
         4. Check for alternating sequences.
         5. Use a simplified "compressed description" measure to avoid easily describable sequences.
        
        :param candidate: The number to check.
        :param start: Lower bound for the random number (inclusive).
        :param end: Upper bound for the random number (inclusive).
        :return: True if the candidate passes all checks, False otherwise.
        """
        
        # If history is too short for pattern detection, accept the candidate immediately
        if len(self.history) < 3:
            return True

        # 1. Check for an arithmetic sequence such as [3, 5, 7]
        if self.check_arithmetic_sequence(candidate):
            return False
        
        # 2. Check for repeating sequences like [4, 4]
        if self.check_repeating_sequence(candidate):
            return False
        
        # 3. Check for alternating patterns like [10, 20, 10, 20]
        if self.check_alternating_sequence(candidate):
            return False

        # 4. Check the simplified compressed description length.
        #    The idea is that if the sequence can be described in a very short "compressed" form,
        #    it might be too predictable. We compare it to a fraction (0.8) of the total possible
        #    information content (log2 of the range size).
        if self.compressed_description_length(candidate) < 0.8 * math.log2(end - start + 1):
            return False

        # If all checks are passed, it's "random enough"
        return True

    def check_arithmetic_sequence(self, candidate):
        """
        Check if adding 'candidate' to the history forms a simple arithmetic progression.
        
        :param candidate: The new number.
        :return: True if the difference between the last two numbers in history matches
                 the difference between candidate and the last number.
        """
        # Need at least two numbers in history to detect an arithmetic progression
        if len(self.history) < 2:
            return False
        
        # Differences: (history[-1] - history[-2]) vs. (candidate - history[-1])
        diff1 = self.history[-1] - self.history[-2]
        diff2 = candidate - self.history[-1]
        return diff1 == diff2

    def check_repeating_sequence(self, candidate):
        """
        Check if 'candidate' repeats the immediately preceding number.
        
        :param candidate: The new number.
        :return: True if candidate is identical to the last number in history.
        """
        # Ensure history is not empty, then compare candidate to the last generated number
        return len(self.history) > 0 and candidate == self.history[-1]

    def check_alternating_sequence(self, candidate):
        """
        Check if 'candidate' forms an alternating pattern with the last two numbers, e.g., [x, y, x].
        
        :param candidate: The new number.
        :return: True if candidate matches the item two positions ago, forming an alternating pattern.
        """
        # Need at least two numbers to see an alternation
        if len(self.history) < 2:
            return False
        
        # If the new candidate matches the number from two steps ago, we have [old, new, old]
        return candidate == self.history[-2]

    def compressed_description_length(self, candidate):
        """
        Calculate a very simplified "compressed description length" of the last two numbers
        plus this candidate. Here, we do a naive run-length encoding of the sequence and sum
        the log2 of each distinct number and its repetition count.
        
        :param candidate: The new number being evaluated.
        :return: A numeric value representing a rough measure of the sequence's "complexity."
                 Lower values mean it could be easily described, suggesting it might be less random.
        """
        # Consider the last two generated numbers and the new candidate together
        sequence = self.history[-2:] + [candidate]
        
        # We'll do a simple run-length encoding for the sequence
        compressed = []
        count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i-1]:
                # If the current number is the same as the previous, increment the count
                count += 1
            else:
                # Otherwise, store the previous number and count in the 'compressed' list
                compressed.append((sequence[i-1], count))
                count = 1
        
        # Append the last number and its count
        compressed.append((sequence[-1], count))
        
        # Sum up the log2 of the absolute value of the number (for its "value complexity")
        # and the log2 of the count (for its "repeat complexity").
        return sum(math.log2(max(1, abs(num))) + math.log2(count) for num, count in compressed)

    def update_history(self, number):
        """
        Add a new number to the history, ensuring it doesn't exceed the maximum length.
        
        :param number: The new number to store.
        """
        self.history.append(number)
        
        # If history exceeds max length, remove the oldest entry
        if len(self.history) > self.max_history:
            self.history.pop(0)

# Usage example
# Here, we create an instance with a specific seed for reproducibility,
# generate 20 random numbers between 1 and 100, and print them.
generator = ImprovedRandomGenerator(seed=576)
random_numbers = [generator.random_number(1, 100) for _ in range(20)]
print(random_numbers)
