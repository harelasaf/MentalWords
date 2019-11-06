# MentalWords
Using openBCI to classify covert words

This work is based on @Jag Singh's work from https://towardsdatascience.com/merging-with-ai-how-to-make-a-brain-computer-interface-to-communicate-with-google-using-keras-and-f9414c540a92

Basically, utilizes the openBCI GUI to transmit data on LSL, read that data to record 2 second sub-vocalized words,
then train a CNN to classify these words and send them to a Google query.

Libraries in use:
Numpy, Keras, Pandas, pyopenBCI, pylsl and maybe others... it's written in the code really - you should be fine. :)
