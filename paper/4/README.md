# Paper 4 Summary

##Reference:
Bettenburg, N., Just, S., & Schroter, A. (2008). "What Makes a Good Bug Report?" *Proceedings of the 
16th ACM SIGSOFT International Symposium on Foundations of software engineering*, 308-318. [Link](http://dl.acm.org/citation.cfm?id=1453146)

##Keywords:
- *ii1)* CUEZILLA: a tool that considers bug reports and makes suggestions on how the report could be improved to better meet the developers needs (based on empirical research)
- *ii2)* Reporters: the people (usually end-users but can also be developers) who made the bug reports
- *ii3)* Quality of bug reports: a bug report's ability to convey the intended bug that was encountered and supply the developer with information which will aid in addressing this bug.
- *ii4)* Consistency: this means that any answer to the second question in the survey has to be a subset of the answers in the first question or they are removed from consideration.
- *ii5)* Bounces: the amount of people who the surveyers tried to contact and could not reach

##Notes: <from 1-19>
- *iii1)* Sampling Procedures: they go into depth about how they selected their developers and reporters and which people were excluded.
- *iii2)* Baseline results: they show the types of problem bug reports that are given to them and the disconnects between developers and reporters. 
- *iii3)* Informative Visualizations: This article does a great job with visualizations, quickly displaying information to the reader and saving space in the paper. In particular, I think that Table 7 is really helpful and provides a lot of information at a quick glance (however, I am surprized they didn't call this a figure instead of a table).
- *iii4)* Future work: The future work section mostly considers the impact of making improvements to their CUEZILLA tool, but they could have been more specific on what sorts of improvements need to be made.

##Artifacts:
###Motivation: 
A large portion of the development after software releases is based on the bug reports that the developers recieve and the quality of those reports effects how quickly the problems can be fixed. However there is a disconnect between reporters and developers on what is important when reporting bugs and this is effecting productivity.
###Hypotheses: 
After considering what both reporters and developers believe to be important in bug reports, tools can be developed which evaluate the quality of bug reports and then suggest improvements to the report. These improvements to the bug reports will help the bugs be addressed more quickly and effectively.
###Contributions: 
- Responses from 466 developers and reporters on a survey about how bug reports are used
- Empirical evidence showing that bug reports do not usually meet the expectations and needs of developers
- A tool that evaluates bug reports and makes suggestions for how a reporter could improve the bug report so the bugs will get resolved faster and completely

##Areas for Improvement:
- *iv1)* On page 311, Tables 2 and 3 would be more effective if the figure on page 310 that described the color coding scheme was on the same page.
- *iv2)* On page 311, Table 3 shows test cases having 75% but the color coding does not reflect such a high percentage.
- *iv3)* CUEZILLA could be expanded to consider different languages than just C++ and Java
- *iv4)* There definition of completeness of a bug report was revealed in the following quote: "In order to assess the completeness of a bug report, we computed for each group a score based on the keywords present in the bug report. The maximum score of 1 for a group is reached when a keyword is found. In order to obtain a final score we averaged the scores of the individual groups." More information should be provided about this completeness measure and the keywords involved. I also feel like checking the length of the reports is necessary to have higher confidence that the report accurately exposes the bug.

##References (2008-2010):
- Bettenburg, N., Premraj, R., Zimmermann, T., & Kim, S. (2008). "Duplicate bug reports considered harmful... really?" *In ICSM '08: Proceedings of the 24th IEEE International Conference on Software Maintenance.*
- Bettenburg, N., Premraj, R., Zimmermann, T., & Kim, S. (2008). "Extracting structural information from bug reports." *In Proceedings of the Fifth International Working Conference on Mining Software Repositiories.*
- Just, S., Premraj, R., & Zimmermann, T. (2008). "Towards the next generation of bug tracking systems." *In VL/HCC '08: Proceedings of the 2008 IEEE Symposium on Visual Languages and Human-Centric Computing.*

