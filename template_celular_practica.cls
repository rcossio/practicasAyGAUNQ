\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{algebra_exercises}[2023/09/12 Algebra Exercises Class]

\LoadClass{article}


% Packages
\RequirePackage[paperheight=100cm,paperwidth=7.2cm,left=0.5cm,right=0.5cm,top=0.5cm,bottom=0.5cm]{geometry}
\RequirePackage[spanish]{babel}
\decimalpoint

\RequirePackage[colorlinks = true,
            linkcolor = blue,
            urlcolor  = blue,
            citecolor = blue,
            anchorcolor = blue]{hyperref}

\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{enumitem}
\RequirePackage{multicol}
\RequirePackage{graphicx}
\RequirePackage[autostyle]{csquotes}
\RequirePackage{xcolor}


% Settings
\pagestyle{empty} 
\renewcommand{\baselinestretch}{1.5} 

\setlist[enumerate,1]{wide, labelwidth=!, labelindent=0pt} 
\setlist[enumerate,2]{label=(\alph*)} % Second level of enumerate (a), (b), (c), ...

\MakeOuterQuote{"} % Makes " work as expected
\definecolor{darkblue}{RGB}{0,0,100}
\sloppy

% Command definitions

% Defines enumcols, which combines enumerato with multicols
\NewDocumentEnvironment{enumcols}{O{1}}
{
  \begin{enumerate}
}
{
  \end{enumerate} \vspace{24pt}
}

% Defines the header for the practice
\newcommand{\practiceheader}[2]{
    \noindent \hrulefill \\
    \vspace{-24pt}
    \begin{center}
        \textbf{#1} \\
        #2
    \end{center}
    \vspace{-10pt}
    \hrulefill
}

\newcommand{\Item}{\item[\stepcounter{enumii}$\blacktriangleright$\textbf{(\alph{enumii})}]} % Item with triangle
\newcommand{\answer}{\item[$\blacktriangleright$]} % Answer
\newcommand{\exercise}{\item} % Exercise
\newcommand{\SEL}[1]{\left\{\begin{matrix} #1 \end{matrix}\right.} % System of equations
\newcommand{\AMat}[2]{\left(\begin{array}{@{}*{#1}{c}|c@{}} #2 \end{array}\right)} % Augmented matrix
\newcommand{\Mat}[1]{\begin{pmatrix} #1 \end{pmatrix}} % Matrix
\newcommand{\Det}[1]{\begin{vmatrix} #1 \end{vmatrix}} % Determinant
\newcommand{\f}[2]{\frac{#1}{#2}} % Fraction
\newcommand{\conj}[1]{\overline{#1}} % Conjugate
\newcommand{\cis}[1]{\left[\cos\left({#1}\right)+i\sin\left({#1}\right)\right]} % cis form of complex number
\newcommand{\img}[2]{ \begin{minipage}[t]{\linewidth} \raisebox{-\height}{\includegraphics[width=#1]{#2}} \end{minipage} } % Include image in a minipage  
\newcommand{\vect}[1]{\overrightarrow{#1}} % Vector
\newcommand{\vers}[1]{\check{#1}} % Versor
\newcommand{\degs}{^{\circ}} % Degree symbol
\newcommand{\R}{\mathbb{R}} % Real numbers
\newcommand{\C}{\mathbb{C}} % Complex numbers
\newcommand{\x}{\hspace{-0.2mm}\times \hspace{-0.2mm}} % cartesian product
\newcommand{\Cmat}[2]{\mathbb{C}^{{#1} \x {#2}}} % Complex matrix
\newcommand{\Z}{\mathbb{Z}} % Integers
\newcommand{\Q}{\mathbb{Q}} % Rational numbers
\newcommand{\ivec}{\check{\imath}} % i versor
\newcommand{\jvec}{\check{\jmath}} % j versor
\newcommand{\kvec}{\check{k}} % k versor

\endinput
