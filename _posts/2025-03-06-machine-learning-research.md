---
layout: post
title: "Machine Learning Research"
date: 2025-03-06
---

## 1. Two Steps of Machine Learning — Explained Simply

**Step 1 — Data Collection & Preparation**

Imagine you want to teach a friend to recognize ripe apples. First, you gather hundreds of apples — some ripe, some not — and label each one. That is exactly what data collection and preparation means in machine learning. We gather raw data, clean it up (removing errors or missing values), and organize it so the model can learn from it.

In my work at Nationwide Insurance, this is the step I relate to most. Every ETL pipeline I build in Informatica PowerCenter is essentially about collecting and preparing data — making sure it is clean, consistent, and ready for downstream use. Without good data, no model will produce reliable results, regardless of how sophisticated the algorithm is.

**Step 2 — Model Training & Evaluation**

Now imagine showing your friend those labeled apples repeatedly until they can identify ripe ones on their own. Training is when we feed our prepared data into an algorithm and let it find patterns. Evaluation is when we test how well it learned — did it correctly identify new apples it has never seen before?

In my CSCC capstone project predicting Franklin County housing prices, I trained an OLS regression model and evaluated it using R² (which reached approximately 0.78), meaning the model explained 78% of the variation in home prices. Adding features like school district rankings and geospatial POI data is exactly the training-and-evaluation cycle in practice.

---

## 2. ML Application: AI-Powered Underwriting in Insurance

**a. How ML Improves Existing Solutions**

The application I discovered is AI-driven automated underwriting, where ML models assess risk and price policies in real time. Traditionally, underwriting was a manual, rules-based process — underwriters reviewed applications individually using rigid actuarial tables, a process that could take days.

Machine learning replaces much of this with predictive models trained on millions of past policies, claims data, telematics, and satellite imagery. Key improvements:
- **Speed:** Decisions that took days now happen in seconds
- **Accuracy:** Models detect risk factors human reviewers might miss
- **Personalization:** Risk scoring becomes dynamic and individual
- **Scalability:** Models evaluate thousands of applications simultaneously

**b. Development Status**

AI underwriting is both in active development and already deployed. Lemonade Insurance uses ML models to process claims in seconds. Progressive's Snapshot program uses telematics and ML for personalized auto pricing. Large carriers like Nationwide are investing in AI underwriting as part of broader digital transformation — which is directly connected to the AI initiative sponsoring my CSCC enrollment.

---

## 3. Ethical Concern: Algorithmic Bias in Insurance Underwriting

A significant ethical concern with ML in insurance underwriting is the risk of perpetuating historical bias. When models are trained on historical data, they can encode systemic inequities from the past. For example, if zip codes historically associated with redlining are included as features, a model may assign higher risk scores to those residents — not because of actual individual risk, but because of inherited patterns in the data.

The consequences are material: higher premiums, reduced coverage, or outright denial of coverage for people in already underserved communities.

From a data engineering perspective, this reinforces why feature selection during data preparation is critical. Variables like zip code, while predictive, may serve as proxies for protected characteristics such as race or national origin. Responsible ML practitioners must audit models for disparate impact. Regulatory frameworks like the Fair Housing Act and CFPB guidance on algorithmic discrimination are pushing insurers to implement explainable AI (XAI) and bias audits — an area I expect will grow significantly as AI underwriting scales.

---

## Personal & Professional Connection

This topic connects directly to my daily work as a data engineer at Nationwide and my CSCC coursework. The ML pipeline mirrors the data lifecycle I manage — from ingestion and cleansing through monitoring and evaluation. The ethical dimensions also connect to our AI ethics module on fairness and transparency. As I build skills in Python, statistical modeling, and data visualization, I am working toward contributing to responsible AI development within the insurance industry.
```

**Step 5 — Commit the file**
Scroll down to the **"Commit new file"** section. Add a commit message like:
```
Add Machine Learning Research portfolio entry
