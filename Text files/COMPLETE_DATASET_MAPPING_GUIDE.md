# 🗺️ KrishiMitra AI - COMPLETE Dataset Mapping Guide
**ALL datasets mapped to directory structure - Must-Have, Important & Nice-to-Have**

## 📁 Directory Structure Overview
```
D:\SIH\farmer-ai-system\data\
├── vision/          # Vision Model Datasets (EfficientNet/YOLO)
├── speech/          # Speech Model Datasets (Whisper)
├── text_qa/         # Text/QA Model Datasets (TinyLlama)
├── translation/     # Translation Model Datasets (NLLB)
└── market/          # Market Forecasting Model Datasets
```

---

## 🔍 A. VISION MODEL DATASETS

### 🔴 Must-Have (Priority: High)

#### 1. PlantVillage Dataset (~54k images, ~1.2GB)
**📥 Source**: https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset
**📂 Extract to**: `data/vision/plantvillage/`
```
data/vision/plantvillage/
└── raw/             # All downloaded images (split during training)
```
**🔧 Processing Steps**:
- Download and extract Kaggle dataset directly to raw/ folder
- Keep original class folder structure from Kaggle
- Split will be done programmatically during model training

#### 2. PlantDoc Dataset (~2.5k images, ~500MB)
**📥 Source**: https://github.com/pratikkayal/PlantDoc-Dataset
**📂 Extract to**: `data/vision/plantdoc/`
```
data/vision/plantdoc/
└── raw/             # All downloaded files (images + annotations)
```

#### 3. Universal Crop Datasets (~15GB total) - ALL INDIAN CROPS
**📂 Extract to**: `data/vision/universal_crops/`

##### A. CEREALS (25+ varieties)
**📂 Path**: `data/vision/universal_crops/cereals/`
- Rice: https://www.kaggle.com/datasets/vbookshelf/rice-leaf-diseases
- Wheat: https://www.kaggle.com/datasets/olyadanylenko/wheat-leaf-disease-detection  
- Maize: https://www.kaggle.com/datasets/smaranjitghose/corn-or-maize-leaf-disease-dataset
- Millets: https://www.kaggle.com/datasets/aman2000jaiswal/millet-crop-disease-detection
- Barley: https://www.kaggle.com/datasets/rashikrahmanpritom/barley-disease-dataset

##### B. PULSES (8+ varieties)  
**📂 Path**: `data/vision/universal_crops/pulses/`
- Chickpea: https://www.kaggle.com/datasets/nirmalsankalana/chickpea-leaf-disease-dataset
- Lentil: https://www.kaggle.com/datasets/theeyeschico/lentil-disease-classification
- Pigeon pea: https://www.kaggle.com/datasets/prasunroy/pigeon-pea-disease-dataset

##### C. OILSEEDS (12+ varieties)
**📂 Path**: `data/vision/universal_crops/oilseeds/`  
- Groundnut: https://www.kaggle.com/datasets/rishikeshkonapure/groundnut-disease-dataset
- Sunflower: https://www.kaggle.com/datasets/arnavr10/sunflower-disease-classification
- Mustard: https://www.kaggle.com/datasets/aryashah2k/mustard-disease-dataset

##### D. SPICES (20+ varieties)
**📂 Path**: `data/vision/universal_crops/spices/`
- Turmeric: https://www.kaggle.com/datasets/aryashah2k/turmeric-leaf-disease-dataset  
- Chili: https://www.kaggle.com/datasets/arshid/chilli-leaf-disease-detection
- Coriander: https://www.kaggle.com/datasets/aman2000jaiswal/coriander-disease-dataset

##### E. FRUITS (25+ varieties)
**📂 Path**: `data/vision/universal_crops/fruits/`
- Mango: https://www.kaggle.com/datasets/aryashah2k/mango-leaf-disease-dataset
- Citrus: https://www.kaggle.com/datasets/jonathansilva2020/citrus-diseases  
- Grapes: https://www.kaggle.com/datasets/rm1000/grape-disease-dataset-original
- Apple: https://www.kaggle.com/datasets/rashikrahmanpritom/apple-disease-dataset

##### F. VEGETABLES (30+ varieties)
**📂 Path**: `data/vision/universal_crops/vegetables/`
- Tomato: https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf
- Potato: https://www.kaggle.com/datasets/arjuntejaswi/plant-village
- Onion: https://www.kaggle.com/datasets/aman2000jaiswal/onion-disease-dataset
- Cabbage: https://www.kaggle.com/datasets/abdallahalidev/cabbage-disease-classification

##### G. PLANTATION CROPS (8+ varieties)
**📂 Path**: `data/vision/universal_crops/plantation/`
- Tea: https://www.kaggle.com/datasets/shashwatwork/tea-leaf-disease-dataset
- Coffee: https://www.kaggle.com/datasets/alvarole/coffee-leaves-disease
- Rubber: https://www.kaggle.com/datasets/aman2000jaiswal/rubber-tree-disease-dataset

### 🟡 Important India-Specific Sources

#### 4. ICAR/KVK Agricultural Bulletins (~800MB)
**📥 Sources**: http://www.icar.org.in/, State Agricultural Universities
**📂 Extract to**: `data/vision/icar_images/`

#### 5. Plantix App Research Data
**📥 Source**: Research papers and taxonomy data
**📂 Extract to**: `data/vision/plantix_research/`
**🔧 Use Cases**: Disease taxonomy alignment, benchmarking

### 🟢 Nice-to-Have Advanced Sources

#### 6. Roboflow Agricultural Datasets
**📥 Source**: https://roboflow.com/datasets?q=agriculture
**📂 Extract to**: `data/vision/roboflow/`
**🔧 Use Cases**: Pre-processed YOLO-ready detection datasets

#### 7. Community-Sourced Farmer Images
**📂 Store in**: `data/vision/community/`
**🔧 Use Cases**: WhatsApp groups, KVK submissions (with consent)

#### 8. Synthetic Data Generation
**📂 Store in**: `data/vision/synthetic/`
**🔧 Use Cases**: GANs, dirt overlays, multi-disease leaves

---

## 🎤 B. SPEECH MODEL DATASETS

### 🔴 Must-Have (Priority: High)

#### 1. Mozilla Common Voice (Indic Languages) (~15GB, ~200 hours)
**📥 Source**: https://commonvoice.mozilla.org/datasets
**📂 Extract to**: `data/speech/common_voice/`

#### 2. OpenSLR Indic Speech Corpora (~8GB, ~150 hours)
**📥 Sources**: 
- SLR63: Hindi (http://openslr.org/63/)
- SLR64: Tamil (http://openslr.org/64/)
- SLR65: Telugu (http://openslr.org/65/)
- SLR78: Marathi (http://openslr.org/78/)

**📂 Extract to**: `data/speech/openslr/`

### 🟡 Important Field-Specific Sources

#### 3. mKisan/Kisan Call Center Transcripts (~2GB)
**📥 Source**: mKisan portal, Kisan Call Center archives
**📂 Extract to**: `data/speech/mkisan/`
**🔧 Use Cases**: Authentic farmer queries, phrasing, dialects

#### 4. AI4Bharat IndicSpeech/TTS Corpora (~5GB)
**📥 Source**: https://github.com/AI4Bharat/IndicSpeech
**📂 Extract to**: `data/speech/ai4bharat/`
**🔧 Use Cases**: High-quality TTS voice generation

### 🟢 Nice-to-Have Enhancement Sources

#### 5. Field Recordings & Farmer Queries
**📂 Store in**: `data/speech/field_recordings/`

#### 6. Noisy Environment Augmentation
**📂 Store in**: `data/speech/noise_augmentation/`
**🔧 Use Cases**: Farm sounds, tractors, birds, wind for robustness

---

## 💬 C. TEXT/QA MODEL DATASETS

### 🔴 Must-Have (Priority: High)

#### 1. ICAR/KVK Publications (~500MB text, ~2,000 documents)
**📥 Sources**: http://www.icar.org.in/, Pest advisories, Seasonal calendars
**📂 Extract to**: `data/text_qa/icar_advisories/`

#### 2. Agmarknet/eNAM Market Data (~200MB)
**📥 Sources**: https://agmarknet.gov.in/, https://enam.gov.in/
**📂 Extract to**: `data/text_qa/market_data/`

#### 3. mKisan/Farmer Portal Advisories
**📥 Source**: mKisan portal SMS archives
**📂 Extract to**: `data/text_qa/mkisan/`
**🔧 Use Cases**: SMS archives, push messages, concise advisory format

#### 4. MS MARCO Q&A Dataset (Agriculture-filtered) (~100MB)
**📥 Source**: https://huggingface.co/datasets/microsoft/ms_marco
**📂 Extract to**: `data/text_qa/ms_marco_filtered/`
**🔧 Use Cases**: Conversational diversity, question patterns

### 🟡 Important Multilingual Sources

#### 5. Indic NLP Corpora (AI4Bharat, IndicCorp) (~2GB)
**📥 Source**: https://github.com/AI4Bharat/IndicBERT
**📂 Extract to**: `data/text_qa/indic_nlp/`
**🔧 Use Cases**: Multilingual context, transliteration, code-mixing

#### 6. Wikipedia Dumps (Indic Languages)
**📂 Extract to**: `data/text_qa/wikipedia/`
**🔧 Use Cases**: Agricultural articles in Indian languages

#### 7. State Agricultural University Bulletins
**📂 Extract to**: `data/text_qa/state_universities/`
**🔧 Use Cases**: Regional best practices, local crop varieties

### 🟢 Nice-to-Have Enhancement Sources

#### 8. Multilingual Agricultural Corpus
**📂 Store in**: `data/text_qa/multilingual_corpus/`

#### 9. Agricultural Forums & Community Data
**📂 Store in**: `data/text_qa/community_forums/`
**🔧 Use Cases**: Farmer forums, Q&A platforms, social media

#### 10. Research Papers & Scientific Literature
**📂 Store in**: `data/text_qa/research_papers/`
**🔧 Use Cases**: Scientific agricultural knowledge, latest research

---

## 🌐 D. TRANSLATION MODEL DATASETS

### 🔴 Must-Have (Priority: High)

#### 1. NLLB-200-600M (HuggingFace) (~1.2GB)
**📥 Source**: facebook/nllb-200-600M
**📂 Store in**: `data/translation/models/`
**🔧 Setup**: Download via HuggingFace transformers

### 🟡 Domain Adaptation Sources

#### 2. AI4Bharat IndicTrans Parallel Corpora (~800MB)
**📥 Source**: https://github.com/AI4Bharat/indictrans
**📂 Extract to**: `data/translation/parallel_corpora/indictrans/`

#### 3. OPUS/FLORES-200 Multilingual Corpora
**📥 Sources**: https://opus.nlpl.eu/, https://github.com/facebookresearch/flores
**📂 Extract to**: `data/translation/parallel_corpora/`

#### 4. Government Bilingual Advisories (~300MB)
**📂 Store in**: `data/translation/domain_specific/`

### 🟢 Nice-to-Have Enhancement Sources

#### 5. Custom Agricultural Parallel Corpus
**📂 Store in**: `data/translation/custom_parallel/`
**🔧 Use Cases**: Domain-specific translation pairs

#### 6. Code-Mixed Data
**📂 Store in**: `data/translation/code_mixed/`
**🔧 Use Cases**: Hinglish and other mixed language scenarios

#### 7. Regional Language Variants
**📂 Store in**: `data/translation/regional_variants/`
**🔧 Use Cases**: Dialect-specific translations

---

## 📈 E. MARKET FORECASTING DATASETS

### 🔴 Must-Have (Priority: High)

#### 1. Agmarknet Historical Prices (~2GB, ~10M records)
**📥 Source**: https://agmarknet.gov.in/
**📂 Extract to**: `data/market/agmarknet/`

#### 2. eNAM Real-time Trade Data (~500MB + streaming)
**📥 Source**: https://enam.gov.in/
**📂 Extract to**: `data/market/enam/`

#### 3. Weather Data (IMD) (~1GB)
**📥 Source**: https://mausam.imd.gov.in/
**📂 Extract to**: `data/market/weather/`

#### 4. Yield Data (~200MB)
**📥 Sources**: https://www.fao.org/faostat/, https://agricoop.nic.in/
**📂 Extract to**: `data/market/yield_data/`

### 🟡 Important India-Specific Sources

#### 5. State Agricultural Market Boards
**📂 Extract to**: `data/market/state_boards/`
**🔧 Examples**: Gujarat Agricultural Marketing Board, Maharashtra APMC

#### 6. NABARD/NITI Aayog Agricultural Reports
**📂 Extract to**: `data/market/policy_reports/`
**🔧 Use Cases**: Demand trends, consumption patterns

### 🟢 Nice-to-Have Enhancement Sources

#### 7. Kaggle Agricultural Commodity Price Datasets
**📂 Extract to**: `data/market/kaggle_prices/`
**🔧 Use Cases**: Cleaned CSVs based on Agmarknet

#### 8. World Bank & IFPRI Food Price Datasets
**📂 Extract to**: `data/market/international/`
**🔧 Use Cases**: International trends for comparison

#### 9. Commodity Exchange Data
**📂 Extract to**: `data/market/commodity_exchanges/`
**🔧 Use Cases**: NCDEX, MCX futures data

#### 10. Supply Chain & Logistics Data
**📂 Extract to**: `data/market/supply_chain/`
**🔧 Use Cases**: Transportation costs, storage data

---

## 📋 COMPLETE DATASET COLLECTION CHECKLIST

### Week 1: Foundation Datasets (Days 8-10) - 🔴 Must-Have
- [ ] **Vision**: Download PlantVillage → `data/vision/plantvillage/raw/`
- [ ] **Vision**: Download PlantDoc → `data/vision/plantdoc/`
- [ ] **Vision**: Download crop-specific datasets → `data/vision/crop_specific/`
- [ ] **Speech**: Setup Mozilla Common Voice (5 languages) → `data/speech/common_voice/`
- [ ] **Speech**: Download OpenSLR corpora → `data/speech/openslr/`
- [ ] **Text**: Collect ICAR publications (top 100) → `data/text_qa/icar_advisories/`
- [ ] **Text**: Setup Agmarknet market data → `data/text_qa/market_data/`
- [ ] **Translation**: Download NLLB model → `data/translation/models/`
- [ ] **Market**: Setup Agmarknet API (1 year) → `data/market/agmarknet/`
- [ ] **Market**: Download weather data → `data/market/weather/`

### Week 2: Enhancement & Processing (Days 11-14) - 🟡 Important
- [ ] **Vision**: Add ICAR images → `data/vision/icar_images/`
- [ ] **Vision**: Add Plantix research data → `data/vision/plantix_research/`
- [ ] **Speech**: Add mKisan transcripts → `data/speech/mkisan/`
- [ ] **Speech**: Add AI4Bharat corpora → `data/speech/ai4bharat/`
- [ ] **Text**: Add mKisan advisories → `data/text_qa/mkisan/`
- [ ] **Text**: Filter MS MARCO → `data/text_qa/ms_marco_filtered/`
- [ ] **Text**: Add Indic NLP corpora → `data/text_qa/indic_nlp/`
- [ ] **Translation**: Add IndicTrans → `data/translation/parallel_corpora/indictrans/`
- [ ] **Translation**: Add OPUS/FLORES → `data/translation/parallel_corpora/`
- [ ] **Market**: Add eNAM data → `data/market/enam/`
- [ ] **Market**: Add yield data → `data/market/yield_data/`

### Week 3: Advanced Sources (Days 15-21) - 🟢 Nice-to-Have
- [ ] **Vision**: Add Roboflow datasets → `data/vision/roboflow/`
- [ ] **Vision**: Setup community collection → `data/vision/community/`
- [ ] **Speech**: Setup field recordings → `data/speech/field_recordings/`
- [ ] **Speech**: Add noise augmentation → `data/speech/noise_augmentation/`
- [ ] **Text**: Add Wikipedia dumps → `data/text_qa/wikipedia/`
- [ ] **Text**: Add state university bulletins → `data/text_qa/state_universities/`
- [ ] **Text**: Setup community forums → `data/text_qa/community_forums/`
- [ ] **Translation**: Add custom parallel corpus → `data/translation/custom_parallel/`
- [ ] **Translation**: Add code-mixed data → `data/translation/code_mixed/`
- [ ] **Market**: Add state boards data → `data/market/state_boards/`
- [ ] **Market**: Add international data → `data/market/international/`

---

## 🚀 QUICK SETUP COMMANDS

### 1. Install Kaggle API
```powershell
# Navigate to project directory
cd D:\SIH\farmer-ai-system

# Install required packages
python scripts\install_kaggle.py

# Setup Kaggle authentication
python scripts\setup_kaggle_auth.py
```

### 2. Quick Start - Download PlantVillage (Your Code!)
```python
# Your exact code - now enhanced with organization
import kagglehub

# Download latest version
path = kagglehub.dataset_download("abdallahalidev/plantvillage-dataset")
print("Path to dataset files:", path)

# Run the enhanced version:
python scripts\quick_start_datasets.py
```

### 3. Automated Dataset Downloads (Kaggle API)
```python
# All vision datasets
python scripts\download_datasets.py  # Choose option 2

# All datasets at once
python scripts\download_datasets.py  # Choose option 1
```

### 4. Individual Kaggle Dataset Commands
```python
# Vision datasets - Using kagglehub (like your code)
import kagglehub

# PlantVillage (your original request)
path = kagglehub.dataset_download("abdallahalidev/plantvillage-dataset")

# PlantDoc with bounding boxes
path = kagglehub.dataset_download("pratikdaigavane/plantdoc-dataset")

# Additional crop diseases
path = kagglehub.dataset_download("vipoooool/new-plant-diseases-dataset")

# Rice leaf diseases
path = kagglehub.dataset_download("vbookshelf/rice-leaf-diseases")

# Tomato leaf disease
path = kagglehub.dataset_download("kaustubhb999/tomatoleaf")

# Wheat disease detection
path = kagglehub.dataset_download("olyadanylenko/wheat-leaf-disease-detection")

# Text/Market datasets
path = kagglehub.dataset_download("atharvaingle/crop-recommendation-dataset")
path = kagglehub.dataset_download("srinivas1/agricuture-crops-production-in-india")
```

### 5. Manual Downloads (Non-Kaggle)
```bash
# Speech datasets (Mozilla Common Voice)
# Visit: https://commonvoice.mozilla.org/datasets
# Download Hindi, Bengali, Tamil, Telugu, Gujarati

# ICAR Publications
# Visit: http://www.icar.org.in/
# Download agricultural advisories and bulletins

# Weather Data (IMD)
# Visit: https://mausam.imd.gov.in/
# Download historical weather data
```

### 6. Verify Downloads
```powershell
# Check directory structure
tree data /F

# Run verification script
python scripts\verify_datasets.py
```

---

## 💾 COMPLETE STORAGE REQUIREMENTS

| Dataset Category | Must-Have | Important | Nice-to-Have | Total |
|------------------|-----------|-----------|--------------|-------|
| **Vision** | ~5GB | ~3GB | ~2GB | **~10GB** |
| **Speech** | ~23GB | ~7GB | ~5GB | **~35GB** |
| **Text/QA** | ~1GB | ~3GB | ~2GB | **~6GB** |
| **Translation** | ~1GB | ~1GB | ~0.5GB | **~2.5GB** |
| **Market** | ~3GB | ~2GB | ~1GB | **~6GB** |
| **GRAND TOTAL** | **~33GB** | **~16GB** | **~10.5GB** | **~59.5GB** |

### Priority-Based Collection Strategy
- **Phase 1**: Must-Have only (~33GB) - Core functionality
- **Phase 2**: Must-Have + Important (~49GB) - Production quality  
- **Phase 3**: All datasets (~59.5GB) - Research & enhancement

---

## 🎯 SUCCESS METRICS BY PRIORITY

### 🔴 Must-Have Targets
- **Vision**: >90% accuracy on PlantVillage test set
- **Speech**: <10% WER on Common Voice validation
- **Text/QA**: >85% expert approval on ICAR Q&A pairs
- **Translation**: >20 BLEU score on FLORES-200
- **Market**: >90% data completeness on Agmarknet

### 🟡 Important Targets  
- **Vision**: >93% accuracy with India-specific data
- **Speech**: <7% WER with regional accents
- **Text/QA**: >88% expert approval with multilingual
- **Translation**: >23 BLEU score with domain adaptation
- **Market**: >93% completeness with multi-source data

### 🟢 Nice-to-Have Targets
- **Vision**: >95% accuracy with synthetic augmentation
- **Speech**: <5% WER in noisy environments
- **Text/QA**: >90% approval with community validation
- **Translation**: >25 BLEU with code-mixing support
- **Market**: >95% completeness with international correlation

---

## 🗂️ FINAL DIRECTORY STRUCTURE

```
D:\SIH\farmer-ai-system\data\
├── vision/
│   ├── plantvillage/               # 🔴 PlantVillage dataset (single folder)
│   ├── plantdoc/                   # 🔴 PlantDoc with annotations (single folder)
│   ├── icar_images/                # 🟡 ICAR extracted images (single folder)
│   ├── plantix_research/           # 🟡 Plantix taxonomy data (single folder)
│   ├── roboflow/                   # 🟢 Roboflow datasets (single folder)
│   ├── community/                  # 🟢 Community-sourced images (single folder)
│   └── synthetic/                  # 🟢 Synthetic data generation (single folder)
├── speech/
│   ├── common_voice/               # 🔴 Mozilla Common Voice (single folder)
│   ├── openslr/                    # 🔴 OpenSLR Indic corpora (single folder)
│   ├── mkisan/                     # 🟡 mKisan call transcripts (single folder)
│   ├── ai4bharat/                  # 🟡 AI4Bharat speech data (single folder)
│   ├── field_recordings/           # 🟢 Real farmer recordings (single folder)
│   └── noise_augmentation/         # 🟢 Environmental noise (single folder)
├── text_qa/
│   ├── icar_advisories/            # 🔴 ICAR publications (single folder)
│   ├── market_data/                # 🔴 Market advisory texts (single folder)
│   ├── mkisan/                     # 🔴 mKisan SMS archives (single folder)
│   ├── ms_marco_filtered/          # 🔴 Filtered MS MARCO (single folder)
│   ├── indic_nlp/                  # 🟡 AI4Bharat Indic corpora (single folder)
│   ├── wikipedia/                  # 🟡 Wikipedia agricultural articles (single folder)
│   ├── state_universities/         # 🟡 State university bulletins (single folder)
│   ├── multilingual_corpus/        # 🟢 Multilingual Q&A pairs (single folder)
│   ├── community_forums/           # 🟢 Farmer forums & social media (single folder)
│   └── research_papers/            # 🟢 Scientific literature (single folder)
├── translation/
│   ├── models/                     # 🔴 NLLB-600M model (single folder)
│   ├── parallel_corpora/           # 🟡 IndicTrans, OPUS, FLORES (single folder)
│   ├── domain_specific/            # 🟡 Agricultural terminology (single folder)
│   ├── custom_parallel/            # 🟢 Custom parallel corpus (single folder)
│   ├── code_mixed/                 # 🟢 Hinglish & mixed languages (single folder)
│   └── regional_variants/          # 🟢 Dialect-specific data (single folder)
└── market/
    ├── agmarknet/                  # 🔴 Historical price data (single folder)
    ├── enam/                       # 🔴 Real-time trade data (single folder)
    ├── weather/                    # 🔴 IMD weather data (single folder)
    ├── yield_data/                 # 🔴 FAO & ministry yield data (single folder)
    ├── state_boards/               # 🟡 State market board data (single folder)
    ├── policy_reports/             # 🟡 NABARD/NITI reports (single folder)
    ├── kaggle_prices/              # 🟢 Kaggle price datasets (single folder)
    ├── international/              # 🟢 World Bank & IFPRI data (single folder)
    ├── commodity_exchanges/        # 🟢 NCDEX, MCX futures (single folder)
    └── supply_chain/               # 🟢 Logistics & transportation (single folder)

---

## 📦 F. ADDITIONAL CRITICAL DATASETS

### 🔴 Must-Have Market & Vision Enhancements

#### 1. ICRISAT Crop Yield Statistics (~500MB)
**📥 Source**: ICRISAT (International Crops Research Institute for the Semi-Arid Tropics)
**📂 Extract to**: `data/market/crop_yield_icrisat/`
**🔧 Content**: Regional crop yield statistics for Indian staples
- Detailed data on millets, pulses, sorghum, groundnut, cotton
- Long-term yield trends correlation with climate & soil data
- Market forecasting enhancement data

#### 2. State Mandi Reports (~1GB)
**📥 Sources**: State agriculture marketing boards (Maharashtra, Gujarat, Karnataka)
**📂 Extract to**: `data/market/state_mandi_reports/`
**🔧 Content**: Regional mandi price bulletins and crop arrival data
- District-level price fluctuations
- Local market dynamics
- Improved farmer-level price prediction accuracy

#### 3. IARI Disease Image Collection (~2GB)
**📥 Source**: Indian Agricultural Research Institute (IARI)
**📂 Extract to**: `data/vision/iari_disease_images/`
**🔧 Content**: Field images of India-specific crop diseases
- Rice blast, cotton wilt, pulse rust, sugarcane red rot
- Authentic field-condition Indian datasets
- Real-world conditions with dust, mixed leaves, soil background

### 🟡 Important Speech & Text Enhancements

#### 4. Bhashini Speech Corpora (~3GB)
**📥 Source**: Government of India's National Language Translation Mission
**📂 Extract to**: `data/speech/bhashini/`
**🔧 Content**: Comprehensive Indic speech corpora
- Multiple languages: Hindi, Tamil, Telugu, Marathi, Bengali
- Standardized speech recognition and synthesis data
- Official Indian accent coverage

#### 5. mKisan SMS Archive (~200MB)
**📥 Source**: mKisan Portal (Government SMS advisory system)
**📂 Extract to**: `data/text_qa/mkisan_sms_archive/`
**🔧 Content**: Farmer-submitted queries and advisory messages
- Hindi/English code-mixed format
- Real farmer query patterns
- Context-rich agricultural communications

### 🟡 Important Translation Enhancement

#### 6. Government Bilingual Advisories (~500MB)
**📥 Source**: ICAR/KVK weekly/monthly bulletins
**📂 Extract to**: `data/translation/govt_bilingual_advisories/`
**🔧 Content**: Parallel Hindi-English agricultural texts
- Crop practices documentation
- Disease control advisories
- Input use guidelines
- High-quality domain-specific parallel corpus

---
```

---

ADD ON DATASETS:-

1.market/crop_yield_icrisat

Source: ICRISAT
 (International Crops Research Institute for the Semi-Arid Tropics)

Content: Regional crop yield statistics for Indian staples (millets, pulses, sorghum, groundnut, cotton).

Why Important: Provides long-term yield trends, helping correlate productivity with climate, soil, and market data. Strengthens forecasting beyond just prices.

2. market/state_mandi_reports

Source: State agriculture marketing boards (e.g., Maharashtra, Gujarat, Karnataka)

Content: Regional mandi price bulletins and crop arrival data.

Why Important: Adds granularity missing in Agmarknet, capturing local market fluctuations at the district level. Improves farmer-level price prediction accuracy.

3. vision/iari_disease_images

Source: IARI
 (Indian Agricultural Research Institute) disease research datasets.

Content: Field images of India-specific crop diseases (rice blast, cotton wilt, pulse rust, sugarcane red rot).

Why Important: Provides authentic, field-condition Indian datasets (dust, mixed leaves, soil background), closing the gap between clean global datasets (PlantVillage) and Indian farm reality.

4. speech/bhashini

Source: Bhashini
 (Government of India’s National Language Translation Mission)

Content: Indic speech corpora (Hindi, Tamil, Telugu, Marathi, Bengali, etc.) for ASR/TTS.

Why Important: Official, standardized dataset that ensures speech models cover Indian accents and languages, aligning with Digital India initiatives.

5. text_qa/mkisan_sms_archive

Source: mKisan Portal
 (Government SMS advisory system)

Content: Farmer-submitted queries and advisory messages in Hindi/English code-mixed format.

Why Important: Directly reflects real farmer queries — short, code-mixed, context-rich. Enables training of QA models to respond in farmer-style communication.

6. translation/govt_bilingual_advisories

Source: ICAR/KVK advisories (weekly/monthly bulletins)

Content: Parallel Hindi-English texts on crop practices, disease control, input use.

Why Important: Serves as high-quality domain-specific parallel corpus, strengthening Indic translation models for agriculture.


✅ Datasets That Need Filtration
🌱 Vision

Universal Crop Datasets (all cereals, pulses, oilseeds, spices, fruits, vegetables, plantation crops)
🔎 Issue: Many Kaggle sets include global crop species, duplicate classes, and inconsistent labeling.
👉 Action: Filter for Indian crops + merge only relevant disease categories.

PlantDoc Dataset (~2.5k images)
🔎 Issue: Mixed annotation quality, sometimes irrelevant leaves/non-leaf objects.
👉 Action: Keep only properly annotated images.

ICAR Images & Plantix Research
🔎 Issue: Semi-structured research images, not directly ML-ready.
👉 Action: Manually curate per crop/disease.

Community-Sourced Farmer Images
🔎 Issue: High noise (random background, duplicate photos, low resolution).
👉 Action: Strict filtering for usable, labeled samples.

Synthetic Data Generation
🔎 Issue: GAN overlays may create unrealistic artifacts.
👉 Action: Keep only validated synthetic samples.

🎤 Speech

Mozilla Common Voice (Indic)
🔎 Issue: Contains non-agriculture sentences, urban phrasing, noisy accents.
👉 Action: Filter for agricultural vocab + clean noisy samples.

OpenSLR Indic Speech Corpora
🔎 Issue: General-purpose corpora, not agriculture-specific.
👉 Action: Extract agriculturally relevant conversations.

mKisan Call Center Transcripts
🔎 Issue: Raw transcripts have spelling mistakes, repetition, personal info.
👉 Action: Filter for query–response format only.

Bhashini Speech Corpora
🔎 Issue: Very broad coverage (all domains).
👉 Action: Select agriculture-related utterances only.

Field Recordings
🔎 Issue: Noisy, overlapping speech, background farm sounds.
👉 Action: Label clean vs noisy, use noise as augmentation separately.

💬 Text/QA

MS MARCO Q&A (Agriculture-filtered)
🔎 Issue: Base dataset is generic web queries.
👉 Action: Keep only agriculture-related Q&A.

Indic NLP Corpora
🔎 Issue: General language corpus (news, Wikipedia, stories).
👉 Action: Extract agriculture + rural domain terms.

Wikipedia Dumps (Indic languages)
🔎 Issue: Contains entire Wikipedia, not just agriculture.
👉 Action: Filter to agri-related articles.

Community Forums & Social Media
🔎 Issue: Highly noisy, mixed language, irrelevant chatter.
👉 Action: Strict curation (farmer Q&A only).

mKisan SMS Archive
🔎 Issue: SMS messages may have duplicates, broken Hindi-English transliteration.
👉 Action: Normalize text, remove spam.

🌐 Translation

OPUS/FLORES-200
🔎 Issue: Global-domain corpora.
👉 Action: Extract agriculture-related translations only.

AI4Bharat IndicTrans
🔎 Issue: General-purpose parallel corpora.
👉 Action: Filter for domain-specific agriculture advisories.

Govt. Bilingual Advisories
🔎 Issue: Mixed formats (bulletins, tables, scans).
👉 Action: Convert to clean parallel text pairs.

Code-Mixed Data
🔎 Issue: Hinglish can be very informal, noisy.
👉 Action: Keep only agriculturally relevant utterances.

📈 Market

State Mandi Reports
🔎 Issue: Often in PDFs, scanned images, inconsistent formats.
👉 Action: OCR + structure data into clean CSV.

State Boards / NABARD Reports
🔎 Issue: Long PDF policy docs with irrelevant narrative.
👉 Action: Extract tabular + numeric sections only.

Kaggle Price Datasets
🔎 Issue: Many duplicates of Agmarknet, some synthetic.
👉 Action: Remove redundant datasets.

Supply Chain & Logistics Data
🔎 Issue: Often messy, partial, incomplete.
👉 Action: Normalize & deduplicate records.

🚦 Quick Rule of Thumb

Already Clean (no filtration needed) → PlantVillage, NLLB-200, Agmarknet, eNAM, IMD Weather, FAO Yield.

Needs Filtration → Universal crops, speech corpora, text corpora, translation corpora, state reports, community/synthetic sources.