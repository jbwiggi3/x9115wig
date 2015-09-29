# Paper 3 Summary

##Reference:
Sureka, A. & Jalote, P. (2010). "Detecting Duplicate Bug Report Using Character N-Gram-Based Features." *Proceedings of the 2010 Asia Pacific Software Engineering Conference*, 366-374. [Link](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5693213&tag=1)

##Keywords:
- *ii1)* Semantic similarity: how similar one meaning is to the other (for example "hello my name is Steve" is more semantically similar to "they call me Steve" than "hello my name is Bob")
- *ii2)* Lexical similarity: how similar the words in one set are to another set (for example "hello my name is Steve" is more lexically similar to "hello my name is Bob" than "they call me Steve")
- *ii3)* Super-word features: features that span across the limit of a single word
- *ii4)* Defect: an element of a software artifact that is not functional or not present.
- *ii5)* Eclipse: an integrated development environment (IDE) for java which is publicly available and open sources its bug reports (the focus of this study)

##Notes: <from 1-19>
- *iii1)* Related work: This paper has a good representation of other articles from this area and does a good job contrasting their approach with the other studies approach to highlight their strengths.
- *iii2)* Sampling proceedures: The eclipse bug respository was chosen to be the focus of this work because it is very large (>200K entries), already has the duplicate bugs tagged and is a real bug respository which will help reveal the usefulness of this approach to industry.
- *iii3)* Baseline results: The paper mentions the recall rate of other approaches 
- *iii4)* New results: This paper makes a good case for using this n-gram approach in future automatic triaging, solving many problems (see contributions sections).

##Artifacts:
###Motivation: 
Identifying duplicate defect reports automatically avoids having multiple developers working on the same problem and gives a more holistic representation of the bug. When attempting to identify duplicates by considering high-level features, such as the words used in a bug report, automatic triaging is susceptible to dependence on a certain language, noisy data and handling domain specific term variations. A lower-level feature, such as character level features overcome these boundaries. Methods need to be developed to overcome these limitations.
###Hypotheses: 
Character n-gram-based features will out-preform high-level features based models for predicting duplicate bugs.
###Contributions: 
- This character level approach provides the following advantages over word-level representations: 1) Ability to match concepts from system messages; 2) Ability to extract super-word features; 3) Handling misspelled words; 4) Ability to match short-forms with their expanded form; 5) Ability to match term variations to a common root; 6) Ability to match hyphenated phrases
- This paper provides an empirical evaluation of the character level approach on a publicly available Eclipse bug dataset, which is significantly larger (200K vs. <50K entries) than its predicessors

##Areas for Improvement:
- *iv1)* Table 1 was not very effective at visually conveying that the bugs were duplicates. It would probably be more effective if the first column (BUG ID) was replaced with a high level description of the bug being reported.
- *iv2)* Some text was devoted to breaking down phrases into different n-grams and that would have been more effective as a graphic.
- *iv3)* There should have been more mention of the weakness of this approach such as, when it mistags a duplicate bug, why does this approach?
- *iv4)* There is no future work section in this paper or any allusion to it in the conclusion section. It is difficult to speculate what the next steps should be as a reader and it would be nice to see what direction this line of work could go in. As it stands, I'm not sure that this approach is really that strong and without room for improvement I wonder if this is work worth doing.

##References (2008-2010):
- Nguyen, T., Weimer, W., Le Goues, C., & Forrest, S. (2009). "Fixing Software Bugs in 10 minutes or less using evolutionary computation." *In the 6th Annual Human-Computer Competition HUMIES AWARD.*
- Hassan, A., & Xie, T. (2010). "Mining software engineering data." *In Proceedings of the 32nd International Conference on Software Engineering (ICSE 2010), Companion Volume, Tutorial.*
- Jalbert, N., Weimer, W. (2008). "Automated duplicate detection for bug tracking systems." *In DSN 2008: 38th Annual IEEE/IFIP International Conference on Dependable Systems and Networks,* p. 52-61.
- Kemp, T. (2009). "Automated detection of duplicate free-form english bug reports." *In MS Computer Science Thesis, Department of Computer Science, Morgantown, West Virginia.*
- Sun, C., Lo, D., Wang, X., Jiang, J., & Khoo, S.C. (2010). "Discriminative model approach towards accurate duplicate bug report retrival." *In ICSE 2010: Proceedings of the 32nd international conference on Software Engineering.*
- Wang, X., Zhang, L., Xie, T., Anvik, J., & Sun, J. (2008). "An approach to detecting duplicate bug reports using natural language and execution information." *In ICSE '08: Proceedings of the 30th international conference on Software Engineering,* p. 461-470.
