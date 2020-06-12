(* ::Package:: *)

(* ::Subsubsection:: *)
(*Introduction*)


(* ::Text:: *)
(*Suppose a cutset of size S splits K(n, r) into c components.*)
(*a is a lower bound on how many of those c components are singletons.*)
(*S, if not specified, will be its upper bound \[LeftCeiling](n/r-1)c\[RightCeiling]-1.*)


a[n_,r_,c_,S_]:=With[{d=Binomial[n-r,r]},Ceiling[(2d-2)/(d-2) c-d/(d-2) S]];
a[n_,r_,c_]:=a[n,r,c,Ceiling[(n/r-1)c]-1]


(* ::Text:: *)
(*Upper bound of the number of edges from cutset S to the remaining c-a components.*)


u[n_,r_,c_,S_]:=Binomial[n-r,r]S-Binomial[n-r,r]a[n,r,c,S];
u[n_,r_,c_]:=u[n,r,c,Ceiling[(n/r-1)c]-1]


(* ::Text:: *)
(*f is a lower bound on the number of edges from a single component to S.*)
(*Semi-quadratic function from the Laplacian bound.*)


f[10,4,1]=15;
f[10,4,2]=28;
f[10,4,3]=41;
f[10,4,4]=52;
f[10,4,t_]:=f[10,4,t]=Ceiling[(9t(210-t))/210];


f[9,4,1]=5;
f[9,4,2]=8;
f[9,4,3]=11;
f[9,4,4]=14;
f[9,4,5]=17;
f[9,4,6]=18;
f[9,4,7]=21;
f[9,4,8]=22;
f[9,4,t_]:=f[9,4,t]=Ceiling[(2t(126-t))/126];


f[7,3,1]=4;
f[7,3,2]=6;
f[7,3,3]=8;
f[7,3,4]=10;
f[7,3,5]=12;
f[7,3,6]=12;
f[7,3,t_]:=f[7,3,t]=Ceiling[(2t(35-t))/35];


(* ::Text:: *)
(*p is list of m partitions of the remaining vertices into the c-a components which minimize the number of edges to S.*)
(*If m is not specified, p returns all partitions that do not exceed the upper bound.*)
(*l is lower bound of the number of edges from the c-a components to S.*)


p[n_,r_,c_,S_,m_]:=With[{l=IntegerPartitions[Binomial[n,r]-S-a[n,r,c,S],{c-a[n,r,c,S]}]},MinimalBy[l,Total[f[n,r,#]&/@#]&,m]];
p[n_,r_,c_,S_]:=With[{l=IntegerPartitions[Binomial[n,r]-S-a[n,r,c,S],{c-a[n,r,c,S]}]},Select[l,Total[f[n,r,#]&/@#]<=u[n,r,c,S]&]];
p[n_,r_,c_]:=p[n,r,c,Ceiling[(n/r-1)c]-1];


l[n_,r_,c_,S_]:=l[n,r,c,S]=Total[f[n,r,#]&/@First[p[n,r,c,S,1]]];
l[n_,r_,c_]:=l[n,r,c]=l[n,r,c,Ceiling[(n/r-1)c]-1]


(* ::Subsubsection:: *)
(*Testing*)


(* ::Text:: *)
(*Example: c=40 for K(9, 4).*)


(* ::Input:: *)
(*l[9,4,40]*)


(* ::Text:: *)
(*Does lower bound exceed upper bound (contradiction)?*)


(* ::Input:: *)
(*l[9,4,40]>u[9,4,40]*)


(* ::Text:: *)
(*From spectral bounds, we only need to test 49<=c<=76 for K(10, 4).*)
(*Works for c<=56:*)


(* ::Input:: *)
(*g[c_]:=l[10,4,c]-u[10,4,c]*)


(* ::Input:: *)
(*g/@Range[49,57]*)


(* ::Text:: *)
(*From spectral bounds, we only need to test 8<=c<=53 for K(10, 4).*)
(*Works for c<=40:*)


(* ::Input:: *)
(*g[c_]:=l[9,4,c]-u[9,4,c]*)


(* ::Input:: *)
(*g/@Range[8,53]*)


(* ::Text:: *)
(*For c>=41, what values of S will yield a contradiction?*)
(*Note c+1 <= S < (n/r-1)c.*)


(* ::Input:: *)
(*g[c_]:=Select[Range[c+1,Ceiling[(9/4-1)c]-1],l[9,4,c,#]>u[9,4,c,#]&]*)
(*g/@Range[41,53]*)


(* ::Text:: *)
(*Similarly try for K(10, 4).*)
(*Runs slowly, so use binary search.*)
(*Returns the first S for which we cannot get a contradiction.*)


(* ::Input:: *)
(*g[c_]:=Block[{lo=c+1,hi=Ceiling[(10/4-1)c],m=0},While[lo<hi,m=Floor[(lo+hi)/2];If[l[10,4,c,m]>u[10,4,c,m],lo=m+1,hi=m]];lo]*)
(*g[57]*)


(* ::Input:: *)
(*l[10,4,57,84]>u[10,4,57,84]*)


(* ::Input:: *)
(*l[10,4,57,83]>u[10,4,57,83]*)


(* ::Text:: *)
(*K(7, 3)*)


(* ::Input:: *)
(*g[c_]:=l[7,3,c]-u[7,3,c]*)


(* ::Input:: *)
(*g/@Range[5,13]*)


(* ::Input:: *)
(*g[c_]:=Select[Range[c+1,Ceiling[(7/3-1)c]-1],l[7,3,c,#]>u[7,3,c,#]&]*)


(* ::Input:: *)
(*g[11]*)


(* ::Input:: *)
(*g[12]*)


(* ::Input:: *)
(*g[13]*)


(* ::Text:: *)
(*LaTeX*)


(* ::Input:: *)
(*Import["https://raw.githubusercontent.com/jkuczm/MathematicaCellsToTeX/master/NoInstall.m"]*)


(* ::Input:: *)
(*Cells[][[3]]//NotebookRead*)


(* ::Input:: *)
(*CellToTeX[NotebookRead[Cells[][[13]]]]*)


(* ::Text:: *)
(*Rule out more partitions for K(9, 4) with Ramsey.*)


(* ::Input:: *)
(*p[9,4,41]*)


(* ::Input:: *)
(*ind[n_]:=ind[n]=LengthWhile[{0,3,9,13,17,21,25,29,36},#<=n&]*)


(* ::Input:: *)
(*indtot[partition_]:=Total[ind/@partition]*)


(* ::Input:: *)
(*Table[Select[p[9,4,c],indtot[#]+a[9,4,c]>56&],{c,41,53}]*)
