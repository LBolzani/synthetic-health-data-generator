---
title: 'Infrastructure for Synthetic Health Data'
title_short: 'Synthetic Health Data'
tags:
  - Health data
  - Synthetic data
  - Workflows
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

Following up the efforts currently undertaken in the ELIXIR Health Data and the Machine Learning Focus Groups around the synthetic health data landscape, this project will focus on the health data providers' need for a ready-to-use synthetic data platform which is assessed by health data experts, researchers, and ML specialists. Aligned to ELIXIR Health Data Focus Group’s objectives, we aim at building an infrastructure for synthetic health data offering a dockerized synthetic data generator based on the open-source libraries Synthetic Data Vault (SDV) (github.com/sdv-dev) and ydata-synthetic (github.com/ydataai) with state of the art ML methods. This will enable users to generate synthetic data that has the same structure and statistical properties as the original dataset from a variety of data types (clinical, variational or omics). Despite the capacity to generate their own datasets, a set of exemplary datasets will be publicly available in appropriate repositories and will include rich metadata descriptions according to the DOME recommendations (https://dome-ml.org/) and GA4GH (ga4gh.org) standards. OpenEBench (openebench.bsc.es) will host a community of practice for comparing different approaches for synthetic data generation.


# Results

## Synthetic Data Generation workflows

## Web UI

## Docker container

## FAIR Synthetic Datasets
We generated some synthetic datasets that we described using machine-readable metadata and uploaded in BioStudies repository. In the following sections we describe the metadata model and the criteria used to select an appropriate repository for deposition.

### Metadata model
Having in mind the provision of synthetic datasets reusable for the community and by machines, i.e. FAIR data, we modelled a minimal metadata model.

#### BioSchemas

### Repository for deposition


# Discussion


# Future work includes:

1. Documentation;
2. ...

As long-term outcomes, we are planning to submit a manuscript on the synthetic health data infrastructure developed following ELIXIR requirements. The development of the infrastructure _per se_ is a long-term outcome, where we envision adding other components such as implementing evaluation metrics to assess the quality of the generated synthetic data and a direct deposition of the synthetic datasets to recommended repositories.

## Contributions


## Acknowledgements

We thank the organisers of the BioHackathon-Europe 2022 for travel support for some of the authors.


## References
