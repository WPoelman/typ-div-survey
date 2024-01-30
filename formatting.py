def make_bold(s):
    return f"\\textbf{{{s}}}"


def make_it(s):
    return f"\\textit{{{s}}}"


# Not a great solution, but it works and is the most human 'readable'
TITLE_MAP = {
    "MIA 2022 Shared Task: Evaluating Cross-lingual Open-Retrieval Question Answering for 16 Diverse Languages": (
        "\\citet{asai-etal-2022-mia}",
        None,
        "QA",
    ),
    "Making More of Little Data: Improving Low-Resource Automatic Speech Recognition Using Data Augmentation": (
        "\\citet{bartelds-etal-2023-making}",
        None,
        "ASR",
    ),
    "Learning and Evaluating Emotion Lexicons for 91 Languages": (
        "\\citet{buechel-etal-2020-learning-evaluating}",
        None,
        "Lexicon generation",
    ),
    "IGLUE: A Benchmark for Transfer Learning across Modalities, Tasks, and Languages": (
        "\\citet{bugliarello2022iglue}",
        "IGLUE",
        "Visual QA, IR, RE, NLI",
    ),
    "TyDi QA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages": (
        "\\citet{clark-etal-2020-tydi}",
        "TyDiQA",
        "QA",
    ),
    "MasakhaPOS: Part-of-Speech Tagging for Typologically Diverse African languages": (
        "\\citet{dione-etal-2023-masakhapos}",
        "MasakhaPOS",
        "Part-of-speech tagging",
    ),
    "MorphAGram, Evaluation and Framework for Unsupervised Morphological Segmentation": (
        "\\citet{eskander-etal-2020-morphagram}",
        "MorphAGram",
        "Morphological segmentation",
    ),
    "MASSIVE: A 1M-Example Multilingual Natural Language Understanding Dataset with 51 Typologically-Diverse Languages": (
        "\\citet{fitzgerald-etal-2023-massive}",
        "MASSIVE",
        "Slot-filling, Intent classification",
    ),
    "Findings of the SIGMORPHON 2023 Shared Task on Interlinear Glossing": (
        "\\citet{ginn-etal-2023-findings}",
        None,
        "Interlinear glossing",
    ),
    "XHate-999: Analyzing and Detecting Abusive Language Across Domains and Languages": (
        "\\citet{glavas-etal-2020-xhate}",
        "XHate-999",
        "Abusive language classification",
    ),
    "SIGMORPHON–UniMorph 2023 Shared Task 0: Typologically Diverse Morphological Inflection": (
        "\\citet{goldman-etal-2023-sigmorphon}",
        None,
        "Morphological inflection",
    ),
    "Cross-Lingual Knowledge Distillation for Answer Sentence Selection in Low-Resource Languages": (
        "\\citet{gupta-etal-2023-cross}",
        "Xtr-WikiQA \& TyDi-AS2",
        "QA, Answer sentence selection",
    ),
    "MultiTACRED: A Multilingual Version of the TAC Relation Extraction Dataset": (
        "\\citet{hennig-etal-2023-multitacred}",
        "MultiTACRED",
        "Relation extraction",
    ),
    "SMALLWorlds – Multilingual Content-Controlled Monologues": (
        "\\citet{henrichsen-uneson-2012-smallworlds}",
        "SMALLWorlds",
        "ASR",
    ),
    "Multi2WOZ: A Robust Multilingual Dataset and Conversational Pretraining for Task-Oriented Dialog": (
        "\\citet{hung-etal-2022-multi2woz}",
        "Multi2WOZ",
        "Task-oriented dialogues",
    ),
    "The ACQDIV Corpus Database and Aggregation Pipeline": (
        "\\citet{jancso-etal-2020-acqdiv}",
        "ACQDIV",
        "Language acquisition",
    ),
    "X-FACTR: Multilingual Factual Knowledge Retrieval from Pretrained Language Models": (
        "\\citet{jiang-etal-2020-x}",
        "X-FACTR",
        "Knowledge retrieval",
    ),
    "SIGMORPHON–UniMorph 2022 Shared Task 0: Generalization and Typologically Diverse Morphological Inflection": (
        "\\citet{kodner-etal-2022-sigmorphon}",
        None,
        "Morphological inflection",
    ),
    "Visually Grounded Reasoning across Languages and Cultures": (
        "\\citet{liu-etal-2021-visually}",
        "MaRVL",
        "Visually grounded RE",
    ),
    "MKQA: A Linguistically Diverse Benchmark for Multilingual Open Domain Question Answering": (
        "\\citet{longpre-etal-2021-mkqa}",
        "MKQA",
        "QA",
    ),
    "Manual Clustering and Spatial Arrangement of Verbs for Multilingual Evaluation and Typology Analysis": (
        "\\citet{majewska-etal-2020-manual}",
        "SpAM",
        "Verb analysis",
    ),
    "Morphological Segmentation for Low Resource Languages": (
        "\\citet{mott-etal-2020-morphological}",
        None,
        "Morphological segmentation",
    ),
    "Using Neural Machine Translation for Generating Diverse Challenging Exercises for Language Learner": (
        "\\citet{palma-gomez-etal-2023-using}",
        None,
        "Language learning, cloze test",
    ),
    "xGQA: Cross-Lingual Visual Question Answering": (
        "\\citet{pfeiffer-etal-2022-xgqa}",
        "xGQA",
        "Visual QA",
    ),
    "XCOPA: A Multilingual Dataset for Causal Commonsense Reasoning": (
        "\\citet{ponti-etal-2020-xcopa}",
        "XCOPA",
        "Commonsense reasoning",
    ),
    "XTREME-R: Towards More Challenging and Nuanced Multilingual Evaluation": (
        "\\citet{ruder-etal-2021-xtreme}",
        "XTREME-R",
        "Classification, Parsing, IR, QA",
    ),
    "Understanding Compositional Data Augmentation in Typologically Diverse Morphological Inflection": (
        "\\citet{samir-silfverberg-2023-understanding}",
        None,
        "Morphological inflection",
    ),
    "DivEMT: Neural Machine Translation Post-Editing Effort Across Typologically Diverse Languages": (
        "\\citet{sarti-etal-2022-divemt}",
        "DivEMT",
        "MT post-editing",
    ),
    "Co-reference annotation and resources: A multilingual corpus of typologically diverse languages": (
        "\\citet{sasaki-etal-2002-co}",
        None,
        "Co-reference resolution",
    ),
    "Language models are multilingual chain-of-thought reasoners": (
        "\\citet{shi2023language}",
        "MGSM",
        "Arithmetic reasoning",
    ),
    "A Database for Measuring Linguistic Information Content": (
        "\\citet{sproat-etal-2014-database}",
        None,
        "Linguistic information content",
    ),
    "TyDiP: A Dataset for Politeness Classification in Nine Typologically Diverse Languages": (
        "\\citet{srinivasan-choi-2022-tydip}",
        "TyDiP",
        "Politeness classification",
    ),
    "Multi-SimLex: A Large-Scale Evaluation of Multilingual and Crosslingual Lexical Semantic Similarity": (
        "\\citet{vulic-etal-2020-multi}",
        "Multi-SimLex",
        "Semantic similarity",
    ),
    "SIGMORPHON 2020 Shared Task 0: Typologically Diverse Morphological Inflection": (
        "\\citet{vylomova-etal-2020-sigmorphon}",
        None,
        "Morphological inflection",
    ),
    "SLABERT Talk Pretty One Day: Modeling Second Language Acquisition with BERT": (
        "\\citet{yadavalli-etal-2023-slabert}",
        "SLABERT",
        "Second language acquisition",
    ),
    "Mr. TyDi: A Multi-lingual Benchmark for Dense Retrieval": (
        "\\citet{zhang-etal-2021-mr}",
        "Mr. TyDi",
        "IR",
    ),
    "MIRACL: A Multilingual Retrieval Dataset Covering 18 Diverse Languages": (
        "\\citet{zhang-etal-2023-miracl}",
        "MIRACL",
        "IR",
    ),
}
