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

## Question 2

### 2.1 

Given
$$
A_i \implies A_j \forall 1\le i \lt j\le n - (i)
\\A_i \implies A_j \forall 1\le i \gt j\le n - (ii)
$$
We can rearrange $(ii)$  to imply that 
$$
A_i \implies A_j \forall 1\le j \lt i\lt n
$$
Using this we can conclude that $A_i \implies A_j \forall 1\le i,j\le n$,  thus implying that every $A_i : 1\le i \le n$ is  a key.

 

### 2.2

1^st^ normal form :

To satisfy the 1st normal form every attribute should be a atomic value (i.e not multivalued attribute or composite attribute), clearly we don't have enough information to determine if the attributes are multivalued or not, so we can't conclude.

2^nd^ normal form :

Clearly since every attribute is a key thus every attribute is a prime attribute thus the relationship satisfies the second normal form requirement. 

3rd normal form :

A relationship is said to be in 3rd normal form if it satisfies the following conditions for every functional dependency $X \implies Y$

1. X is a super key 
2. Y is a prime attribute.

Clearly since every attribute is a primary key, thus for any functional dependency  $X \implies Y$ , X and Y will both be a super key (since every attribute is a key, thus every attribute which are present in X or Y are keys thus X will be super key and Y will be a prime attribute), thus this relationship is in 3rd normal form.

BCNF :

To satisfy BCNF for every non trivial functional dependency in the relationship $X\implies A$ , X must be a super-key of the relation, since every attribute is a key therefore for every relationship  $X\implies A$, ( X will be a super-key since every attribute that is a component of it is a key), therefore the relation is a BCNF.



### 2.3

Minimum cover requires:

1. Every functional dependency to have a single attribute in the RHS

2. Removal of all the redundant functional dependencies, which are of the form $X \implies Y$ with the following condition: 

      The set of dependencies F = the set of dependencies $(F- (X \implies Y))$

A set of cyclic dependencies can satisfy all the conditions. Therefore, cyclic dependencies will be a minimal cover for the above relation. 

​	One possible minimal cover would look like $A_1 \implies A_2,\space A_2 \implies A_3 \dots A_{n-1} \implies A_n,\space  A_n \implies A_1$.  Since we have n attributes, we can generate $(n-1)!$ such cyclic permutations. 
