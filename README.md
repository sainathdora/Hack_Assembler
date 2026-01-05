<h1>Hack Assembler</h1>

<p>
This project is an implementation of an <strong>Assembler for the Hack computer</strong>,
as defined in the <em>Nand2Tetris</em> Book.
The assembler translates Hack assembly language (<code>.asm</code>) programs
into Hack machine language (<code>.hack</code>) binary instructions.
</p>

<hr>

<h2>Overview</h2>

<p>
The Hack Assembler takes a human-readable assembly program and converts it into
a binary format executable by the Hack CPU.
This project closely follows the official Hack specification and implements
the complete two-pass assembly process required for symbol resolution.
</p>

<p>
The assembler supports:
</p>

<ul>
  <li>A-instructions (<code>@value</code>, <code>@symbol</code>)</li>
  <li>C-instructions (<code>dest=comp;jump</code>)</li>
  <li>Label declarations (<code>(LABEL)</code>)</li>
  <li>Predefined, user-defined, and variable symbols</li>
</ul>

<hr>

<h2>Architecture</h2>

<h3>1. Preprocessing</h3>
<ul>
  <li>Removes whitespace and comments</li>
  <li>Normalizes input for easier parsing</li>
</ul>

<h3>2. First Pass (Symbol Table Construction)</h3>
<ul>
  <li>Scans the program for label declarations</li>
  <li>Maps labels to instruction addresses</li>
  <li>Does not generate machine code in this pass</li>
</ul>

<h3>3. Second Pass (Code Generation)</h3>
<ul>
  <li>Resolves symbols and variables</li>
  <li>Allocates memory for variables starting at address 16</li>
  <li>Translates A- and C-instructions into 16-bit binary code</li>
</ul>

<hr>

<h2>Instruction Translation</h2>

<h3>A-instructions</h3>
<p>
Translated into:
</p>
<pre>
0vvvvvvvvvvvvvvv
</pre>
<p>
where <code>v</code> represents a 15-bit address or value.
</p>

<h3>C-instructions</h3>
<p>
Translated into:
</p>
<pre>
111 a cccc cc ddd jjj
</pre>
<p>
according to the Hack specification for <code>comp</code>, <code>dest</code>, and <code>jump</code> fields.
</p>

<hr>

<h2>Symbol Table</h2>

<p>
The assembler supports:
</p>

<ul>
  <li>Predefined symbols (<code>R0</code>–<code>R15</code>, <code>SP</code>, <code>LCL</code>, <code>ARG</code>, <code>THIS</code>, <code>THAT</code>, <code>SCREEN</code>, <code>KBD</code>)</li>
  <li>Label symbols defined using <code>(LABEL)</code></li>
  <li>Variables allocated dynamically during the second pass</li>
</ul>

<hr>

<h2>Input and Output</h2>

<h3>Input</h3>
<ul>
  <li>Hack assembly file (<code>.asm</code>)</li>
</ul>

<h3>Output</h3>
<ul>
  <li>Binary machine code file (<code>.hack</code>)</li>
  <li>Each line contains one 16-bit instruction</li>
</ul>

<hr>

<h2>How to Run</h2>

<ol>
  <li>
    <strong>Clone the repository</strong> into a directory of your choice
    (for example <code>/foo</code>):
    <pre>
git clone &lt;repository-url&gt;
    </pre>
  </li>

  <li>
    <strong>Create a Hack assembly file</strong> (e.g. <code>dummy.asm</code>)
    and write your Hack assembly code into it.
  </li>

  <li>
    <strong>Specify the input file</strong> in <code>main.py</code> by assigning
    the filename (without extension) to the <code>fn</code> variable:
    <pre>
fn = "dummy"
    </pre>
  </li>

  <li>
    <strong>Run the assembler</strong>:
    <pre>
python main.py
    </pre>
  </li>

  <li>
    <strong>Output</strong>:  
    A corresponding <code>.hack</code> file will be generated in the same directory.
    For example:
    <pre>
dummy.hack
    </pre>
  </li>
</ol>
