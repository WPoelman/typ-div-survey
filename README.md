# typ-div

Data and code for the EMNLP 2024 paper "What is 'Typological Diversity' in NLP?" by [Esther Ploeger](https://twitter.com/EstherPloeger), [Wessel Poelman](https://wesselpoelman.nl/), [Miryam de Lhoneux](https://people.cs.kuleuven.be/~miryam.delhoneux/) and [Johannes Bjerva](https://bjerva.github.io/).

The paper can be found here: https://arxiv.org/abs/2402.04222

## Abstract
The NLP research community has devoted increased attention to languages beyond English, resulting in considerable improvements for multilingual NLP. However, these improvements only apply to a small subset of the world's languages. An increasing number of papers aspires to enhance generalizable multilingual performance across languages. To this end, linguistic typology is commonly used to motivate language selection, on the basis that a broad typological sample ought to imply generalization across a broad range of languages. These selections are often described as being typologically diverse. In this meta-analysis, we systematically investigate NLP research that includes claims regarding typological diversity. We find there are no set definitions or criteria for such claims. We introduce metrics to approximate the diversity of resulting language samples along several axes and find that the results vary considerably across papers. Crucially, we show that skewed language selection can lead to overestimated multilingual performance. We recommend future work to include an operationalization of typological diversity that empirically justifies the diversity of language samples. To help facilitate this, we release the code for our diversity measures.

## Usage
Tested with Python 3.11.

```
pip install -r requirements.txt
```

And then run the notebooks in order.


## Citation
```bibtex
@inproceedings{ploeger-etal-2024-typological,
  title={What is {{``Typological Diversity''}} in {{NLP}}?},
  author={Ploeger, Esther and Poelman, Wessel and de Lhoneux, Miryam and Bjerva, Johannes},
  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year={2024}
}
```

## Data Licenses
- [Grambank](https://grambank.clld.org/) is licensed under a [Creative Commons 4.0 BY International License](https://creativecommons.org/licenses/by/4.0/).
- [WALS](https://wals.info/) is licensed under a [Creative Commons 4.0 BY International License](https://creativecommons.org/licenses/by/4.0/).
- [URIEL and `lang2vec`](https://github.com/antonisa/lang2vec) are licensed under a [Creative Commons 4.0 BY-SA International License](https://creativecommons.org/licenses/by-sa/4.0/).


## Credits
We want to thank Thomas Bauwens for his help creating the tables and his nice [plotting library](https://github.com/bauwenst/fiject).
