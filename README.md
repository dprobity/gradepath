Readme v1

📊 GradePath

ML-Enabled Academic Decision Support System

Overview

GradePath is an applied machine learning system designed to help students make informed academic decisions under GPA constraints.

Students often track grades manually across fragmented sources such as syllabi PDFs and learning management systems (LMS), leading to calculation errors, poor planning, and uncertainty around critical outcomes (e.g. maintaining scholarship GPA thresholds).
GradePath centralizes these data sources and provides predictive, explainable “what-if” analysis to support accurate academic planning.

Problem Statement

Academic planning suffers from three core issues:

Fragmented data

Syllabi stored as unstructured PDFs

Grades distributed across LMS platforms

Manual calculations prone to error

Lack of predictive insight

Students cannot easily answer questions like:
“What score do I need on the final to maintain a 3.5 GPA?”

Poor decision support

Existing tools track grades but do not model outcomes under constraints

GradePath addresses these gaps by transforming unstructured academic data into predictive signals that support decision-making.

System Architecture (High Level)
Syllabus PDFs ──► OCR / NLP Parsing ──► Structured Course Data
                                           │
LMS APIs ───────────────► Grade Ingestion ──┘
                                           │
                               Predictive & Deterministic Modeling
                                           │
                           What-If Simulation & Decision Support
                                           │
                               Context-Aware Guidance (RAG)

Key Features
1. Document Processing & Feature Extraction

OCR and NLP pipelines extract:

grading weights

deadlines

assignment structure

Converts unstructured syllabus PDFs into structured, machine-readable data

2. Real-Time Grade Integration

LMS data ingestion via APIs

Maintains up-to-date academic state

Enables dynamic recalculation as grades change

3. Predictive & Deterministic Modeling

Simulates grade outcomes under user-defined GPA targets

Supports scenario analysis (e.g. best/worst-case outcomes)

Designed for transparency and explainability rather than black-box prediction

4. Context-Aware Guidance (RAG)

Retrieval-augmented generation grounded in course-specific materials

Avoids generic responses by constraining answers to relevant academic context

Machine Learning Components
Component	Purpose
OCR / NLP	Extract structured signals from syllabus PDFs
Feature Engineering	Encode grading structure and constraints
Predictive Modeling	Estimate required scores for GPA targets
Deterministic Simulation	Exact outcome computation under constraints
RAG	Context-grounded academic guidance

Note: GradePath prioritizes explainability and correctness over opaque prediction, aligning with decision-support best practices.

Evaluation & Impact

Reduced manual grade calculations from hours per term to seconds per query

Eliminated common arithmetic and tracking errors

Enabled repeatable, explainable academic planning

Designed to scale across multiple courses and academic terms

Tech Stack

Language: Python

ML / Data: PyTorch, NumPy, Pandas, scikit-learn

NLP / RAG: OCR pipelines, retrieval-augmented generation

Systems: APIs, data pipelines

Infrastructure: Docker, cloud-deployable architecture

Repository Structure (Planned)
gradepath/
├── data/
│   ├── raw/              # Raw syllabus PDFs, LMS exports
│   ├── processed/        # Structured course data
├── src/
│   ├── ingestion/        # OCR, NLP, LMS API clients
│   ├── features/         # Feature engineering logic
│   ├── models/           # Predictive & deterministic models
│   ├── evaluation/       # Metrics and validation
│   └── app/              # Decision-support interface
├── notebooks/            # Exploratory analysis
├── tests/
├── README.md

Future Work

Quantitative evaluation of extraction accuracy and prediction error

Support for uncertainty estimation in scenario modeling

Extension to multi-semester GPA optimization

User-level personalization and longitudinal performance analysis

Motivation & Learning Goals

This project was built to:

Practice designing end-to-end ML systems, not just training models

Apply ML to a real decision-support problem

Emphasize evaluation, explainability, and system design

Bridge applied ML with practical user impact

Author

David Emehelu
Applied Machine Learning | ML Systems`
