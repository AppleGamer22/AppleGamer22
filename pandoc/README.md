---
assignment: Template
unit: Pandoc
author: Omri Bornstein
email: omribor@gmail.com
orcid: 0000-0001-8645-6321
bibliography: bibliography.bib
date: 14/11/2021
csl: csl/apa.csl
link-citations: true
colorlinks: true
linkReferences: true
nameInLink: true
codeBlockCaptions: true
removeSectionNumbering: true
toc: true
---
# Source Code
Paragraphs have a single line break between them.

You can include source code.

* A [Go](https://go.dev) code block:
```go
import "fmt"

// the main function
func main() {
	fmt.Println("Hello, word! -> => <= >= !=")
}
```

# Math Equations
$$x_{1, 2} = \frac{-b \pm \sqrt{b^2 -4ac}}{2a}$$

$$
\left[\begin{array}{cc|c}
	1 & 2 & 3 \\
	4 & 5 & 6 \\
	\cancel{7} & 8 & 9
\end{array}\right]
$$

$$
y = \begin{cases}
	x + 3 & \text{if } x \geq 20 \\
	\frac{\sin^2\left(\sqrt[43]{e^x + \cos(x)}\right)}{\ln(x - 3)} & \text{if } x \neq 90
\end{cases}
$$

# Lists
1. First
	1. nested first
		1. nested second
			1. forth
1. Second

#. First
	#. nested first
		#. nested second
			#. forth
#. Second

* first
	* second
		* third
			* forth

## Diagrams
* A TikZ diagram:

```{.tikz caption="Finite Automaton that accepts only those words that **do not** end in $ba$"}
\usetikzlibrary{automata,graphdrawing,graphdrawing.trees,graphs,positioning,arrows}
\tikzset{->,>=stealth,node distance=2.5cm,every state/.style={thick, fill=gray!10},initial text=$ $}
\begin{tikzpicture}
	\node[state, initial, accepting] (q1) {1};
	\node[state, accepting, right of=q1] (q2) {2};
	\node[state, right of=q2] (q3) {3};

	\draw (q1) edge[above] node{b} (q2);
	\draw (q2) edge[above] node{a} (q3);
	\draw (q1) edge[loop below] node{a} (q1);
	\draw (q2) edge[loop below] node{b} (q2);
	\draw (q3) edge[bend left, below] node{b} (q2);
	\draw (q3) edge[bend right, below] node{a} (q1);
\end{tikzpicture}
```

* A Karnaugh map:
```{.tikz caption="A Karnaugh map" additionalPackages="\usepackage{kvmap}"}
\begin{kvmap}
	\begin{kvmatrix}{a,b,c,d}
		0 & 1 & 1 & 0 \\
		1 & 0 & 0 & 1 \\
		0 & 0 & 0 & 1 \\
		0 & 1 & 1 & 1 \\
	\end{kvmatrix}
	\bundle{3}{3}{2}{3}
	\bundle[color=blue]{3}{2}{3}{1}
	\bundle[invert=true,reducespace=2pt,overlapmargins=6pt]{1}{0}{2}{3}
	\bundle[invert=true,reducespace=2pt]{0}{1}{3}{1}
\end{kvmap}
```
<!-- 
```mermaid
sequenceDiagram
	participant dotcom
	participant iframe
	participant viewscreen
	dotcom->>iframe: loads html w/ iframe url
	iframe->>viewscreen: request template
	viewscreen->>iframe: html & javascript
	iframe->>dotcom: iframe ready
	dotcom->>iframe: set mermaid data on iframe
	iframe->>iframe: render mermaid
``` -->
