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

## XHTML Conversion TODO

### Completed (Done)
- [x] `docs/chapter1/第一章 NLP基础概念.md` → `docs/chapter1.xhtml`
- [x] `docs/chapter2/第二章 Transformer架构.md` → `docs/chapter2_transformer_architecture.xhtml`
- [x] `docs/chapter3/第三章 预训练语言模型.md` → `docs/chapter3_pretrained_language_models.xhtml`
- [x] `docs/chapter4/第四章 大语言模型.md` → `docs/chapter4_large_language_models.xhtml`
- [x] `docs/chapter5/第五章 动手搭建大模型.md` → `docs/chapter5_building_large_models.xhtml`
- [x] `docs/前言.md` → `docs/preface.xhtml`

### Completed (All XHTML files generated)
- [x] `Extra-Chapter/why-fine-tune-small-large-language-models/readme.md` → `Extra-Chapter/why-fine-tune-small-large-language-models/readme.xhtml`
- [x] `docs/chapter6/6.4[WIP] 偏好对齐.md` → `docs/chapter6/6.4[WIP] 偏好对齐.xhtml`
- [x] `docs/chapter6/第六章 大模型训练流程实践.md` → `docs/chapter6/第六章 大模型训练流程实践.xhtml`
- [x] `docs/chapter7/第七章 大模型应用.md` → `docs/chapter7/第七章 大模型应用.xhtml`
- [x] `Extra-Chapter/transformer-architecture/readme.md` → `Extra-Chapter/transformer-architecture/readme.xhtml`

## XHTML Conversion Requirements

### Requirements
1. **目标格式**：将markdown文件转换为xhtml格式，后续用于转换为epub电子书
2. **标准要求**：生成的xhtml必须符合epub规范要求
3. **样式文件**：使用 `./docs/epub-style.css` 作为样式表（可修改）

### 转换规范
- 使用标准XHTML 1.1或XHTML5格式
- 确保所有标签正确闭合
- 图片路径需要相对化
- 数学公式优先使用MathML格式
- 代码块使用`<pre><code>`标签
- 表格使用标准HTML表格格式
- 目录结构符合epub规范
- 字符编码统一为UTF-8