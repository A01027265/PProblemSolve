<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Portfolio][moreinfo-shield]][moreinfo-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">P Problem Solver</h3>

  <p align="center">
    A CLI program that verifies input solutions for input K-SAT problems.
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#abilities-mastered">Abilities Mastered</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A CLI program where the user inputs a `.txt` file with a K-SAT problem and a solution to verify. The program then responds with a 1 if the user's solution was accepted or with a 0 if the user's solution was rejected for the K-SAT problem in question.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ABILITIES MASTERED -->
## Abilities Mastered

* Text conversion to correct format (string parsing)
* Efficient verification for P-Problem solutions

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/empobla/PProblemSolver.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Each *P* problem must be saved as a `.txt` file individually inside the `/Input` directory for the program to run properly in the following format (which includes DIMACS CNF):

```sh
c A SAT instance generated from a 3-CNF formula that had 91 clauses and 20 variables
p cnf 20 91
10000111101010101010
9 -3 16 0
4 -16 20 0
-4 6 5 0
-6 -5 4 0
-6 -12 -13 0
-19 -16 13 0
1 -20 -9 0
6 -2 5 0
-4 -11 15 0
-16 8 10 0
-5 2 18 0
-5 8 3 0
-4 -20 -6 0
7 -6 20 0
-17 2 -3 0
-8 -9 -11 0
...
8 10 -19 0
```

Where the first line describes the problem in question, the second line provides a shorthand summary of the problem, and the third line provides an input binary string to be tested against the clauses starting from the fourth line untill the last line.

### Sample Input
Two sample inputs (one that accepts and one that rejects respectively) are provided in the `/Input` directory as `demoaccept.txt` and `Instance_3SAT_example.txt`.

### Output

This program will output a 0 if the binary string provided in line 3 is rejected or a 1 if the binary string provided in the line 3 is accepted.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

This project is property of Emilio Popovits Blake, Patricio Tena, Ana Paola Minchaca, and Rodrigo Benavente. All rights are reserved. Modification or redistribution of this code must have _explicit_ consent from any owner.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Emilio Popovits Blake - [Contact](https://emilioppv.com/contact)

Ana Paola Minchaca García - [Github](https://github.com/anapao-minchaca)

Project Link: [https://github.com/empobla/PProblemSolver](https://github.com/empobla/PProblemSolver)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/emilio-popovits

[Python]: https://img.shields.io/badge/python-3776ab?style=for-the-badge&logo=python&logoColor=ffdc52
[Python-url]: https://www.python.org/

[moreinfo-url]: https://emilioppv.com/projects#p-problem-verifier
[moreinfo-shield]: https://img.shields.io/badge/more%20info-1b1f24?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAApVBMVEUbHyQbHyQbHyRnam2sra+vsbKys7Wsrq+goqQwNDgaHyQaIilbXWGChIZMT1OYmpwYQFoaICYXRF8WUHQZLjwvMzdwcnaztLZ1d3pcX2IaICUXTG0WUHMXS2sXSGcWT3MaKjcpLTFVWFyFh4lTVllvcnWpqqwYOEwZM0QXTW4XTnAaJS8lKS3IycoYPlYaIyt4e36rra60tba5urutr7BQU1cAAAB8HBV3AAAAAnRSTlOR/KrCyFQAAAABYktHRDZHv4jRAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH5wEZCiUZVutNzgAAAGpJREFUCNdjYGBkggNGBmQeiM+EAjC5zCwsrGzsHJwQLhc3ExMPLxMfP5OAIBODkLCIqBi/uASHpJS0jCyDnLyCopIyh4qqmrqGphYDk5Q2WLGOrh63PsgoA0NDI2NDE1PsFqFw0RyJ6gUAuK4HVipJCoQAAAAuelRYdGRhdGU6Y3JlYXRlAAAImTMyMDLWNTDUNTINMTSwMja3MjLVNjCwMjAAAEFRBQlQZi6pAAAALnpUWHRkYXRlOm1vZGlmeQAACJkzMjAy1jUw1DUyDTE0sDI2tzIy1TYwsDIwAABBUQUJeVmGIQAAAABJRU5ErkJggg==
