# This function finds the Longest Increasing Subsequence (LIS) in a 
# sequence seq.
#
# We define max_lengths, an array where max_lengths[i] is the
# length of the LIS of seq up to i. This can be defined recursively as the
# maximum element of max_lengths up to i, plus one.
# 
# Runs in O(n^2) thanks to nested loops.

def lis(seq):
    lis_lengths = [None]*len(seq)
    for i in range(len(seq)):
        max_size = 0;
        for j in range(i):
            if seq[i] > seq[j]:
                if lis_lengths[j] > max_size:
                    max_size = lis_lengths[j]
        lis_lengths[i] = max_size + 1;

    max_size = 0
    for i in range(len(seq)):
        if lis_lengths[i] > max_size:
            max_size = lis_lengths[i]

    return max_size
