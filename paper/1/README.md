# Paper 1 Summary

This is a very interesting line of work because it could be integrated into existing systems and decrease the amount of excess work that software developers are having to do in order to address the bugs or ignore bugs that have been addressed. This work seems to have potential for making a strong impact on several large companies and would be helpful for smaller projects as well. In general, it is well motivated and situated in the literature and presents its contribution in an easily interpretable way.

##Reference:
Sun, C., Lo, D., Khoo, S.C., and Jiang, J. (2011). "Towards More Accurate Retrieval of Duplicate Bug Reports." *Proceedings of the 2011 26th IEEE/ACM International Conference on Automated Software Engineering (ASE)*, 253-262. [Link](http://dl.acm.org/citation.cfm?id=2190180)

##Keywords:
- *ii1)* Bug report: a description of an observed defect or missing feature from a piece of software, reported by a tester
- *ii2)* Master report: the first bug report for a particular problem
- *ii3)* Duplicate report: bug reports on bugs that had already been reported
- *ii4)* Triager: person who reviews bug reports and identifies which bug reports are actually duplicates
- *ii5)* REP: a retrieval function to measure the similarity between two bug reports

##Notes: <from 1-19>
- *iii1)* Motivational Statements: Duplicate bug reports consume developer resources when they are not managed, but they are important for understanding the full scope of the bug. This is why this paper looks to combine duplicate bug reports, versus those that would dispose of the duplicates.
- *iii2)* Baseline results: They compare their modified BM25F to the original BM25F and REP-NV to SVM.
- *iii3)* Sampling procedures: Since they were interested in identifying duplicate bugs from large sets that have non-textual/categorial features, they used large bug datasets from Bugzilla.
- *iii4)* Future Work: In the future they plan to integrate processes like these into Bugzilla. This would be 

##Artifacts:
###Motivation: 
During the testing of software bugs are observed by testers and reported. These bugs are then addressed by developers and used to improve the quality of the software artifacts. However, in larger pieces of software, bugs come in great volume and consume significant developer resources. Grouping bugs reports that stem from the same bug is not a trivial task and adds to the burden on the developers. If the bug reports could be automatically combined instead of manually, it would have ripple effects on the quality of the software.
###Hypotheses: 
By combining textual features (e.g. the text of the report) and non-textual/categorial features (e.g. product, component, version, priority, type) duplicate bugs can be identified more effectively than just considering the textual features alone.
###New Results: 
They made a variant of BM25F which showed 3-13% improvement in recall rate@k and a 4-11% improvement in MAP accross four large datasets.
They also made a new retrieval function, REP, which outperformed their previous work with SVM by 10-27% on recall rate@k and 17-23% on MAP.

##Areas for Improvement:
- *iv1)* It seems odd that the authors chose to use BM25F for this task, considering that there are other models which are designed longer queries with duplicate words
- *iv2)* Nowhere in the paper do they talk about the gold standard for identifying duplicate bugs, which is very important. I would suppose it was done by humans, but which humans is also important to know. Was it the developers of the system? Was it the writers of the paper? Was it someone on mechanical turk?
- *iv3)* I believe that this paper also needs to go into more depth about the reported accuracy of the systems. How frequently do the formulas get false positives and true negatives? How likely is it that some duplicates will be grouped together but others will get a new bug bin?

##References (2008-2010):
- Jalbert, N., & Weimer, W. (2008). "Automated Duplicate Detection for Bug Tracking Systems." *Proceedings of the International Conference on Dependable Systems and Networks*.
- Wang, X., Zhang, L., Xie, T., Anvik, J., & Sun, J. (2008). "An Approach to Detecting Duplicate Bug Reports using Natural Language and Execution Information." *Proceedings of the International Conference on Software Engineering*.
- Sun, C., Lo, D., Wang, X., Jiang, J., & Khoo, S.C. (2010). "A Discriminative Model Approach for Accurate Bug Report Retrieval." *Proceedings of the International Conference on Software Engineering*.
- Sureka, A., & Jalote, P. (2010). "Detecting Duplicate Bug Report using Character n-gram-based Features." *Proceedings of teh 2010 Asia Pacific Software Engineering Conference*.
- Bettenburg, N., Premraj, R., Zimmermann, T., & Kim, S. (2008). "Duplicate Bug Reports Considered Harmful ... Really?" *Proceedings of the IEEE International Conference on Software Maintenance*.
- Menzies, T., & Marcus, A. (2008). "Automated Severity Assessment of Software Defect Reports." *Proceedings of IEEE International Conference on Software Maintenance*.
- Bettenburg, N., Premraj, R., Zimmermann, T., & Kim, S. (2008). "Extracting Structural Information from Bug Reports." *Proceedings of the 2008 International Working Conference on Mining Software Repositories*.
- Bettenburg, N., Just, S., Schroter, A., Weiss, C., Premraj, R., & Zimmermann, T. (2008). "What Makes a Good Bug Report?" *Proceedings of the 16th ACM SIGSOFT International Symposium on Foundations of Software Engineering*.
