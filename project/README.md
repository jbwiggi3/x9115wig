# x9115wig - Final Coding Project
## Title: 

##Abstract

###Keywords:

##Introduction
Mutation testing is a way to test your test suite, mutating the code and seeing if the existing test suite can identify the mutant. ____ [citation] pushed this technology to the next level with EvoSuite, by not only mutating code but also test cases to capture mutants automatically. These tests, or oracles, ... Their approach..
For this project I integrated a more sophisticated genetic algorithm and crowd pruner into EvoSuite and will make this publically available on EvoSuite.

##Overview of Algorithms
###Differential Evolution


###MOEA/D

##EvoSuite
EvoSuite is.. In this section, the author will explain how to get EvoSuite running on your local machine. For more information on EvoSuite visit their [website](http://www.evosuite.org/).

###Setting up EvoSuite
EvoSuite is publically available on [github](https://github.com/EvoSuite/evosuite). To begin setup, fork this repository and move your command line (or terminal) directory into the folder it downloaded into. Before beginning, make sure your JAVA_HOME environment variable is correctly set to where the JDK is downloaded.
EvoSuite is most easily installed using Maven ([Link](https://maven.apache.org/)). From command line (or terminal), install Maven using the *'mvn install'* command. Once that is finished, build EvoSuite in the command line with *'mvn compile'*. Finally, to create a binary distribution that includes all dependencies type *'mvn package'*.

###Running EvoSuite
EvoSuite has many capabilities not covered by this readme, so if you want to explore other EvoSuite functionality type *'java -jar evosuite-1.0.1.jar -options'* once the binary distribution has been generated.
To run evosuite, you will need a Java project that has had its .class files generated. I will use a simple program I created called PhysicsBuddy to display what a command to generate a test suite in EvoSuite looks like.

>java –jar evosuite-1.0.1.jar –projectCP /Users/adminuser/Documents/workspace/PhysicsPal/bin –class PhysicsBuddy

As can be seen above, the important elements are the '-projectCP', which stand for project class path and needs to point to where the .class files are generated, and the '-class', which is the name of the class you intend to generate tests for.

##Threats to Validity
One major issue with this work is that it has the flawed assumption that the code is bug free. If there were a bug, it would create tests that will only pass when that bug is present. This is because the system is agnostic of any of the code's objectives, it is only trying to get a thorough test suite. However, this does not mean that the tool is unuseful. Once a piece of code has been tested by developers and users and a large portion of the bugs had been caught, it would then be helpful to run EvoSuite, improving your test suite. This robust test suite would then be ideal for integration and regression testing.

##Conclusions


##Future Work
The algorithms currently evolve agnostic of the pre-existing test cases, which means that original chromosomes are chosen in a pretty ignorant fashion. It would likely improve the system significantly if the original chromosomes were instead based on the pre-existing test cases, making it more likely to reach higher code coverage and have more meaningful tests. It might also decrease the amount of time it takes to reach its final set of test cases.
