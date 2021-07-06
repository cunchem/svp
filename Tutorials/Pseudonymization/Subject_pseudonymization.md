# Reidentification of pseudonymized data

[Pseudonymization](https://en.wikipedia.org/wiki/Pseudonymization)  is a technique that replaces personnal identifiers, such as a name or numerical identifiers, by an artificial identifier with no obvious link with the user. A common, but often inadequate,  practice is to generate pseudonyms by applying a one way function such as a cryptographic hash. 


Pseudonyms generated with this approach can often be re-identified: the original identifier can be recovered from the pseudonym. The two following exercises shows how pseudonyms derived through simple cryptographic hashing can be trivially recovered. 
  

## Reidentification of customer identifiers

In this exercise, we consider an hypothetical bank that derives  pseudonyms from the identifier of its customer. The `customer_id` is an integer encoded on five digits.

A file containing the pseudonyms of users who are endebted  has been leaked along with the script used to derive the pseudonyms,

* File containing the pseudonyms: [userid_hashed.txt](userid_hashed.txt)
* Script used to generate the pseudonyms: [pseudonymisation_userid.py](pseudonymisation_userid.py). 

The goal of this exercise is to perform a re-identification recovering the original identifiers from the pseudonyms.  A sketch of the reidentification process can be found in the file [reidentification_userid.py](reidentification_userid.py).

* Sketch of the reidentification script: [reidentification_userid.py](reidentification_userid.py)

Leveraging the content of [pseudonymisation_userid.py](pseudonymisation_userid.py), complete the script [reidentification_userid.py](reidentification_userid.py) and  re-identify the `customer_id` corresponding to the pseudonyms stored in the file [userid_hashed.txt](userid_hashed.txt). 


## Reidentification of social security numbers

In this exercise, we consider an hypothetical hospital that derives pseudonyms from the patient's social security number. The social security number (SSN) is a 15 digits identifier allocated to each person born in France and is is composed of the following items:

* gender (1: male, 2: female) 
* year / month of birth
* department / city of birth
* rank of birth in this location and period
* key acting as a checksum for verification

those items are organised as follow to create a SSN:

| A  | BB   | CC  | DD  |  EEE  | FFF | KK |
|---|---|---|---|---|---|---|
| Gender (1,2) | Year    | Month | Department |  City  | Rank | Key |

The key is the 97’s complement of the beginning of the identifier and can be derived by  computing the integer division by 97 of the number formed by the first 13 digits and then taking the remainder of this division and subtracting it from 97.

A file containing the pseudonyms of the patients suffering from a rare disease has been leaked as well as the script used for the generation of the pseudonyms. The following information is known about the patients: they are all born in Lyon, therefore the part of the SSN corresponding to department and city, DD EEE belongs to (69001 .. 69009). In general, the rank of birth, FFF, is smaller than 100.


* File containing the pseudonyms: [SSN_hashed.txt](SSN_hashed.txt)
* Script used to generate the pseudonyms: [pseudonymisation_SSN.py](pseudonymisation_SSN.py). 

The goal of this exercise is to perform a re-identification recovering the original SSN from the pseudonyms.  A sketch of the reidentification process can be found in the file [reidentification_SSN.py](reidentification_SSN.py).

* Sketch of the reidentification script: [reidentification_SSN.py](reidentification_SSN.py)


Leveraging the content of [pseudonymisation_SSN.py](pseudonymisation_SSN.py), complete the script  [reidentification_SSN.py](reidentification_SSN.py) and  re-identify the SSNs corresponding to the pseudonyms stored in the file [SSN_hashed.txt](SSN_hashed.txt). 

