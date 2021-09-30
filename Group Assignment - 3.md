# Group Assignment - 3

> Team : Kurkure

## Question 1

**Given : ** Consider $R(A_1,A_2,A_3,...,A_n)$ to be a relation with functional dependencies defined as
$$
A_{(i-1)i/2 + 1}A_{(i-1)i/2 + 2}...A_{(i-1)i/2 + i} \rightarrow A_{(i-1)i/2+i+1}...A_nA_1...A_i(i-1)/2
$$
For $i>3$ and till $\frac{(i-1)i}2+i = n$

### 1.1

The given condition $\frac{(i-1)i}2+i = n$ must be satisfied for some $i\in N$for the functional dependencies to be possible. Thus
$$
n = \frac{i(i+1)}2
$$

### 1.2

For some i,
$$
A_{\frac{i(i-1)}2+1}A_{\frac{i(i-1)}2+2}...A_{\frac{i(i-1)}2+i} \rightarrow A_{\frac{i(i-1)}2+i+1}A_{\frac{i(i-1)}2+i+2}...A_nA_1A_2...A_{\frac{i(i-1)}2}
$$
This can also be written as
$$
A_{\frac{i(i-1)}2+1}A_{\frac{i(i-1)}2+2}...A_{\frac{i(i-1)}2+i} \rightarrow A_{\frac{i(i-1)}2+i+1}A_{\frac{i(i-1)}2+i+2}...A_nA_1A_2...A_{\frac{i(i-1)}2}A_{\frac{i(i-1)}2+1}A_{\frac{i(i-1)}2+2}...A_{\frac{i(i-1)}2+i}\\
\implies A_{\frac{i(i-1)}2+1}A_{\frac{i(i-1)}2+2}...A_{\frac{i(i-1)}2+i} \rightarrow A_i \forall i\\
\implies A_{\frac{i(i-1)}2+1}A_{\frac{i(i-1)}2+2}...A_{\frac{i(i-1)}2+i} \text{ is a key }\forall i
$$
Thus the number of keys equals i for which $\frac{(i-1)i}2 = n$, that is
$$
i = \frac{-1+\sqrt{1+8n}}2
$$

### 1.3

1. No information is provided on the atomicity of the attributes, we assume all the attributes are atomic and thus the relation is in the First Normal Form

2. From the functional dependencies given we can conclude

   1. Every attribute is a prime attribute, that is each attribute $A_x$ belongs to a key. This can clearly be seen as $\frac{i(i-1)}2+1 \leq x \leq \frac{i(i-1)}2+i$ for some $i$.
   2. Also each attribute $A_x$ belongs to exactly one key as each of the sets $[\frac{i(i-1)}2+1,\frac{i(i-1)}2+i]$ are disjoint

   From the above to conclusion we can further conclude that any of the functional dependencies above no longer hold if one of the attributes is removed. Thus the relation R is in the Second Normal Form.

3. Since every attribute in R is a prime attribute, the relation is in Third Normal Form

4. For every $X \rightarrow Y$, $X$ is a key. Thus the relation R is in Boyce-Codd Normal Form

### 1.4

The given set of functional dependencies can be broken down into
$$
\begin{equation}\begin{split}F\ &=\{A_1\rightarrow A_2, A_1\rightarrow A_3,...,A_1\rightarrow A_n,\\
&A_2A_3 \rightarrow A_1, A_2A_3 \rightarrow A_4, ..., A_2A_3 \rightarrow A_n,\\
&...,\\
&A_{\frac{i(i-1)}2+1}A_{\frac{i(i-1)}2+2}...A_{\frac{i(i-1)}+i} \rightarrow A_1,...,A_{\frac{i(i-1)}2+1}A_{\frac{i(i-1)}2+2}...A_{\frac{i(i-1)}+i} \rightarrow A_n
\}\end{split}\end{equation}
$$
This set consists of (n-1)i dependencies many of which are clearly redundant such as $A_1 \rightarrow A_2A_3\ \&\ A_2A_3 \rightarrow A_4 \implies A_1 \rightarrow A_4$ which is already a part of the set.

Consider the set of functional dependencies G such that
$$
\begin{equation}\begin{split}
G &= \{
A_1\rightarrow A_2, A_1\rightarrow A_3,...,A_1\rightarrow A_n\\
&A_2A_3 \rightarrow A_1,\\
&...,\\
&A_{\frac{i(i-1)}2+1}A_{\frac{i(i-1)}2+2}...A_{\frac{i(i-1)}+i} \rightarrow A_1
\}
\end{split}\end{equation}
$$
This set of functional dependencies has $n+i-2$ dependencies. Also $G = G^+ = F^+$ thus the number of dependencies in G cannot be reduced. Also for every $X \rightarrow Y$, $X$ has the minimum number of attributes, thus G is the minimal cover of F. 

Since $G \sube F$, All our conclusion from $F$ still hold, thus G is in Boyce-Codd Normal Form.