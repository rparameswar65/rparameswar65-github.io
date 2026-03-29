# 🧠 Solving Problems with Large Language Models
### DAT-1850 | Learning Portfolio | Natural Language Processing — LLMs

---

## Overview

In this assignment, I explored how a Large Language Model (LLM) can be used to analyze and extract meaning from classic literary text. I chose to work with **Claude.ai** (Anthropic) as my LLM tool and used *The Wonderful Wizard of Oz* by L. Frank Baum as my source text from [Project Gutenberg](https://www.gutenberg.org/ebooks/55). Throughout this exercise, I connected the capabilities and limitations I observed to real-world applications in **customer communication and Natural Language Processing (NLP) in insurance**, which is directly relevant to my work as a data engineer at Nationwide Insurance.

---

## Step 1: Choosing a Book

I selected ***The Wonderful Wizard of Oz*** (1900) by L. Frank Baum for several reasons:

- It is a **familiar, widely recognized narrative**, which made it easy to evaluate whether the LLM's responses were accurate or hallucinated.
- The book features **rich dialogue, distinct characters, and a clear narrative arc** — all of which are ideal for testing an LLM's ability to summarize, analyze tone, and extract structured information.
- The text is relatively short and freely available as a plain `.txt` file on Project Gutenberg, making it easy to paste relevant passages directly into the LLM prompt.
- On a personal level, the story's central theme — navigating an unfamiliar world by building knowledge, trusting new allies, and finding your way home — resonated with my own journey from traditional ETL engineering into AI and data analytics.

**Source:** [Project Gutenberg — The Wonderful Wizard of Oz](https://www.gutenberg.org/ebooks/55)

---

## Step 2: Interacting with the LLM (Claude.ai)

After downloading the plain text file, I copied selected passages and chapters into Claude.ai and engaged in a structured series of prompts. Below is a summary of each interaction.

---

### Interaction 1: Character Extraction

**Prompt:**  
> *"Based on the text I've provided, list the main characters in The Wonderful Wizard of Oz and give a one-sentence description of each."*

**LLM Response Summary:**  
Claude returned a well-structured list including Dorothy, Toto, the Scarecrow, the Tin Woodman, the Cowardly Lion, Glinda (the Good Witch), the Wicked Witch of the West, and the Wizard. Each description accurately reflected the character's role and defining trait (e.g., the Scarecrow wanting a brain, the Tin Woodman wanting a heart).

**Observation:**  
The response was accurate and well-organized. Interestingly, Claude volunteered that Toto, while minor in dialogue, plays a significant plot-triggering role — something a casual reader might overlook. This "value-add" insight beyond the literal question mirrors how a skilled human analyst might flag a subtle but important detail.

---

### Interaction 2: Tone and Sentiment Analysis

**Prompt:**  
> *"Analyze the emotional tone of Dorothy's dialogue throughout the chapters I've shared. Is her communication style consistent? How does it shift, if at all?"*

**LLM Response Summary:**  
Claude identified Dorothy's tone as predominantly **hopeful and resilient**, occasionally shifting to **anxious or assertive** in moments of confrontation (particularly with the Wicked Witch and the Wizard). It noted that her language becomes more confident and direct in later chapters as her agency increases.

**Observation:**  
This type of sentiment arc analysis is closely related to how NLP tools are used in insurance — for example, analyzing customer emails or call transcripts over the lifecycle of a claim to detect frustration escalation, confusion, or satisfaction. The LLM's ability to perform this analysis on unstructured literary text demonstrates the same underlying capability that powers real-world insurance customer communication tools.

---

### Interaction 3: Summarization and Key Theme Extraction

**Prompt:**  
> *"Summarize the plot of The Wonderful Wizard of Oz in three paragraphs, then list the three most important themes of the book."*

**LLM Response Summary:**  
The summary was accurate and well-paced. The three themes identified were: **(1) the power of self-belief**, **(2) the value of community and collaboration**, and **(3) the idea that "home" is not a place but a state of belonging**. Claude also mentioned that the text can be read as an allegory for the American Populist movement of the 1890s — an interpretation that was historically accurate and demonstrated knowledge beyond the text itself.

**Observation:**  
This showed that the LLM is not operating purely on the pasted text — it is drawing on its broader training data to enrich its response. This is a double-edged capability: it adds depth, but it also means the model can "drift" beyond the document and potentially introduce information that wasn't in the original text. In regulated industries like insurance, this distinction between *in-document evidence* and *model-generated inference* is critical.

---

### Interaction 4: Question Answering (Comprehension Test)

**Prompt:**  
> *"At the end of the story, how does Dorothy return home? What does this reveal about the nature of the Wizard's power?"*

**LLM Response Summary:**  
Claude correctly explained that Dorothy's silver shoes (changed to ruby slippers in the 1939 film) always had the power to return her home, and that the Wizard was revealed as an ordinary man — a showman from Omaha — who wielded the *perception* of power rather than real magic. Claude noted this as a commentary on authority built on illusion.

**Observation:**  
The LLM accurately distinguished between the **book's silver shoes** and the **film's ruby slippers** without being prompted — a detail that many people confuse. This demonstrated strong factual grounding and attention to source fidelity.

---

## Step 3: Challenges and Limitations

Despite strong overall performance, I observed several notable limitations:

| Challenge | Description |
|---|---|
| **Context window constraints** | I could not paste the entire book at once. I had to work chapter-by-chapter, which meant the LLM could not perform whole-book analysis in a single pass. |
| **Hallucination risk** | When I asked a vague follow-up question without pasting new text, the LLM occasionally blended book details with knowledge from the 1939 film adaptation. This highlights the importance of well-scoped, grounded prompts. |
| **No memory between sessions** | Each new session required re-pasting context. There was no persistent memory of prior interactions with the same text. |
| **Confidence without calibration** | The LLM presented all responses with similar confidence, whether it was reporting a clear textual fact or making an interpretive inference. A human analyst would typically signal the difference more explicitly. |

---

## Step 4: Reflection — LLM Patterns vs. Human Responses

The LLM's responses were consistently fluent, well-structured, and accurate at a surface level. However, I noticed a few behavioral patterns that distinguished it from how a human expert might respond:

- **A human reader** would likely express personal emotional reactions to the story, reference their prior reading experiences, or ask clarifying questions before answering. The LLM responded immediately and thoroughly regardless of ambiguity.
- **A human analyst** would flag uncertainty (e.g., "I'm not sure if this is in the book or the movie"). The LLM required explicit prompting to make this distinction.
- **A human communicator** might tailor the depth of their summary based on perceived audience expertise. The LLM defaulted to a moderate level of detail unless prompted to adjust.

These differences are important to understand when designing AI-assisted workflows. The LLM excels at **speed, consistency, and breadth** — but human oversight remains essential for **judgment, uncertainty signaling, and contextual calibration**.

---

## Professional Connection: NLP in Insurance Customer Communication

This exercise reinforced several concepts that are directly applicable to AI-driven customer communication at Nationwide Insurance and the broader P&C insurance industry:

**1. Sentiment Analysis on Claims Correspondence**  
Just as I analyzed Dorothy's shifting emotional tone, NLP models are used to analyze inbound customer emails and call center transcripts to detect frustration, confusion, or urgency — enabling proactive intervention before a complaint escalates.

**2. Automated Summarization of Policy Documents**  
The summarization capability I tested maps directly to use cases where LLMs distill dense policy language into plain-English summaries for customers during the quoting or claims process, reducing call volume and improving satisfaction scores.

**3. Grounding and Hallucination Risk in Regulated Contexts**  
The hallucination behavior I observed — where the LLM blended book and film details — is a critical risk in insurance, where confabulated policy terms or coverage explanations could expose the company to liability. This reinforces why **Retrieval-Augmented Generation (RAG)** architectures (grounding LLM responses in verified policy documents) are essential for production insurance AI systems.

**4. Human-in-the-Loop Design**  
The LLM's lack of uncertainty signaling underscores the need for human review in high-stakes communication. In claims triage, an AI might draft a response, but a licensed adjuster must review it before it is sent — especially in states with strict fair claims handling regulations.

---

## Conclusion

Working with Claude.ai on *The Wonderful Wizard of Oz* was a productive exercise in understanding what LLMs do well and where their boundaries lie. The model demonstrated strong capabilities in **extraction, summarization, sentiment analysis, and question answering** — all of which have direct analogs in enterprise NLP applications. At the same time, the limitations I observed — hallucination risk, context constraints, and confidence miscalibration — are exactly the challenges that data engineers and AI practitioners must design around when building reliable, production-grade AI systems.

As I continue building toward AI engineering roles in the insurance domain, this hands-on experience sharpens my ability to evaluate LLM outputs critically and design workflows where AI augments — rather than replaces — human judgment.

---

## Resources

- 📖 [Project Gutenberg — The Wonderful Wizard of Oz](https://www.gutenberg.org/ebooks/55)
- 🤖 [Anthropic Claude.ai](https://claude.ai)
- 📘 [Anthropic Model Documentation](https://docs.anthropic.com)
- 🔗 [GitHub Learning Portfolio](https://github.com/rparameswar65/rparameswar65-github.io)

---

*Submitted for DAT-1850 | Natural Language Processing — LLMs Discussion Board*  
*Columbus State Community College | Workforce Innovation Program*
