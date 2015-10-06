# Paper 5 Summary

##Reference:
Bettenburg, N., Premraj, R., Zimmermann, T., & Kim, S. (2008). "Duplicate bug reports considered harmful... really?" *In ICSM '08: IEEE international conference on Software maintenance,* 337-345. [Link](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4658082&tag=1)

##Keywords:
- *ii1)* Failure: the manifestation of the bug when the users are interacting with the system
- *ii2)* Defect: the error in the source code
- *ii3)* Master report: The bug report that is primarily considered by the testers (it is not necessary the first report on this bug, but most likely the most descriptive)
- *ii4)* Duplicate reports: Secondary reports for a master report
- *ii5)* Duplicate detection: the task of deciding if a bug report is a master report or a duplicate
- *ii6)* Extended master report: a bug report that has information from both the master and the duplicate bugs and more fully captures the nature of the bug

##Notes: <from 1-19>
- *iii1)* Informative visualizations: Figure 2 is a really effective way of displaying the experimental setup (displayed in a much more user friendly format than I have ever seen before)
- *iii2)* Anti-Patterns: This paper has a stellar "Threats to Validity" section. It is very detailed and broken down into section that would help someone improve upon this study are have even more reliable results.
- *iii3)* New results: After comparing the models for the system, they found the SVM outperformed the Bayes models and ended up having an accuracy of 65%
- *iii4)* Future work: This paper states that bug reporting tools need to be improved to help users create more effective bug reports

##Artifacts:
###Motivation: 
In some companies, there are strict rules about writing a duplicate bug to one that is already in the system because it wastes developer resources. However, it is not always easy to tell if your bug has already been submitted and employees have been noted to someone not submit a bug when they are not sure. This culture may prevent bugs from being reported when they are discovered and perhaps prevent high quality bug reports. This paper considers bug reports and hopes to dispell the belief that duplicate bugs are harmful, and replace that with the belief that they are helpful to diagnosing the bug.
###Hypotheses: 
- Duplicate bug reports provide developers with information that was not present in the original report
- The information in bug deplicates can improve automated triaging techniques, i.e., who should fix a bug
###Contributions: 
- Analysis of why duplicates are submitted
- Analysis of what extra information is in bug reports
- Models for automatically identifying duplicates

##Areas for Improvement:
- *iv1)* The calculations that go into the Master and Extended columns in Table 1 are difficult to trust. First, the way that they are coded seems strange (one point for each "unique item"). Also, if it is on a different OS or is a different product shouldn't that just be considered a totally different bug?
- *iv2)* The model performance was displayed for accuracy but it would have also been nice to see the precision, recall and F1 to have a better idea of the models performance. Then discussion about the trade-off between false-positives and true-negatives could have also been introduced.
- *iv3)* Only using the two different modeling approaches (SVM and Bayes) may not be enough. They should probably try other modeling attempts
- *iv4)* Only using lexical items for the classification is also a short coming. It would be helpful to understand some semantics of the system, perhaps identifying things like actions, which could be more highly weighted than nouns or something to that effect

##References (2008-2010):
- Bettenburg, N., Just, S., Schroter, A., Weiss, C., Premraj, R., & Zimmermann. (2008). "What makes a good bug report?" *In FSE '08: Proceedings of teh 16th ACM SIGSOFT International Symposium on the Foundations of Software Engineering.*
- Bettenburg, N., Premraj, R., Zimmermann, T., & Kim, S. (2008) "Extracting structural information from bug reports." *In MSR '08: Proceedings of the 5th Working Conference on Minging Software Repositories.*
- Just, S., Premraj, R., & Zimmermann, T. (2008) "Towards the next generation of bug tracking systems." *In Proceedings of the IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC)*
- Wang, X., Zhang, L., Xie, T., Anvik, J., & Sun, J. (2008). "An approach to detecting duplicate bug reports using natural language and execution information." *In ICSE '08: Proceedings of the 30th International Conference on Software Engineering.*

