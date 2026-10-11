**HW \#2 – Solving the n-queens problem**

We have discussed the 8-queens problem ([https\://en.wikipedia.org/wiki/Eight\_queens\_puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle)) in class.

Now is your time to have some fun with it\!\!\!

I will give you code to use as a base, solve\_queens\_dfs, for the n-queen problem that uses DFS with backtracking.  It works but isn’t nearly as efficient as many other possibilities that we’ve discussed in class.  

The workbook I made about this code is at:

[https\://colab.research.google.com/drive/1QwgdCtwzYAXca4zTm4\_nt7X7uOhJJTAN?usp=sharing](https://colab.research.google.com/drive/1QwgdCtwzYAXca4zTm4_nt7X7uOhJJTAN?usp=sharing) 

Your homework will be to implement five new additional ways of solving the problem (discussed later below) in addition to the British Museum and DFS implementations. Similar to homework \#1, we are interested in counting how long it took to find a solution through metrics that count the number of actions within the logic (compare this to the number of pushes and pops from homework \#1). However, this time we will quantify it via actual time.

Note this example for measuring time:

[https\://colab.research.google.com/drive/1W0YoiDUfeTl1YR52Arl4kP6BlRNAFHcy?usp=sharing](https://colab.research.google.com/drive/1W0YoiDUfeTl1YR52Arl4kP6BlRNAFHcy?usp=sharing) 

which I recommend you basing yourself on for measuring time.

**Your goal**: Solve all n-queens problems from 8 up to 100 queens as quickly possible.

Hint: You **are** encouraged to make the is\_place\_in\_next\_row\_valid function more sophisticated if needed, particularly in the forward checking solution. Also, you will consider several variations of Hill-Climbing as per the options below.

**Your Assignment:**  Compare the following 4 implementations and their counters:

1. The British Museum—The easiest algorithm to beat. For example, I found that solving the 8-queens problem this way took over 4 billion (\!) iterations.  DO NOT try solving the queens problem past 8 with this method. In fact, even the 8 queens instance can take nearly an hour\!  I would suggest you check it first for 4 or 6 queens and only if that works relatively fast, try to do the 8 queens instance. If it doesn’t report on the 4 or 6 queens instance instead.  
2. DFS with Backtracking – pretty straightforward and deterministic. Given as the baseline to beat.  Do not try solving past 25 with this.  
3. Heuristic Repair/Stochastic Search—can be just like we discussed in class (with random initial placement) or not (only putting down one queen and then doing DFS).    
4. Forward Checking.

Consider four Hill-climbing options plus Forward Checking:

1. The basic Hill-climbing. In the first option, consider this classic implementation:  
   1. Put down n-queens  
   2. Select the queen with the most constraints (like in class)  
   3. Try fixing that queen.

   Note: this option will often get stuck.

2. The slightly more advanced option is to restart if you don’t find a solution after a certain amount of time (a parameter you can and should tune).  Consider this implementation:  
   1. Put down n-queens  
   2. Select the queen with the most constraints (like in class)  
   3. Try fixing that queen.  
   4. If after a certain number of iterations you don’t find a solution, or if there is no move that reduces the number of constraints, go back to step-1  
3. An even more advanced option is to try to sideways correction (e.g. same number of constraints but different board) before you restart if you don’t find a solution after a certain amount of time (a parameter you can and should tune).  Consider this implementation:  
   1. Put down n-queens  
   2. Select the queen with the most constraints (like in class)  
   3. Try fixing that queen.  
   4. If there is no move that reduces the number of constraints, try a sideways configuration with queens in different positions even if it doesn’t improve the solution  
   5. If after a certain number of iterations you still don’t find a solution go back to step-1  
4. Another way to improve things is to select any improvement instead of just the “best” improvement. As this video shows, this can be faster.  

   [https\://www\.youtube.com/watch?v=7fjmGWkv-sY](https://www.youtube.com/watch?v=7fjmGWkv-sY) 

   Similarly choosing the next placement randomly instead of the first possible position can also help.

5. A Forward checking solutions similar to what we discussed in class. 

**Pedagogic note:** you could say that the methods that some of these heuristic repairs think more “humanly” (options B and D resonated with *me*) and those using search ordering heuristics like forward checking are more “rational”.  

To show how well your best algorithm works, create a table for how long each of the options took.  Your table could look like this:

| Algorithm | Time (Seconds) |
| :---- | ----: |
| British Museum with n=8 (or 4 or 6\) | 1234 |
| DFS from n=8 to 25 | 49.9 (18 of 18\) |
| Simple Hill-Climbing | 0.04 (0 of 93\) |
| Hill-Climbing with Simple Restart | 67.1 (37 of 93\) |
| Hill-Climbing with Sideways Correction | 2.28 (93 of 93\) |
| Hill-Climbing with Simple Heuristic | 1.18 (93 of 93\) |
| Forward Checking | 1.34 (93 of 93\) |

**Reflection Question:** How did your algorithms compare?  It is possible that your Simple Hill-Climbing had a hard time getting to 100, and that in fact is to be expected. However, how much did your other variations take?  What is the difference in their complexity?  (No need to compute it, but note that the first three Hill Climbing all use a “fancy” check to find the best queen to move, while the last one doesn’t. How much did that impact things?)  How did forward checking fare in comparison for you?

Grade Breakdown:

50 points – providing a working solution for the British Museum algorithm, Heuristic Repair and Forward Checking Algorithms. 

30 points – correct logging for the counters for all algorithms. At least 3 of the algorithms must have solved all queens from 8 to 100 in under one minute to get full credit for this section. As was the case for the first homework, have the code output the values for the table. There is no need to make a better formatted output such as in Excel, but do include the output you had as a comment at the end of your code.

20 points – documentation of logic used – especially for how you cut down search times in your implementations. Include support for how you selected parameters like the number of steps you consider side steps, how much time until you restarted the problem and how you implemented the forward checking solution.

Submission: via Git as usual.

**Due date: October 12, 2026 (first Monday after classes resume)**