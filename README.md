# Unified Alignment of Protein-Protein Interaction Networks

Supplementary data and resources for the paper on **[Unified Alignment of Protein-Protein Interaction Networks](https://doi.org/10.1038/s41598-017-01085-9)**.

## Authors

- N. Malod-Dognin
- K. Ban
- N. Przulj

**Corresponding Author:** Prof. Natasa Przulj  
📧 natasa.przulj@mbzuai.ac.ae

## Overview

This repository provides the datasets and scripts used in our research on unified alignment methods for protein-protein interaction networks.

## Repository Contents

### Datasets
Complete datasets used in the experiments and analyses.

**[Download Datasets](http://www0.cs.ucl.ac.uk/staff/natasa/Ulign/Datasets.zip)** (ZIP archive)

### Ulign Python Script
Python implementation for unifying network alignments across different methods.

## Network Alignment Tools

Our study utilized the following network alignment algorithms (listed alphabetically):

- **[HUBALIGN](http://www.ru.nl/publish/pages/726696/hubalign.zip)** - Hub-based network alignment
- **[L-GRAAL](http://www0.cs.ucl.ac.uk/staff/natasa/lagrangian-graal/)** - Lagrangian relaxation-based graph alignment
- **[MAGNA++](http://www3.nd.edu/~cone/MAGNA++/)** - Genetic algorithm-based network aligner
- **[NATALIE](http://www.molgen.mpg.de/~natalie/)** - Network alignment tool based on integer linear programming
- **[OPTNET](http://www.optnetalign.org/)** - Optimal network alignment
- **[PISWAP](http://www.ibi.vu.nl/programs/piswapwww/)** - Protein interaction network alignment via swapping
- **[SPINAL](http://www.loria.fr/~aalekes/spinal.html)** - Scalable protein interaction network aligner

## Installation

```bash
git clone https://github.com/przulj-lab/ulign.git
cd ulign
```

## Usage

```python
# Example usage of Ulign script
python ulign.py
```

## Citation

If you use this code or data in your research, please cite:

```
N. Malod-Dognin, K. Ban and N. Przulj
Unified Alignment of Protein-Protein Interaction Networks
Sci Rep. 2017 Apr 19;7(1):953. doi: 10.1038/s41598-017-01085-9. PMID: 28424527; PMCID: PMC5430463.
```

## Contact

For questions or issues, please contact Prof. Natasa Przulj at natasa.przulj@mbzuai.ac.ae
