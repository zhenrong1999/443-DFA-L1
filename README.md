# 443-DFA-L1

CPT 443 Assignment
2021/2022
Report Due: 27 May 2022 Program Demo: 28/29/30 May 2022

eLearn:

1. Softcopy of Report – PDF,
2. Source Code of Program

Write a well-structured, well-documented recognizer Deterministic Finite Automata (DFA) for the
assigned language. The program must be based on a complete DFA for the language, but you can
terminate the program on entering a trap state. You MUST process one character at a time from left
to right simulating a finite state machine. No other strategy for your program is allowed.
Each student will be given a different language to search for. For program development, a text file will
be given as example for implementation and testing. During the demonstration day, you may use the
given sample text or new text file to demo your machine.
For demonstration purpose, the output from the run must show the following:
 The pattern (input string).
The text used for demo.
The status (whether accept/reject).
Additional information (the position of the pattern found, occurrences of patterns, visualization using
boldface of the pattern occurred in the text etc.).

You also hand in a typed technical report on your project. Recommended outline:
I. Introduction – state your language, define your scope and give the complete DFA (sample DFA if the
complete one is too huge).

II. Implementation Information

    a. how your read and processed the strings
    b. overview of programming constructs used for your program

III. Conclusion – Summary

IV. Appendix – Sample/Full programs.

``
Σ = { a,..z, A,..Z, 0,…9, and other symbols found the sample text}``

Example languages

``
L = {w ∈ Σ *| w contain substring “Malaysia”, “Kuala Lumpur”, “Penang” ...}
``

``
L = {w ∈ Σ* | w contain substring “2 litres”, “1kg”, “100%” ...}``

L1. Place Finder (E.g. Country, Organization, Shops, States etc.)
Example: Malaysia, Australia, Penang, Pizza Hut, Intel etc.

Open Window Terminal Powershell.

``` powershell
conda init powershell
```

Restart powershell

``` powershell
conda env create -n 443-DFA-ASN --file ENV.yml
```

## Additional for not importing ENV.yml

``` powershell
conda config --env --set channel_priority strict
```

``` powershell
conda install --channel conda-forge pygraphviz
```

``` powershell
pip install - r requirements.txt
```

## Steps to run scripts

``` powershell
conda activate 443-DFA-ASN
python main.py
```

## Steps to test src codes

``` powershell
./.env/Scripts/activate
python -m pytest ./test
```

## Reference

- [Malaysia Area Names](https://www.citypopulation.de/en/malaysia/cities/)

- [Wiki Location Names and Organization](https://event.ifi.uni-heidelberg.de/?page_id=532)

- [Wikipedia continent](https://en.wikipedia.org/wiki/Continent)