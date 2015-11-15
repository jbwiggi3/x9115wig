# Paper 8 Summary

##Reference:
Nguyen, A. T., Nguyen, T. T., Nguyen, T. N., Lo, D., & Sun, C. (2012, September). Duplicate bug report detection with a combination of information retrieval and topic modeling. In Automated Software Engineering (ASE), 2012 Proceedings of the 27th IEEE/ACM International Conference on (pp. 70-79). IEEE. [Link](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.364.8064&rep=rep1&type=pdf)

##Keywords:
- *ii1)* DBTM: a duplicate bug report detection approach that takes advantage of both IR-based features and topic based features (a contribution of this paper)
- *ii2)* IR: Information retrieval approaches which can help with automatic triaging but do not do a good job of detecting the same technical issue written in different descriptive terms
- *ii3)* SVM: Support Vector Machine which is a machine learning technique
- *ii4)* Automatic Triaging: automatically determining which bugs are duplicates of one another
- *ii5)* NLP: natural language processing, methods for processing words and understanding their meaning automatically

##Notes: <from 1-19>
- *iii1)* Pattern: This paper contains an interesting section titled "Implications" on page 72 in which they justify this line of work and I think it is effective at backing their thoughts behind why topic-based features will make large contributions to automatic triaging and the quality of the involved code.
- *iii2)* Informative visualizations: The variety of graphics helps capture several elements of the paper that would be difficult to explain only in the text. In particular, figure 4 (Document Modeling) effectively shows the connection between the bug reports and the topic assignments.
- *iii3)* Commentary: Not only does the paper include a lot of effective visualizations to describe the topic modeling proceedure, but they also show the algorithm which ultilized the topic models in the Prediction Algorithm in figure 6 on page 75.
- *iii4)* They put in examples of potential bug reports and used them to push the conversation forward, but in justification of the technique and how it is applied.

##Artifacts:
###Motivation: 
Triaging is a time consuming task for developers and becomes more difficult when there is a high volume of bugs.
###Hypotheses: 
Building topic-based features will help capture the general idea of the bug and that idea will help connect duplicate bugs.
###Contributions: 
- DBTM was introduced and its interworkings were revealed by the paper.
- DBTM was shown to have a 20% in accuracy over state-of-the-art approaches

##Areas for Improvement:
- *iv1)* While this technique is preforming well on the set of duplicates but it should also be considered in a more realistic setting in which a large proportion of the reports they are encountering are duplicates and have their own separate topic.
- *iv2)* Figure 5 is difficult to understand even with the text on page 73 that supports it. It probably would have been more effective to keep the narrative going that was between figure 3 & 4 on the previous page and then ground the idea.
- *iv3)* There is not a future work section and although some potential room for improvement can be seen through reading the paper, it would be helpful to the research community if these sections were explicitly stated.
- *iv4)* The conclusion is also very short and could be beefed up with other results from the paper or thoughts they have about their analysis. As is, it seems to be only a rewording of their abstract.
