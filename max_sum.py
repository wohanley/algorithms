# This function finds the subsequence with the largest sum in a given
# sequence.
#
# You just need to go through the sequence summing elements
# and recording the maximum until you dip into negative numbers, at which
# point you reset the current running sum to 0. Once you've been through the
# entire sequence, your maximum recorded sum is the maximum sum.
# 
# Runs in O(n), just a single loop over the sequence.

def max_sum(sequence):

    current_sub_max = 0
    current_global_max = 0
    subseq_start = 0
    subseq_end = 0

    for i in range(len(sequence)):
        current_sub_max += sequence[i]

        if current_sub_max <= 0:
            subseq_start = i
            current_sub_max = 0

        if current_sub_max > current_global_max:
            current_global_max = current_sub_max
            subseq_end = i

    return sequence[subseq_start + 1 : subseq_end + 1]
