# musketeer3

This is the git repository of group 4 for the FourthBrain programming assignment "Building and Containerizing a Sentiment Analyzer".

The detailed instructions of the programming assignment can be found in the repository of FourthBrain:
https://github.com/FourthBrain/MLE-6/tree/main/assignments/Week_13


# How to use

Some software need to be installed for running the Sentiment Analyzer webapp. See the above link for installation instructions.

1. Clone the github repository to your local machine:
   git clone https://github.com/roedersen/musketeer3
   
2. Go to the folder of the local repository and switch to huggingface branch:
   git checkout huggingface
   
3. Build the docker image:
   docker build -t fastapi-demo .

4. Run the docker image:
   docker run -dp 8033:8033 fastapi-demo

5. Open the website 127.0.0.1:8033/docs in a browser.

6. Use the "Try it out" button and exchange the "string" with a sentiment (e. g. "awesome"). See the result of the Sentiment Analyzer below.


# Contributors

The contributors for this repository are:
- Evgeny Mun
- Roma Shusterman
- Arno Röder


# License

This repository is licensed under the MIT License and is free to use.
