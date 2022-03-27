# RNJazzerator

Required Modules
- Django
- WolframClient
- myenv

RNJazzerator takes in an audio file, such as a recorded song, and detects the individual note frequencies. Once we have a list of note frequencies, we associate each note with a unique 6-digit binary value. Once we have 171 note values we can make a 1024-digit binary number, which we then use the wolfram one API to check if the number is prime. If the number is a prime, it can then be used for key generation in RSA cryptography. If it is not a prime, you still have generated a very large random number, which can be used for other purposes.

