### Motivation

The [Asian Parliamentary Debate format](https://www.debate-motions.info/debate-formats/asian-parliamentary-debate-format/) has teams debate topics, but unusually it features three topics instead of one. Each pair of competing teams selects one topic from those three based on their aggregated preferences. The mechanism is simple; both teams independently assign each of the three topics a rank of 1, 2, or 3 (1 being most favoured). These ranks are summed together and the topic with the lowest rank sum (ties broken in favour of the topic with lower-variance rankings) is chosen.

This mechanism, of two teams expressing preferences between three options to narrow them down to one, can be generalized.

# Choice Mechanisms

I define a choice mechanism $C : P \rightarrow O$ as a function from a collection of preference sets $P$ to an option set $O$. The collection of preference sets represents all possible preference sets of a collection of agents. The option set represents all possible outcomes of a choice. $C$ maps a given preference set to a single element in the option set. As a starting point of inquiry, I assume that the collection of preference sets is truthful.

The aim of designing a choice mechanism is, as in much of mechanism design, to maximize social welfare. We can define some salient metrics.

## Performance Guarantees

I use performance guarantee $P$ to describe any of a number of desirable property that $C$ should have. $P$ is how we formalize social welfare in this context - it is defined such that a mechanism that satisfies $P$ will provide high social welfare.

Our first example of $P$ is derived from the example of debating. The mechanism described in that instance has the desirable property that any topic which is ranked 3 by even one team will not be debated. In other words, teams are guaranteed not to debate their least-preferred topic.

Thus, 
