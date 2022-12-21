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
  - name: Marcos Casado Barbero
    orcid: 0000-0002-7747-6256
    affiliation: 3
affiliations:
  - name: Human Genetics, Leiden University Medical Center, Leiden, Netherlands
    index: 1
  - name: Luxembourg Center for Systems Biomedicine, University of Luxembourg, Luxembourg
    index: 2
  - name: European Molecular Biology Laboratory - European Bioinformatics Institute (EMBL-EBI), Hinxton CB10 1SD, UK
    index: 3
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

Following up the efforts currently undertaken in the ELIXIR Health Data and the Machine Learning Focus Groups around the synthetic health data landscape, this project focuses on the health data providers' need for a ready-to-use synthetic data platform assessed by health data experts, researchers, and ML specialists. Aligned with ELIXIR Health Data Focus Group’s objectives, we aim at building an infrastructure for synthetic health data offering a dockerized synthetic data generator based on the open-source libraries Synthetic Data Vault (SDV) (github.com/sdv-dev) and ydata-synthetic (github.com/ydataai) with state of the art ML methods. This framework will enable users to generate synthetic data that has the same structure and statistical properties as the original dataset from a variety of data types (clinical, variational or omics). Despite the capacity to generate their own datasets, a set of exemplary datasets will be publicly available in appropriate repositories and will include rich metadata descriptions according to the DOME recommendations (https://dome-ml.org/) and GA4GH (ga4gh.org) standards. OpenEBench (openebench.bsc.es) will host a community of practice for comparing different approaches for synthetic data generation. Here, we present our prototype for the generation of synthetic health data and our proposed FAIR implementation of the generated synthetic datasets developed after one week of BioHacking together 20 participants (10 new to the project), from different countries (NL, ES, LU, UK, GR, FL, DE).

<!--
# Results
-->

## Infrastructure for Synthetic Health Data
For stress and test development of new ML code, we need suitable data to properly demonstrate the tools application. However, ML developers without data access are not able to see how the tool performs for its intended application. One way to enable this is to generate _synthetic data_, where new "fake" data is created from real data using a specifically designed model. Importantly, the generation model must maintain the original features and structure to be as realistic as possible to the original data. In particular, synthetic data goals are to ensure:

1. applicability: the synthetic data must fit for its intended application.
2. quality: it must be a sufficient and necessary representation of the real data.
3. privacy: synthetic data must be anonymous or pseudo-anonymous. In other words, linkage between the synthetic data and a natural person must be protected, thus preventing that a generated synthetic patient is actually real.

Our main goal was to provide to the health community and life sciences researchers with a simple and reusable way of generating privacy-preserving and effective synthetic data. This is to be used in artificial intelligence technologies and ML methods to speed up research on health data. Next, we present the workflows we developed to generate synthetic health data; how the data could be evaluated; the user interfaces to interact with the whole process; and how to make the synthetic datasets FAIR for others to reuse.


### Synthetic Data Generation workflows
To develop an infrastructure for generating synthetic health data that is easy to use, we first explored how to generate synthetic health data from real data. There are many existing methods to generate synthetic data. The first challenge is that these methods are usually tailored for a specific type and format of the input dataset. The second challenge is to evaluate the quality of the generated synthetic dataset to know whether the model and the data are actually useful.

We first defined an input data type which was _tabular data_ for its simplicity. Then, we chose a starting dataset that was already published and open-access. We selected the [Breast Cancer Wisconsin (Diagnostic) Data set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data) published in the Kaggle website rated with a usability of $8.53$. This dataset contains 32 columns, including: 2 attributes (identifier _ID_ (integer) and _Diagnosis_ (M=malignant, B=benign)); 10 real-valued features computed for each cell nucleus from a digitized image of a breast mass; and three statistical parameters for each feature (_Mean_, _standard error_ and _worst_). They describe characteristics of the cell nuclei present in the image [@bennett1992]. This dataset is similar to those for clinical research making it suitable to produce synthetic data for health.

We experimented with three synthetic data generators: SDV, DataSynthesizer and Synthea.  

### Quality assessment

### Web UI

### Docker container



## FAIR Synthetic Datasets
We generated some synthetic datasets that we described using machine-readable metadata and uploaded to BioStudies repository (**#! Add URL**). In the following sections we describe the metadata model and the criteria used to select an appropriate repository for deposition.

### Metadata model
Having in mind the provision of synthetic datasets that were reusable for the community and readable by machines, i.e. FAIR data, we designed a metadata model to use as guidance for end-users of our framework. This metadata model is publicly available on [GitHub repository](https://github.com/LBolzani/synthetic-health-data-generator/tree/main/metadata-model). It is meant primarily to improve findability of synthetic datasets in public repositories. It is composed of 26 descriptors that, together, provide context for 4 different semantic groups: the dataset, generation tool, attribution and provenance. Not all of these descriptors are required for a functional metadata model, and thus we ranked them following the MoSCoW criteria: 11 Must-, 8 Should- and 7 Could-haves. For the sake of consistency in the metadata of these fields, we provided the recommended ontology mappings to use when populating the metadata model. Due to EDAM developers also attended the ELIXIR BioHackathon, we were able to align with EDAM's ontology and map most terms to this ripe ontology.

The model is available as TSV and JSON distributions.

#### Bioschemas

### Repository for deposition


# Discussion
Our overarching goal of developing an infrastructure prototype for the generation of synthetic health data was achieved. Further, we proposed a FAIR implementation recipe by defining a minimal metadata model and suggesting an existing repository for the description, annotation and deposition of the generated synthetic datasets.

# Future work includes:

1. Addition of documentation;
2. Inclusion of more datatypes and Workflows;
3. ~~Mapping the metadata model to the EDAM ontology and BioSchemas~~, and align to the DOME recommendations;
4. Request a _synthetic data_ metadata profile to the BioStudies repository;
5. Description of the synthetic datasets and its workflow generation as RO-Crate/CWL digital objects;
6. Implement as a Python Package.

As long-term outcomes, we are planning to submit a manuscript on the synthetic health data infrastructure developed following ELIXIR requirements. The development of the infrastructure _per se_ is a long-term outcome, where we envision adding other components such as implementing evaluation metrics to assess the quality of the generated synthetic data and a direct deposition of the synthetic datasets to recommended repositories.

## Contributions


## Acknowledgements

We thank the organisers of the BioHackathon-Europe 2022 for travel support for some of the authors.


## References
