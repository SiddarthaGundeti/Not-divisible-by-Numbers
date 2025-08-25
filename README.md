# Not-divisible-by-Numbers

Input: 5633

Output: True

Question Explanation:

The program is designed to check if a given number N is not divisible by any of the numbers 2, 3, 5, and 7. 

Logical Approach:

Read Input:
Read the number N as an integer.

Check Divisibility by 2, 3, 5, and 7:
Check if N is not divisible by 2. This is done by checking if N % 2 is not equal to 0. Store the result (True/False) in divided_by_2.
Similarly, check for divisibility by 3, 5, and 7, and store the respective results in divided_by_3, divided_by_5, and divided_by_7.

Evaluate Final Condition:
Use a logical and to combine the results of the divisibility checks. If all conditions are true (meaning N is not divisible by 2, 3, 5, and 7), store the result (True) in result. If any one condition is false, result will be False.

Output:
Print the boolean value of result. True means N is not divisible by 2, 3, 5, and 7. False means N is divisible by at least one of these numbers.

Example for Clarity:

If the input N is 5633:
5633 % 2 is 1, so divided_by_2 is True.
5633 % 3 is 1, so divided_by_3 is True.
5633 % 5 is 3, so divided_by_5 is True.
5633 % 7 is 4, so divided_by_7 is True.
Since all conditions are True, the final result is True.

The output will be: True

