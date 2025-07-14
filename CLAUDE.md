# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Happy-LLM is a comprehensive Chinese-language educational repository for learning Large Language Models (LLMs) from scratch. It provides both theoretical foundations and practical implementations for understanding and building LLMs.

## Architecture Structure

The project is organized into 7 main chapters plus extra content:
- **Chapter 1**: NLP basic concepts and text representation evolution
- **Chapter 2**: Transformer architecture with hands-on PyTorch implementation
- **Chapter 3**: Pre-trained language models (Encoder-only, Encoder-Decoder, Decoder-Only)
- **Chapter 4**: Large language models theory and emergent abilities
- **Chapter 5**: Building LLaMA2 from scratch (215M parameter model implementation)
- **Chapter 6**: Training pipeline practice (pre-training, fine-tuning, LoRA)
- **Chapter 7**: Applications (RAG, Agent systems, evaluation)
- **Extra-Chapter**: Additional blogs and insights from contributors

## Key Technologies Used

- **PyTorch**: Primary deep learning framework
- **Transformers**: Hugging Face ecosystem for model loading/saving
- **DeepSpeed**: For distributed training and optimization
- **SwanLab**: Experiment tracking and visualization
- **Jupyter Notebooks**: Interactive learning and experimentation

## Development Environment Setup

### Python Dependencies
Different chapters have different requirements. Install based on your focus:

**For basic learning (Chapter 2):**
```bash
pip install torch==2.7.0 transformers==4.52.4 numpy pandas
```

**For model building (Chapter 5):**
```bash
pip install torch==2.4.0 transformers==4.44.0 datasets sentence-transformers
```

**For training (Chapter 6):**
```bash
pip install transformers datasets torch deepspeed swanlab
```

**For applications (Chapter 7):**
```bash
pip install openai streamlit  # For Agent and RAG demos
```

## Running Code Examples

### Interactive Notebooks
```bash
# Navigate to chapter directory and run Jupyter
jupyter notebook docs/chapter6/code/whole.ipynb
```

### Training Scripts
```bash
# Pre-training (Chapter 6)
cd docs/chapter6/code
chmod +x pretrain.sh
./pretrain.sh

# Fine-tuning (Chapter 6)
chmod +x finetune.sh
./finetune.sh
```

### Model Demos
```bash
# Chapter 5: Run your custom model
python model_sample.py

# Chapter 7: Agent demo
python docs/chapter7/Agent/demo.py

# Chapter 7: RAG demo
python docs/chapter7/RAG/demo.py
```

## Documentation

- **Main docs**: Available at `docs/` directory with Chinese markdown files
- **Web version**: Serve locally with `docsify serve docs` or visit https://datawhalechina.github.io/happy-llm/
- **PDF version**: Download from GitHub releases

## Model Files

- **Pre-trained models**: Available on ModelScope
  - Happy-LLM-Chapter5-Base-215M
  - Happy-LLM-Chapter5-SFT-215M
- **Tokenizers**: Custom tokenizers in `docs/chapter5/code/tokenizer_k/`

## Key File Locations

- **Core implementations**:
  - `docs/chapter2/code/transformer.py` - Basic Transformer implementation
  - `docs/chapter5/code/k_model.py` - LLaMA2 architecture implementation
  - `docs/chapter7/Agent/src/` - Agent system components
  - `docs/chapter7/RAG/` - RAG implementation

- **Training scripts**:
  - `docs/chapter6/code/pretrain.py` - Pre-training pipeline
  - `docs/chapter6/code/finetune.py` - Fine-tuning pipeline
  - `docs/chapter6/code/ds_config_zero2.json` - DeepSpeed configuration

## Common Development Tasks

### Setting up environment for a specific chapter:
1. Navigate to the chapter's code directory
2. Install requirements: `pip install -r requirements.txt`
3. Run demo scripts or notebooks

### Testing your implementation:
Most chapters include runnable demos. Check the individual README files in each chapter for specific instructions.

### Contributing:
- Follow the existing code style (Chinese comments mixed with English code)
- Place new blog posts in `Extra-Chapter/` following the established structure
- Use the provided PR templates and guidelines

## Important Notes

- All content is in Chinese language
- Uses specific Chinese datasets and models
- Requires understanding of both NLP concepts and PyTorch
- Some paths are hardcoded for Chinese cloud environments (autodl-tmp)
- GPU required for training (CUDA_VISIBLE_DEVICES usage throughout)