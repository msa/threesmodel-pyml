# Threesmodel in python using ML inference

## Purpose

I originally developed threesmodel in Ruby, just for fun, just to try out if I could make a solver that would perform
better than I.

It turned out - I could not, or, at least, I was not the one to develop such an algorithm. However, my talanted collegue
Johan Dewe was able to develop e fairly simple algorithm that was on par with a fairly skilled human being (me) at the game.

Now we are approaching the purpose of this particuilar version. I had an idea that it might be possible to develop an
even better performing solver using the most successful games from Johan Dewes algorithm as knowledge base for training a
deep neural network.

I trained a model that showed some promise (mid eighty percent accuracy and a balanced error level between training and validation set).

But in order to get a grasp of the actual performance of the model I need to allow it to actually play some games and
look at the game score distribution and it turns out python is a more suited environment for that purpose.

