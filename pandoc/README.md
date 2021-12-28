---
assignment: Template
unit: Pandoc
author: Omri Bornstein
email: omribor@gmail.com
orcid: 0000-0001-8645-6321
bibliography: bibliography.bib
date: 14/11/2021
csl: csl/apa.csl
monofont: Fira Code
link-citations: true
colorlinks: true
linkReferences: true
nameInLink: true
codeBlockCaptions: true
removeSectionNumbering: true
toc: true
geometry:
	- top=15mm
	- left=15mm
	- right=15mm
	- bottom=15mm
header-includes: |
	\usepackage{cancel}
	\usepackage{amssymb, amsmath, bm}
	\makeatletter\def\verbatim@nolig@list{}\makeatother
	\usepackage[utf8]{inputenc}
	\usepackage{menukeys}
---
# Source Code
* [@lst:go]:
```{#lst:go .go caption="A Go code block"}
import "fmt"

func main() {
	fmt.Println("Hello, word! -> => <= >= !=")
}
```
* [@lst:rust]
```{#lst:rust .rs caption="A Rust code block"}
fn main() {
	println!("Hello, word! -> => <= >= !=")
}
```

# Math Equations
$$x_{1, 2} = \frac{-b \pm \sqrt{b^2 -4ac}}{2a}$$

<!-- \newpage -->

## Diagrams
TikZ diagram:

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

