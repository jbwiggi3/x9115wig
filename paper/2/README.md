# Paper 2 Summary

##Reference:
Wang, X., Zhang, L., Xie, T., Anvik, J., & Sun, J. (2008). "An Approach to Detecting Duplicate Bug Reports using Natural Language and Execution Information." *Proceedings of the International Conference on Software Engineering*, 461-470. [Link](http://delivery.acm.org/10.1145/1370000/1368151/p461-wang.pdf?ip=152.7.224.2&id=1368151&acc=ACTIVE%20SERVICE&key=6ABC8B4C00F6EE47%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&CFID=540221454&CFTOKEN=34045547&__acm__=1441977963_fb4ec257e3ff958aca4b3c5d2918358c)

##Keywords:
- *ii1)* Execution information: runtime error reports, feature requests, and patch reports
- *ii2)* Target report: the original bug report that the other reports duplicate
- *ii3)* Suggested list: the set of bug reports retrieved for examination for a given new bug report
- *ii4)* Runtime error reports: A bug report that reports on a software failure during its execution
- *ii5)* Feature requests: A bug report that asks for some new functionality at a certain point in execution
- *ii6)* Patch reports: A report on the new patch by the developers (Unlikely to have duplicates)

##Notes: <from 1-19>
- *iii1)* Related work: They do a great job situating their work in the body of literature and showing how their methods are improvements over the previous work.
- *iii2)* Anti-patterns: This paper does a good job talking about the potential confounds in their paper in 5.4 Threats to Validity. This adds a lot to the paper because it gives a strong direction for how the analysis could be refined to be less biased and helps you be skeptical about certain ascpects of the paper.
- *iii3)* Graphics: They are missing figure 1, which makes it diffult to follow some of the text. This is a major short-comming. However, the other graphics are very effective at showing off the effectiveness of the formulas.
- *iii4)* Future Work:  They hope to extend this analysis to larger datasets. They also believe that similar approaches could be used to help prioritize bug reports, which would again decrease the amount of effort that developers extend reviewing the bugs.

##Artifacts:
###Motivation: 
The paper states that identification of duplicate bug reports automatically would allow for higher volume and velocity of bug reports to be addressed and that would result in increased possibility of revealing defects and quality of the software product. It also allows the software product to evolve to the user's believes about how it should work, increasing its ability to suit user needs.
###Hypotheses: 
By adding in execution information, duplicate bugs can be more accurately combined and save development time and improve product quality.
###Contributions: 
- Showing th benefit of adding execution information and natural language information when combining bugs
- Description of the approach for determined duplicate bugs
- Empirical results concerning different heuristics
- Evaluting on the Firefox bug repository

##Areas for Improvement:
- *iv1)* The dataset that they are using is not introduced very well so it is difficult to grasp exactly what components the corpus has, how large it is and have similar it is to standard bug reports.
- *iv2)* While the sub sections under section 2 are useful, they do not help the reader understand what is meant by execution information. I feel like more examples of execution information tagging and context would have been much more informative than examples of similar descriptions, which could be easily imagined.
- *iv3)* I am also not convinced that natural language solutions are as weak as they are presented. It seems that if the testers were instructed to use more word in their descriptions or enumerate steps, then there would be more context for the natural language solutions to observe and their performance would be improved.
- *iv4)* The manual recreations of the execution errors really concern me. It seems that this would make it highly likely that in a report someone thinks is similar, they would just carry out the exact same recreations.

##References (2008-2010):
No references from this period
