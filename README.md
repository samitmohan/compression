~ notes


https://www.youtube.com/watch?v=jhgHaV-VaZY&t=374s


The idea is that to understand something is to find patterns and regularities in it. 
If you can find these patterns, you can describe the information more concisely (compress it). 
This is related to Ockham's Razor: simpler explanations (more compressed models) are generally better.

Prediction: The ability to compress well implies an ability to predict well. If you understand the underlying structure of a sequence of data, you can predict what comes next.


In search for intelligence -> Motivaiton -> geohot



How to measure intelligence, is there a turing test for it?
How do i go on learning about compression and intelligence and hutter prize via basics (shannon, huffman coding) -> more complex coding now -> python compression algos -> LLMs and how they use compression -> attempt to solve hutter prize / understand it via LLMs.
What is the strucutre of this project



Goal -> Need a framework for AI
What is intelligence
# what is compression
lossless compression implies intelligence?

For the longest time I've looked for the definition of intelligence. I don't know it. But I do know the definition of compression. As I read more about it I realize intelligence is just compression (lossless) -> and AI is just compression (this is when I read about the Hutter Prize for the first time and it changed my model to think about intelligence)

So I've decided to dive deep into this topic. 
Goals -:
- Know what intelligence is -> how does it work
- What is compression -> origins -> what does it mean now?

I've also been a huge fan of the TV show silicon valley and Richard Hendricks builds a middle out compression algorithm. Basically building intelligence and AGI later on. So how does it work.

## Basics 

Since this is basics I will start off with text words. Images can have lossy compression but words can't. Can't have a bit off in word compression otherwise it changes the meaning of the entire sentence.

So all alphabets in computers are stored in 8 bits (1 byte) since 8 is a power of 2, easily divisible etc...

Taking a string "abc" -> convert that into bits -> (01100001 01100001 01100001) pretty cool -> stores it as one long string and then computer divides this so we can read it/decode as abc.

What is the issue with this? let's say a space bar is "0" and 0 is "00"
so if the string is "0000" how do we know its 4 space bars or the 0s twice? What is the separator? Plus it's going to take a lot of bits like this to represent a text file. How do we make this string of 0s and 1s shorter? without losing data? compression. 

Taking a sample text and converting it -:



### Attempt Hutter Prize


Shannon Encoding
Huffman Encoding
Lempel Ziv Encoding
Script for Weisman Score
Middle out compression
https://www.youtube.com/watch?v=VQ7ydeSqjS4
Python Compressions

Compression at LLM level
AI is compression Hutter Prize
LLMZip

