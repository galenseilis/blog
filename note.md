# Significant Figures

 Significant figures are a useful way to quantify uncertainty, and it is what I was taught in my earlier scientific education. I recall being expected to track of the number of sigfigs preserved through a calculation, and discard the rest at the end. Or sometimes I would report a bunch of them but communicate which were significant and which were not. We were never told how to derive the uncertainty propagation equations, which ones were exact vs approximate (even in theory; they're all approximate in practice), or what assumptions we were making. We were just expected to do them at that stage. I didn't even realize that they were approximations at the time. But they are practical which can count for a lot.


In a general mathematical view this assumption that sigfigs apply is not necessarily correct. Just the number "3" is also conventionally understood in mathematics to be exact, rather than indicating a single sigfig.. One might write this to mean "3=3.000000...". When I am reading published articles that involve math, and some of them are pure math papers, I don't expect that the rules of sigfigs always apply (b/c they don't). It is more general to consider numbers with sigfigs as a particular mathematical structure rather than something that is inherent to all numbers regardless of context.


There are other ways of quantifying uncertainty. Some that I like, such as probability, and some that I don't such neutrosophy. Well, to be fair, I just don't think I really get the idea of neutrosophy. One of the ones I find intriguing is interval arithmetic. While interval arithmetic has its own limitations, I think it is underutilized.


Then there is probability, of course. This is one of the more theoretically general approaches, and you can derive the familiar error propagation formulae in this context.


There's fuzzy logic. I don't particular like the philosophy around it, but it can be fine as an applied mathematical approach.


There's also floating point precision and the roundoff error that occurs when you do arithmetic in a computer. In this context even starting with exact numbers as inputs to a calculation can give inexact outputs.


When it comes to reporting, I tend to have varying opinions depending on the context. If we're talking about raw data, then I want every digit reported. Most analytical instruments don't spit out more than 6 digits anyway, and some forms of data are exact. Data that appears exact may still have uncertainty. Perhaps you figured you counted 20 butterflies, but there is a chance that the count isn't correct. What are the sigfigs then? An alternative is to model the uncertainty with probability distributions.


Another consideration is sensitivity analysis. If it has been independently and repeatedly show that that the sigfigs don't change the results enough to change decisions, then those sigfigs are practically irrelevant to those decisions.  Removing the consideration of sigfigs may make a decision process 'faster'. I don't personally like throwing away decimal places, but lack of sensitivity can sometimes be demonstrated.


