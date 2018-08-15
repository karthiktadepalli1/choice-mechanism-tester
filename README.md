## Voting
Many voting mechanisms require voters to provide a ranking of their preferences. Social choice theory focuses on which of these mechanisms can yield the best outcomes. Here I use computational methods to explore some voting mechanisms and some definitions of "best outcomes" to see whether a particular voting mechanism robustly provides a given "best outcome". 

### Performance guarantees
Let's define the outcomes we want any voting mechanism to have as *performance guarantees*. We want to test the robustness of such performance guarantees to changes in a) the number of voters, b) the number of candidates. 

**Performance guarantee 1 (G1):** For n voters and m candidates, the winning candidate should be ranked k or worse by no more than j candidates.

Intuitively, this is the idea of the *least disliked candidate* being preferred. If some fraction of voters rank the candidate below a threshold rank, G1 is equivalent to the claim that this candidate will not be elected. The ideal fraction and threshold rank to use are best determined contextually, but a reasonable starting place is k = m // 2 and j = n // 2, i.e fewer than half of voters should rank the candidate in their bottom half of rankings.

My social choice tester implements G1 as check_g1() in the checker.py file.

**Performance guarantee 2 (G2):** the winning candidate under a voting mechanism should win every head-to-head comparison between them and another candidate under the same voting mechanism. (The Condorcet Criterion)




> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1ODM2ODIxNDgsMTcyNjc0Mzk5Nl19
-->