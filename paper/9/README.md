# Paper 9 Summary

##Reference:
Rastkar, S., Murphy, G. C., & Murray, G. (2014). Automatic summarization of bug reports. Software Engineering, IEEE Transactions on, 40(4), 366-380. [Link](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6704866&tag=1)

##Keywords:
- *ii1)* BRC: bug report classifier
- *ii2)* Extractive summary approach: in this method of summarizing, the contents of the summary are pulled directly from the parts that are being summarized.
- *ii3)* Abstractive summary approach: in this method of summarizing, the contents of the summary are generated based on a semantic representation of the things that are being summarized
- *ii4)* Stakeholders: agents who are involved with the code (like the marketing team, the manager, the user, the developer), many of which are not technical and could benefit from summarized bug reports.

##Notes: <from 1-19>
- *iii1)* Patterns: The paragraph on "Experimentation Method" goes into a lot of detail about how the experiment was carried out and makes the process repeatable, which is very helpful to experimenters trying to duplicate these results.
- *iii2)* Anti-patterns: The section "6.5 Threats" talks about the short comings of the study and the method and points out aspects that could be improved. This is helpful to someone looking to improve upon this line of work.
- *iii3)* Study Instruments: The section labeled "6.4.3 Participant Satisfaction" reviews some surveys that were given to the participants but they do not go into much detail about the survey or the way it was administered to the participants. This is one part of the study that the "Experimentation Method" did not cover and would not be able to be repeated.
- *iii4)* Statistical tests: p-Values were used to compare the classifiers but the n was too small for other aspects of the study for the authors to use statistical tests. Due to the lack of statistical tests, it is difficult to determine how strong some of the results are.

##Artifacts:
###Motivation: 
Although methods for automatically triaging have become much more effective, it still leaves developers with several bugs and comments on bugs to review before they can proceed to try to fix the bugs. It could be very helpful if duplicate bug reports could also be automatically combined and summarized into a brief summary that the developer could read, getting all relevant information and then be able to attack the bug, informed.
###Hypotheses: 
- Can we produce good summaries with existing conversation-based classifiers?
- Can we do better with a classifier specifically trained on bug reports?
- Do developers prefer working with summaries over original bug reports in duplicate detection tasks?
###Contributions: 
- Demonstrates that accurate summaries for bug reports can be generated
- Reports on a corpus of 36 bug report chosen from 4 separate systems
- Demonstrates the usefulness of training the classifier on bug reports versus non-bug reports
- Shows the automatically generated summaries are judged as helpful to developers

##Areas for Improvement:
- *iv1)* A big issue with this article was that a lot of the claims made were not specific enough to be verified or understood. For instance, in the abstract: "This summarizer produces summaries that are statistially better than summaries produced by existing conversation-based generators." Using "better" and other places throughout the paper really distracts from the message.
- *iv2)* Some decisions in the paper seem abritary, such as making 100 word summaries and only targeting bugs longer 300 words for summarizing.
- *iv3)* This paper had a very small n of 36. It is understandable that gathering a larger corpora could be time intensive, but in a task like summarizing, there are so many possibilities of what the documents getting summarized might contain, it seems that 36 is too small to capture that variance.
- *iv4)* Table 10 is not very easy to understand at a glance, taking me several minutes to understand. I would consider changing time data points from time in minutes to z-scores so that we could see the relative difference between the Tasks and participants.
