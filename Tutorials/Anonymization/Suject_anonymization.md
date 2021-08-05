# Dataset anonymization 

We consider a dataset containing  socio-economical information on a set of individuals. This dataset does not contain any identifier that could be used to identify the corresponding individuals, but we will show that the data can be used to single-out many individuals which could be lead to their re-identification. We will then see how this risk of re-identification can be reduced by applying some transformation to the dataset. 

## The adult dataset

The dataset considered here is the [UCI adult dataset](https://archive.ics.uci.edu/ml/datasets/Adult) which contains the records of 48842 individuals and is composed of 14 attributes including age, workclass, race, sex, native-country, etc. . This dataset includes information about real individuals as it has been extracted from the 1994 USA census database. It is often used to evaluate methods for predicting personal attributes such as the salary.



## Anonymity sets


To analyse the threat of singling-out users in the dataset we will compute (and display) anonymity sets. As a reminder, an anonymity set can be defined as "*A set of individuals that have the same attributes, making them indistinguishable from each other from the perspective of a particular attacker or observer*". 


Let us illustrate that through an example. For the sake of simplicity we assume that the dataset is reduced to four attributes (age, sex, country of origin, race ). If we consider the three first attibutes,  we may find anonymity sets such as:

* a first anonymity set composed of three individuals

| age  | sex  | country of origin  | race |
|---|---|---|---|
|  39 |  Male |  United-States | Black |
|  39 |  Male |  United-States | White |
|  39 |  Male |  United-States | White |

* and a second anonymity set composed of a single individual

| age  | sex  | country of origin  | race |
|---|---|---|---|
|  39 |  Male |  France | Black |

In the second case, the individual can be singled-out based on the three attributes age, sex, country of origin. In this case, we say that {age,sex,country or origin} is a quasi-identifier for this individual. 

Within a dataset, each individual will fall in one anonymity set. The  size of anonymity sets can range from 1 individual (an individual that can be uniquely identified by its attributes) up to the size of the dataset (all the individuals share the same attributes and cannot be distinguished). As we will see with the *adult* dataset, a dataset contains anonymity sets of various sizes. 



### Computing and displaying anonymity sets 

To compute and display the anonimity sets, we will use  [kmap](https://github.com/gaborgulyas/kmap), a tool developped by Gabor Gulyas. Given a set of attirbutes, kmap can computes the anonymity sets and can generate a plot to dsiplay them. 

The plot presenting anonymity sets of a dataset includes several elements :

* Each point represents an anonymity set or a group of anonymity set of the same size. The larger the point, the more anonymity sets in this group.
* The x-axis represents the size of the anonymity set 
* The y-axis represents the number of anonymity 

The following plot has been produced by kmap using the *adult* dataset and by selecting the attributes {age, sex, country of origin}. The size of the anonymity set ranges from 1 (top left) to several hundreds (bottom right). The top-left point of coordinates (1,10^3) means that there are 1000 anonymity sets of size 1.

![](Figures/kmap_attrnum_3_annot.png "Anonymity sets for Size Anonymity sets for the attributes {age, sex, country of origin}" )

* Download *kmap* from its repository [here](https://github.com/gaborgulyas/kmap)
* Download the *adult* dataset from [here](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data)
* Test *kmap* by generating the defaults plots: `convert_to_pickle.py` then `make_plots.py`
* Plot anonymity sets for other attributes (ex: {age, sex, country of origin, race} and {age, sex}). What is the impact of the number of attributes on the anonymity sets ?
* Assuming that you have access to a second dataset  containing the attributes  {full name, age, sex, country of origin} for the same population; what kind of information would you be able to infer and on whom ?
* As individuals in anonymity set of size 1 can be uniquely identified, the remaining attributes (ex: marital-status, capital-gain/loss) can be trivially infered. Can similar information be inferred for users that are not in  anonynity sets of size 1 ?

## Anonymizing the dataset: toward k-anonymity

As seen in the previous examples, some individuals can be uniquely identified by a small set of attributes (anonymity sets of size 1). Other individuals can be in small anonymity sets which can also be problematic from a privacy point of view. 

To remedy this situation, we want to anonymize this dataset. The first approach we will consider is the *generalization* of the attributes, and in a second time we will consider adding noise to numerical attributes.

### Generalizing the attributes *age* and *country of origin*

We want to anonymize the dataset using generalization and more specifically full domain *generalization* (see lecture slides). Our objective is to try to enforce *k-anonymity* on this dataset: ensure that all attributes are in anonymity sets of size at least *k*. The value of *k* will give an indication on the level of protection. In a first time we will try to achive 2-anonymity. 

We will focus on two attributes:  *age* which is a numerical value that we can easily generalize by rounding (for instance to the next multiple of 10) and *country of origin* that can be generalize to the continent level.

* Complete the script `generalize.py` to generalize the attribute age and country of origin in the file `adult.data`
* Plot the new anonymity sets (after having converted the new dataset to pickle)
* What was the impact of this transformation on the anonymity sets ?
* Apply each of the generalization independantly (only age generalized then only country of origin generalized). 
* What is the impact of those transformation on the *utility* of the dataset ?
* Which of the attribute appear to have the most impact on the anonymity sets ?
* After the generalization of both age and country of origin, is our dataset satisfying 2-anonymity ?
* What other modification can be done to satisfy 2-anonymity ?


### Perturbation: adding noise to numerical attributes
 
Another anonymization approach is to add noise to numerical attributes. For instance, the attribute *age* can be perturbed by adding a random value uniformly distributed over [-d,+d] (d=2)

* Write a script that implement this perturbation and apply it to the dataset `adult.data`
* Plot the new anonymity sets (after having converted the new dataset to pickle)
* What is the impact of the anonymity set ?
* How does this technique compare with the generalization of the attribute age (rounding to next multiple of 10) in term of privacy ? What about the impact in term of utility ?
