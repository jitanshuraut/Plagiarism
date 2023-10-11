# Plagiarism Docs



### Project Name: Plagiarism
### Team Members 
```
Ankit Gondha (UI21CS10)
Jitanshu Raut (UI21CS10)
Deepak Dangi (UI21CS15)
```


### Title: Plagiarism Detection Project Workflow Diagram

#### Description:
```
The Plagiarism Detection Project Workflow Diagram illustrates the step-by-step process involved in the development and execution of a plagiarism detection system. This system combines various technologies and components to allow users to upload files, detect plagiarism, and manage user data securely. The workflow encompasses four main components: UI design in Figma, Front-end in React, Back-end in Flask.
```

### Workflow Steps:
```
1. UI Design in Figma:
   - The project begins with UI design in Figma, where designers create the user interface (UI) and user experience (UX) for the application.
   - UI designers collaborate to design visually appealing and user-friendly React pages that will be implemented later.

2. Front-end Development in React:
   - React developers take the UI/UX designs and convert them into functional web pages.
   - Key React pages include:
     - User Authentication Page: This page allows users to sign up, log in, and manage their accounts.
     - File System Page/ WorkSpace : Users can upload files to be checked for plagiarism on this page.

3. Back-end Development in Flask:
   - Flask developers create the server-side logic and functionality needed to handle user requests and file processing.
   - Key Flask functionalities include:
     - File Upload: Users can upload files, which are temporarily stored for analysis.
     - Clustering According to Plagiarism: The backend processes and clusters similar files based on plagiarism criteria.
     - Analyzing According to Plagiarism: Plagiarism detection algorithms are applied to analyze uploaded files for similarities.



```



Login Page
Sign Up page

### Research 


<img width="413" alt="Screenshot 2023-10-11 205426" src="https://github.com/jitanshuraut/Plagiarism/assets/96559286/7aebf176-ebc9-4e62-b999-e445ba4d2c0e">

<img width="487" alt="image" src="https://github.com/jitanshuraut/Plagiarism/assets/96559286/bf0ad451-4d66-43d9-81a3-c1a5a954a398">





## K grams:
```
{
Unigrams: [“c”, “a”, “t”, “a”, “s”, “t”, “r”, “o”, “p”, “h”, “i”, “c”]
Bigrams: [“ca”, “at”, “ta”, “as”, “st”, “tr”, “ro”, “op”, “ph”, “hi”, “ic”]
Trigrams: [“cat”, “ata”, “tas”, “ast”, “str”, “tro”, “rop”, “oph”, “phi”, “hic”]
}
```




MOSS 

The MOSS (Measure Of Software Similarity) algorithm, developed by Alex Aiken at Stanford University, is used for detecting software similarity and potential plagiarism in programming code. It employs a sophisticated approach to compare code submissions and identify similarities. Here's a more detailed explanation of the MOSS algorithm:

Submission Preprocessing:

Before comparing code submissions, MOSS preprocesses them to eliminate non-essential elements like comments, whitespace, and formatting differences.
The goal is to create a canonical representation of the code that focuses on its essential structure and logic.

Tokenization:
MOSS tokenizes the preprocessed code, breaking it down into individual tokens (e.g., keywords, identifiers, literals, operators).
Tokenization helps establish a basis for comparing the structure and content of code fragments.

Hashing:
Each token in the code is hashed using a hash function. This generates a numerical representation of the code based on its token sequence.
Hashing helps to efficiently identify matching tokens in different submissions.

Comparison Algorithms:
MOSS uses a combination of algorithms and heuristics to compare the hashed tokens in code submissions.
One common approach is to compare the tokens' hash values and their sequences to identify code fragments that are similar or identical.

Scoring and Ranking:
MOSS assigns similarity scores to pairs of submissions, indicating the degree of similarity.
The scores are computed based on factors such as the number of matching tokens, their order, and their frequency.
Higher scores suggest a higher likelihood of plagiarism or code sharing.

Threshold Setting:
Users (typically instructors or evaluators) can set a similarity threshold, above which pairs of submissions are considered suspicious.
Submissions with similarity scores above this threshold are flagged for further review.




Result Reporting:

MOSS generates a detailed report that includes information on pairs of submissions that exceeded the similarity threshold.
The report may provide links to view the matching code fragments side by side.
The highlighted code segments make it easier for users to identify similarities.
Manual Inspection:

Instructors or evaluators can manually review the flagged submissions to determine if they represent plagiarism or legitimate code sharing (e.g., due to the use of common libraries or collaboration).
Manual inspection is essential to ensure that the algorithm's findings are accurate


## Distance Algorithms:

### cosine similarity

Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space based on the cosine of the angle between them, resulting in a value between -1 and 1. The value -1 means that the vectors are opposite, 0 represents orthogonal vectors, and value 1 signifies similar vectors.

<img width="644" alt="image" src="https://github.com/jitanshuraut/Plagiarism/assets/96559286/d5fdc0d3-dbc1-490e-a706-21f3a47cc155">


### Jaccard distance

The Jaccard distance, which measures dissimilarity between sample sets, is complementary to the Jaccard coefficient and is obtained by subtracting the Jaccard coefficient from 1, or, equivalently, by dividing the difference of the sizes of the union and the intersection of two sets by the size of the union



<img width="604" alt="image" src="https://github.com/jitanshuraut/Plagiarism/assets/96559286/d8adf068-2064-4162-9dd7-4615c7efc1b2">



### overlap coefficient

The overlap coefficient,[1] or Szymkiewicz–Simpson coefficient, is a similarity measure that measures the overlap between two finite sets. It is related to the Jaccard index and is defined as the size of the intersection divided by the smaller of the size of the two sets:

<img width="586" alt="image" src="https://github.com/jitanshuraut/Plagiarism/assets/96559286/d544b600-57ea-4b06-8df7-a07ec4c1abc4">



### Sørensen–Dice

The index is known by several other names, especially Sørensen–Dice index,[3] Sørensen index and Dice's coefficient. Other variations include the "similarity coefficient" or "index", such as Dice similarity coefficient (DSC). Common alternate spellings for Sørensen are Sorenson, Soerenson and Sörenson, and all three can also be seen with the –sen ending.



<img width="569" alt="image" src="https://github.com/jitanshuraut/Plagiarism/assets/96559286/5c5354e5-85ec-4696-873f-9d638dae73d1">








## Source Code Algorithms:


## winnowing algorithm

### Introduction

Plagiarism detection involves identifying copied content and goes beyond just intact copies, including transformations, synonyms, and restatements without proper references.

PAN (Plagiarism Detection Author Identification Author Profiling) is an annual competition for plagiarism detection, author identification, and author profiling, founded by the EU digital library project.

Major bibliographic databases in China, such as CNKI, Wan Fang Data, and CQVIP, have developed their own plagiarism detection systems to prevent academic misconduct.

Plagiarism is a significant issue in the digital age, with a high percentage of college students admitting to using uncredited material from the internet.

Various forms of plagiarism have been increasing over recent decades.

Commercial plagiarism detection systems may not be cost-effective or suitable for lightweight, real-time, and normalization for students' assignments.

Researchers have explored different methods for plagiarism detection, such as transforming C source code to XML documents and using local word-frequency fingerprinting.

Some studies have compared plagiarism detection algorithms, with Winnowing being noted for its anti-interference ability for noise words.

The presented paper discusses an extension to the Winnowing fingerprint algorithm, preserving location and length information for text fragments, enhancing the algorithm's application and practicality.

The Winnowing fingerprint algorithm can be used to locate and mark plagiarism in source documents based on the extended information.

### Plagiarism detection 
Plagiarism detection methods can be categorized into three main types: grammar-based methods, semantic-based methods, and hybrid methods combining both.

Grammar-based methods focus on the grammatical structure of documents and use string matching techniques like LCS, Karp-Rabin string matching, and the MOSS text block fingerprint detection algorithm for efficient and precise detection of direct replication.


Semantic-based methods construct document feature vectors using term frequency or TF-IDF and measure document similarity using dot product or cosine of vector angle but may struggle to locate plagiarism.


Hybrid methods combine both semantic and grammatical approaches to achieve better results.

The Winnowing algorithm is a fingerprint-based text similarity detection method introduced by Schleimer et al in 2003, inspired by the Karp-Rabin algorithm.


Winnowing generates document fingerprints by selecting the minimum hash value in each window and then compares document fingerprints to identify copied text.



Winnowing is known for its lightweight and flexibility, making it robust for sentence and text block rearrangement and capable of reducing the influence of interference words through parameter settings.


Winnowing uses three parameters, t, k, and w, to control detection granularity and fingerprint density.


Parameter t is the guarantee threshold, ensuring that any substring match at least as long as t is detected.

The basic process of Winnowing fingerprint selection includes text preprocessing, k-gram segmentation, hash calculation, and window-based sampling of document hashes for selection.

These points provide an overview of plagiarism detection methods, with a focus on the Winnowing algorithm and its parameters.


### Extracting Fingerprints with Location Information



1. The first step in Winnowing involves removing irrelevant features from the source text, such as punctuation, spaces, control characters, and stop words.

2. Segi indicates the i-th k-gram text block, and its fingerprint is represented as hi = hash(segi).

3. During this process, the text length changes, and the location of segment hash is lost.

4. In the extended Winnowing method, preprocessing that may change text length is skipped, and text cleanup is done during the k-gram segment processing.

5. The ith k-gram text segment, segi, contains k useful characters, with meaningless characters removed. The length of the text segment in the original document is not less than k, i.e., leni ≥ k.

6. The extended fingerprint consists of triples, hi = {hash(segi), loci, leni}, where loci is the start location of the text segment segi in the original document, and leni is the source length of segi in the original document.

7. After obtaining the hash sequence of a document, the next step is to select "proper" hashes according to a specific rule to generate a new sequence of hashes representing the original document.

8. Algorithm 1 provides an extension method to calculate all the k-gram fingerprint sequences of a document.

9. Algorithm 2 describes the Winnowing process and the selection of fingerprint sequences.


### Algorithm 1:
```
1. Start
   - Initialize an empty list `H[]` to store k-gram hashes.

2. For Each k-gram in Text
   - Set `loc` to the current position (0 initially) and iterate through the text.

3. Extract k-gram
   - Extract a k-gram substring starting from position `loc` with a default length of `k`.
   - Assign this substring to the variable `kgram`.

4. Remove Stopwords
   - Remove characters from `kgram` that match the stopwords list.

5. Check k-gram Length
   - Check if the length of `kgram` is less than `k`.
   - If it is, enter a loop to extend the k-gram length to `k`.

6. Extend k-gram
   - Update the length (`len`) by adding the difference between `k` and the current length of `kgram`.
   - Extract a new k-gram substring with the updated length (`len`) starting from the same location (`loc`).
   - Remove stopwords from the newly extended `kgram`.

7. Calculate Hash
   - Calculate the hash of `kgram`.

8. Record k-gram
   - Create a triple `<hash(kgram), loc, len>` to represent the hash, location, and length of the k-gram.
   - Add this triple to the list `H[]` to record the hash along with its location and length.

9. Repeat
   - Repeat the process for all valid k-gram substrings in the text.

10. End
   - Once the loop is completed, return the list `H[]`, which contains all the k-gram hashes without Winnowing.

```


### Algorithm 2:
```
1. Start
   - Initialize variables:
     - `w` to `t + 1 - k` (scan window width)
     - `n` to the count of all hashes in `H[]`
     - `minIndex` to -1
     - `preMinIndex` to -1
     - `tmpMin`

2. Iterate Over Hashes
   - Begin a loop for `i` from 0 to `H[].count - w`.

3. Reset `tmpMin`
   - Set `tmpMin` to -1 at the start of each iteration.

4. Find Minimum Hash
   - Nested loop for `j` from `i` to `i + w`.
   - Check if `H[j].hash` is less than or equal to `tmpMin`.
   - If true, update `minIndex` to `j` (the rightmost one within the window) and set `tmpMin` to `H[j].hash`.

5. Check Duplicate Value
   - If `minIndex` is not equal to `preMinIndex`, proceed.
   - Add `H[minIndex]` to the `HS[]` list to record the sampled hash.

6. Update `preMinIndex`
   - Update `preMinIndex` with the value of `minIndex`.

7. Increment `i`
   - Increment `i` and repeat the process until the loop is completed.

8. End
   - Return the `HS[]` list, which contains the sampled hashes.


```













### SequenceMatcher

The basic idea is to find the longest contiguous matching subsequence (LCS) that contains no “junk” elements. This does not yield minimal edit sequences, but does tend to yield matches that “look right” to people.

we are trying to find something similar to LCS between a pair of sequence but they are not 100% mathematically elegant. In other words, the result should be more pleasing to the user, that’s why it has been termed as a match that “look right” to people.

<img width="296" alt="image" src="https://github.com/jitanshuraut/Plagiarism/assets/96559286/8163b271-ae05-4042-a648-76be6268dc73">

# Summary 



![Untitled (1)](https://github.com/jitanshuraut/Plagiarism/assets/96559286/6e14cc15-c3bb-4e51-a115-8170dba7fda2)

![Untitled (2)](https://github.com/jitanshuraut/Plagiarism/assets/96559286/2899fb6d-1cc0-4ca6-9696-48bf988c097f)




# API ENDPOINTS Details:

```
/ Folder / Source_Code / Winn
Input: 
{
  Examined_file = File Name1
  Reference_files =File Name2
}
Output:
{ 
  plagiarized_ratio:Int
}



/Folder/Source_Code/Seq
Input:
{
  Examined_file = File Name1
  Reference_files =File Name2
}
Output:
{
 plagiarized_ratio:Int
}

/Folder/BERT_TEST
Input:
{
Test:string
}
Output:
{
String : plagiarizedText
plagiarized_ratio:Int
}



/Folder/BERT/TRAIN
Input:
{
 Examined_file = [Name1,Name2,.....Namen]
}
Output:
{
String :”successfully Train”
}

/Folder/Distance
Input:
{
  Examined_file = [Name1,Name2,.....Namen]
  Reference_files =[Name1,Name2,.....Namen]
}
Output:
{
"input_sentence":String,
"reference_sentence":String,
"reference_document":String,
"similarity_score":Int,
"examined_file": String
}

```
















