---
title: 'Infrastructure for Synthetic Health Data'
title_short: 'Synthetic Health Data'
tags:
  - Health data
  - Synthetic data
  - Workflows
  - FAIR
authors:
  - name: Núria Queralt-Rosinach
    orcid: 0000-0003-0169-8159
    affiliation: 1
  - name: Muhammad Shoaib
    orcid: 0000-0002-4854-4635
    affiliation: 2
affiliations:
  - name: Human Genetics, Leiden University Medical Center, Leiden, Netherlands
    index: 1
  - name: Luxembourg Center for Systems Biomedicine, University of Luxembourg, Luxembourg
    index: 2
date: 11 November 2022
cito-bibliography: paper.bib
event: BioHackEU22
biohackathon_name: "BioHackathon-Europe"
biohackathon_url:   "https://biohackathon-europe.org/"
biohackathon_location: "Paris, France, 2022"
group: Project 15
# URL to project git repo --- should contain paper.md
git_url: https://github.com/NuriaQueralt/synthetic-health-data-generator/bhxiv
# This is the short authors description that is used at the
# bottom of the generated paper.
authors_short: Núria Queralt-Rosinach \emph{et al.}
---
<!--

The paper.md, bibtex and figure file can be found in this repo:

  https://github.com/journal-of-research-objects/Example-BioHackrXiv-Paper

To modify, please clone the repo. You can generate PDF of the paper by
pasting above link (or yours) in

  http://biohackrxiv.genenetwork.org/

-->

# Introduction
Machine Learning (ML) methods are becoming ever more prevalent across all domains in Life Sciences. However, a key component of effective ML is the availability of large datasets that are diverse and representative. In the context of health systems, with significant heterogeneity of clinical phenotypes and diversity of healthcare systems, there exists a necessity to develop and refine unbiased and fair ML models. Synthetic data are increasingly being used to protect the patient’s right to privacy and overcome the paucity of annotated open-access medical data. Synthetic data and generative models can address these challenges while advancing the use of ML in healthcare and research.

Following up the efforts currently undertaken in the ELIXIR Health Data and the Machine Learning Focus Groups around the synthetic health data landscape, this project will focus on the health data providers' need for a ready-to-use synthetic data platform which is assessed by health data experts, researchers, and ML specialists. Aligned to ELIXIR Health Data Focus Group’s objectives, we aim at building an infrastructure for synthetic health data offering a dockerized synthetic data generator based on the open-source libraries Synthetic Data Vault (SDV) (github.com/sdv-dev) and ydata-synthetic (github.com/ydataai) with state of the art ML methods. This will enable users to generate synthetic data that has the same structure and statistical properties as the original dataset from a variety of data types (clinical, variational or omics). Despite the capacity to generate their own datasets, a set of exemplary datasets will be publicly available in appropriate repositories and will include rich metadata descriptions according to the DOME recommendations (https://dome-ml.org/) and GA4GH (ga4gh.org) standards. OpenEBench (openebench.bsc.es) will host a community of practice for comparing different approaches for synthetic data generation. Here, we present our prototype for the generation of synthetic health data and our proposed FAIR implementation of the generated synthetic datasets developed after one week of BioHacking together 20 participants (10 new to the project), from different countries (NL, ES, LU, UK, GR, FL, DE).

<!--
# Results
-->

## Infrastructure for Synthetic Health Data
For stress and test development of new ML code, we need suitable data to properly demonstrate the tools application. However, ML developers without data access are not able to see how the tool performs for its intended application. One way to enable this is to generate _synthetic data_, where new "fake" data is generated from real data using a specifically designed model. Importantly, the generation model must maintain the original features and structure to be as realistic as possible to the original data. In particular, synthetic data goals are to ensure:

1. applicability: the synthetic data must fit for its intended application.
2. quality: it must be a sufficient and necessary representation of the real data.
3. privacy: it must not expose any sensitive private information from the real data, e.g. we must prevent that a generated synthetic patient is actually real.

Our main goal was to provide to the health community and life sciences researchers with a simple and reusable way of generating privacy-preserving and effective synthetic data to be used in artificial intelligence technologies and ML methods to speed up research on health data. Next, we present the workflows we developed to generate synthetic health data, how the data could be evaluated, the user interfaces to interact with the whole process, and how to make the synthetic datasets FAIR for others to reuse.


### Synthetic Data Generation workflows
To develop an infrastructure for generating synthetic health data that is easy to use, we first explored how to generate synthetic health data from real data. There are many existing methods to generate synthetic data. The first challenge is that these methods are usually tailored for a specific type and format of the input dataset. The second challenge is to evaluate the quality of the generated synthetic dataset to know whether the model and the data are actually useful.

We first defined an input data type which was _tabular data_ for its simplicity. Then, we chose a starting dataset that was already published in the public domain. We selected the [Breast Cancer Wisconsin (Diagnostic) Data set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data) published in the Kaggle website rated with a usability of $8.53$. This dataset contains 32 columns including 2 attributes (identifier _ID_ (integer) and _Diagnosis_ (M=malignant, B=benign)) and 10 real-valued features computed for each cell nucleus from a digitized image of a breast mass in addition of three statistical parameters for each feature (_Mean_, _standard error_ and _worst_). They describe characteristics of the cell nuclei present in the image [@bennett1992]. This dataset is similar to those for clinical research making it suitable to produce synthetic data for health.

We experimented with three synthetic data generators: SDV, DataSynthesizer and Synthea.  

## Synthetic Data Vault (SDV)
[@Patki_2016_SDV] presented a framework known as Synthetic Data Vault (SDV) that was intended to generate synthetic relational data. Such a framework combines both statistical approaches and deep learning method to accommodate the synthetization. The authors of this framework were taking into the account the generation of synthetic data that is statistically similar to the original one even in terms of missing values, categorical and datetime distribution. Meanwhile, the authors have focused on increasing the privacy by enabling the user to adjust the model’s parameters in order to add different noisiness.

Within the statistical part, the SDV framework utilized different versions of multivariate Copula Gaussian distribution (e.g. uniform, truncated gaussian, gamma, beta, etc.). In this regard, two main aspects have been considered including distribution and covariance where the first refers to the distributional probability of the values within each attribute while the latter refers to the impact of each value within an attribute in accordance with the values within other attributes. In addition, SDV framework has utilized an approach called Conditional Parameter Aggregation (CPA) to mimic the relationships between tables during the generation of a relational database in which the user could provide metadata about the tables. Furthermore, SDV framework provides two paradigms of synthetic generation through mode-based which aims at generating synthetic data based on an existing model, and knowledge-based which aims at expanding an existing data by generating more examples. 

On the other hand, SDV framework also utilizes a deep learning architecture known as Generative Adversarial Network (GAN). This architecture is based on Deep Neural Network which consists of two main components; generator and discriminator where the first refers to the model that is trained to generate new data while the latter refers to the model that is trained to classify the data into real or synthetic [@Wang_2017_Generative]. 


### Quality assessment
## SDV Parameter Comparison
As mentioned earlier, SDV contains a wide range of parameters during the generation of synthetic data. These parameters are either referring to the desired statistical distribution through different Copula Gaussian or even using the deep learning of GAN which called CTGAN. Using the Breast Cancer dataset, a comparison between these parameters have been conducted in which the dataset was synthesized multiple times using one of these parameters. To evaluate this comparison, a metric score within SDV has been used which compare the synthetic data with the original one. Figure 1 shows such a comparison.

https://github.com/LBolzani/synthetic-health-data-generator/blob/main/images/SDV%20Model%20Comparison.png
Figure 1. SDV model comparison

As shown in Figure 1, the most accurate generation for the Breast Cancer dataset was depicted by GaussianCopula through Kernel Density Estimation (KDE) which has the highest evaluation score of 0.96. Note that, this means that this distribution significantly suits the Breast Cancer dataset. 

## SDV Utility Classification Assessment
As an additional aspect of evaluation, investigating the classification performance of the synthetic data alongside the original one would provide a significant insight on how the synthetic data could be used for further downstream analysis. To this end, the synthetic data generated by the best SDV model parameter of GaussianCopula-KDE has been used. In order to provide a consistent evaluation on such a classification task, a classifier of Random Forest (RF) has been used with 10 cross-fold validation for both datasets (i.e., real and synthetic). In addition, different parameters of RF have been also considered within the classification including the criterion (i.e., gini or entropy) and max-features (i.e., auto, sqrt, log2). Both datasets will be divided into training and testing and classified using each RF parameter through the use of Grid Search in which the average F1-score accuracy will be considered for each experiment. Figure 2 shows the results of this comparison. 

https://github.com/LBolzani/synthetic-health-data-generator/blob/main/images/RF%20Classification%20Real%20and%20Synthetic.png
Figure 2. Utility classification using RF

As depicted in Figure 2, for both real and synthetic dataset, there were no significant differences between the training and testing which demonstrates the absence of either underfitting or overfitting. On the other hand, the results of accuracy for the synthetic were lower but still similar to the real ones which proves the efficacy of the generated synthetic data. 


### Web UI

### Docker container



## FAIR Synthetic Datasets
We generated some synthetic datasets that we described using machine-readable metadata and uploaded in BioStudies repository. In the following sections we describe the metadata model and the criteria used to select an appropriate repository for deposition.

### Metadata model
Having in mind the provision of synthetic datasets reusable for the community and by machines, i.e. FAIR data, we modelled a minimal metadata model. This metadata model is publicly available on [GitHub repository](https://github.com/LBolzani/synthetic-health-data-generator/tree/main/metadata-model) and it is meant primarily for findability of synthetic datasets in public repositories. It is composed of 22 descriptors that describe the dataset, the generation tool, attribution and provenance. We ranked these descriptors following the MoSCoW criteria, where we defined 7 must have descriptors. Thanks to the BioHackathon, we aligned with EDAM developers who were also attending and mapped to EDAM terms the model data values. The model is available as TSV and JSON distributions.

#### Bioschemas

### Repository for deposition


# Discussion
Our overarching goal of developing an infrastructure prototype for the generation of synthetic health data was achieved. Further, we proposed a FAIR implementation recipe by defining a minimal metadata model and suggesting an existing repository for the description, annotation and deposition of the generated synthetic datasets.

# Future work includes:

1. Addition of documentation;
2. Inclusion of more datatypes and Workflows;
3. Mapping the metadata model to the EDAM ontology and BioSchemas, and align to the DOME recommendations;
4. Request a _synthetic data_ metadata profile to the BioStudies repository;
5. Description of the synthetic datasets and its workflow generation as RO-Crate/CWL digital objects;
6. Implement as a Python Package.

As long-term outcomes, we are planning to submit a manuscript on the synthetic health data infrastructure developed following ELIXIR requirements. The development of the infrastructure _per se_ is a long-term outcome, where we envision adding other components such as implementing evaluation metrics to assess the quality of the generated synthetic data and a direct deposition of the synthetic datasets to recommended repositories.

## Contributions


## Acknowledgements

We thank the organisers of the BioHackathon-Europe 2022 for travel support for some of the authors.


## References
