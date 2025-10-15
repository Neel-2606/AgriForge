# 🇮🇳 KrishiMitra AI - India-Focused Dataset Guide (Practical Edition)
**Smart India Hackathon 2025 - Compact, Research-Backed, Training-Ready**

---

## 📋 Executive Summary

**Goal**: Replace global/generic datasets with **Indian research sources** while keeping total storage ≤ 50–60 GB.

**Core Principle**: 100% India-first, IIT/AI4Bharat-anchored, government-aligned, practical for SIH timeline.

**Target Models**: Whisper (STT), TinyLlama (Q&A), NLLB (Translation), EfficientNet (Vision), Prophet/XGB/LSTM (Market)

**Languages**: All 10 target languages - Hindi (hi), Bengali (bn), Marathi (mr), Telugu (te), Tamil (ta), Gujarati (gu), Urdu (ur), Kannada (kn), Odia (or), Malayalam (ml)

---

## 📁 Directory Structure
```
D:\SIH\farmer-ai-system\data\
├── vision/          # Indian field images (IARI/PlantDoc/SAU)
├── speech/          # IndicVoices + OpenSLR + Bhashini (compact)
├── text_qa/         # ICAR + SAU + mKisan (Q&A ready)
├── translation/     # IndicTrans2 + Govt bilingual
└── market/          # Agmarknet + IMD + ICRISAT (India-only)
```

---

## 🔍 A. VISION MODEL DATASETS (India-First, ≤8 GB)

### 🔴 Must-Have (≤6 GB)

#### 1. PlantDoc Dataset - Indian Research (~500 MB)
**📥 Source**: https://github.com/pratikkayal/PlantDoc-Dataset  
**Research**: ACM India Conference paper, Indian field conditions  
**📂 Extract to**: `data/vision/plantdoc/`

**Content**:
- 2,598 images across 13 plant species
- 27 disease classes with bounding boxes
- Real field images (not lab-controlled)
- Includes Indian crops: tomato, potato, bell pepper, etc.

**Processing**:
- Convert annotations to YOLO format
- Filter for Indian-relevant crops only
- Split: 70% train, 15% val, 15% test

---

#### 2. ICAR-IARI Field Disease Images (Request-based, ~2 GB)
**📥 Source**: Contact ICAR-IARI research divisions  
**Email Template**: Available in guide  
**📂 Extract to**: `data/vision/iari_india/`

**Target Crops** (prioritize these):
- Rice: blast, brown spot, bacterial blight
- Wheat: rust (yellow, brown, black)
- Cotton: wilt, boll worm damage
- Pulses: rust, wilt, blight
- Sugarcane: red rot, smut

**Why Critical**: Authentic Indian field conditions (dust, mixed backgrounds, multiple diseases)

---

#### 3. Compact Indian Crop Datasets from Kaggle (~3 GB)
**📂 Extract to**: `data/vision/indian_crops/`

**Priority Downloads** (India-relevant only):
- Rice: https://www.kaggle.com/datasets/vbookshelf/rice-leaf-diseases (~500 MB)
- Wheat: https://www.kaggle.com/datasets/olyadanylenko/wheat-leaf-disease-detection (~300 MB)
- Millets: https://www.kaggle.com/datasets/aman2000jaiswal/millet-crop-disease-detection (~200 MB)
- Chickpea: https://www.kaggle.com/datasets/nirmalsankalana/chickpea-leaf-disease-dataset (~150 MB)
- Groundnut: https://www.kaggle.com/datasets/rishikeshkonapure/groundnut-disease-dataset (~200 MB)
- Turmeric: https://www.kaggle.com/datasets/aryashah2k/turmeric-leaf-disease-dataset (~150 MB)
- Chili: https://www.kaggle.com/datasets/arshid/chilli-leaf-disease-detection (~200 MB)
- Mango: https://www.kaggle.com/datasets/aryashah2k/mango-leaf-disease-dataset (~150 MB)
- Tea: https://www.kaggle.com/datasets/shashwatwork/tea-leaf-disease-dataset (~200 MB)
- Cotton: Search "cotton disease India" on Kaggle (~300 MB)

**Action**: Download only these 10 crops; skip global crops (apple, grape, etc.)

---

#### 4. SAU Image Bulletins (PDF extraction, ~500 MB)
**📥 Sources**: TNAU, PAU, UAS websites  
**📂 Extract to**: `data/vision/sau_bulletins/`

**Method**:
- Download regional crop advisory PDFs (50-100 PDFs)
- Extract disease images using PDF tools
- Manual curation per crop/disease
- Label with crop + disease + region metadata

---

### 🟡 Optional Transfer Learning Base (~2 GB)
**📂 Extract to**: `data/vision/transfer_base/`

**Use**: Only if you need pre-trained feature extraction bootstrap

**Source**: Small PlantVillage subset (tomato, potato, rice, wheat only - ~2 GB)

---

## 🎤 B. SPEECH MODEL DATASETS (India-Only, All 10 Languages, ≤22 GB)

### 🔴 Must-Have (≤10 GB)

#### 1. AI4Bharat IndicVoices (All 10 Languages, ~15-18 GB)
**📥 Source**: https://huggingface.co/datasets/ai4bharat/indicvoices_r  
**Research**: IIT Madras AI4Bharat Initiative  
**📂 Extract to**: `data/speech/indicvoices/`

**Download Strategy** (language-by-language, all 10 target languages):
- Hindi (hi): 2.0 GB (~40-50 hours)
- Bengali (bn): 1.5 GB (~30-35 hours)
- Marathi (mr): 1.5 GB (~30-35 hours)
- Telugu (te): 1.5 GB (~30-35 hours)
- Tamil (ta): 1.5 GB (~30-35 hours)
- Gujarati (gu): 1.5 GB (~30-35 hours)
- Urdu (ur): 1.5 GB (~30-35 hours)
- Kannada (kn): 1.5 GB (~30-35 hours)
- Odia (or): 1.2 GB (~25-30 hours)
- Malayalam (ml): 1.2 GB (~25-30 hours)

**Total**: ~15-18 GB for all 10 languages

**Processing**:
- Downsample to 16kHz mono
- VAD-based silence trimming
- Stratified train/dev/test splits per language
- Keep extempore speech (76% of dataset - most natural)

**Why This Over Common Voice**:
- 22,563 speakers from 208 Indian districts
- Natural, spontaneous speech (76% extempore)
- Covers all 22 Constitutional languages
- IIT Madras research-backed

---

#### 2. OpenSLR Indic Speech (Compact, ~3-4 GB)
**📥 Sources**:  
- SLR63: Hindi - http://openslr.org/63/
- SLR64: Tamil - http://openslr.org/64/
- SLR65: Telugu - http://openslr.org/65/
- SLR78: Marathi - http://openslr.org/78/
- SLR79: Gujarati - http://openslr.org/78/ (check for Gujarati)
- Additional Indic languages as available on OpenSLR

**📂 Extract to**: `data/speech/openslr_compact/`

**Download**: 25-50 hours per available language (~500-700 MB each)

**Note**: OpenSLR has limited coverage for Urdu, Kannada, Odia, Malayalam. IndicVoices will be primary source for these.

**Processing**:
- Convert to 16kHz mono WAV
- Align transcripts with audio
- Quality filter based on SNR

---

#### 3. Bhashini/ULCA Sample Packs (~1-2 GB)
**📥 Source**: https://bhashini.gov.in/ (ULCA platform)  
**Government**: Ministry of Electronics & IT  
**📂 Extract to**: `data/speech/bhashini_sample/`

**Content**:
- Small STT/TTS model packs for Indian languages
- Government-standard language datasets
- Agriculture-related utterances where available

**Access**: API-based through ULCA; request sample datasets

---

### 🟡 Domain-Specific (Add Later, ~2 GB)

#### 4. mKisan/Kisan Call Center (Request-based, ~1-2 GB)
**📥 Source**: Request from government (mKisan portal)  
**📂 Extract to**: `data/speech/mkisan_calls/`

**Content**: Real farmer queries in regional languages

**Processing**:
- Anonymize personal information
- Filter for query-response format
- Clean transcripts (spelling, repetition)

---

## 💬 C. TEXT/QA MODEL DATASETS (Training-Ready, ≤3 GB)

### 🔴 Must-Have (≤2 GB)

#### 1. ICAR KRISHI Repository (500 docs initial, ~300-500 MB)
**📥 Source**: https://krishi.icar.gov.in/  
**Government**: Indian Council of Agricultural Research  
**📂 Extract to**: `data/text_qa/icar_krishi/`

**Content**:
- Crop production packages (50+ crops)
- Pest management guidelines
- Disease control advisories
- Seasonal crop calendars
- Best agricultural practices

**Processing Pipeline** (CRITICAL):
```python
# PDF → Text → Q&A JSONL
{
  "instruction": "मेरी गेहूं की फसल में पीले धब्बे हैं, क्या करूं?",
  "response": "यह गेहूं का yellow rust हो सकता है। तुरंत Propiconazole स्प्रे करें...",
  "metadata": {
    "crop": "wheat",
    "disease": "yellow_rust",
    "region": "punjab",
    "season": "rabi",
    "language": "hi",
    "source": "ICAR_KRISHI",
    "confidence": "expert_verified"
  }
}
```

**Script**: `scripts/extract_icar_qa.py` (to be created)

---

#### 2. SAU Regional Bulletins (100-200 docs, ~200-400 MB)
**📥 Sources**:  
- TNAU: https://tnau.ac.in/ (Tamil Nadu)
- PAU: Punjab Agricultural University
- UAS: University of Agricultural Sciences, Bangalore
- ANGRAU: Andhra Pradesh

**📂 Extract to**: `data/text_qa/sau_bulletins/`

**Content**: Regional best practices, local crop varieties

---

#### 3. mKisan SMS Archive (Sample, ~100-200 MB)
**📥 Source**: mKisan portal (public SMS samples)  
**📂 Extract to**: `data/text_qa/mkisan_sms/`

**Content**:
- Farmer-submitted queries
- Hindi/English code-mixed format
- Short, actionable advice

**Processing**:
- Normalize code-mixed text (Hinglish)
- De-duplicate messages
- Anonymize personal data
- Convert to Q&A pairs

---

#### 4. Agmarknet Advisory Text (~100 MB)
**📥 Source**: https://agmarknet.gov.in/  
**📂 Extract to**: `data/text_qa/market_text/`

**Content**: Market advisory summaries, price trend explanations

---

### 🟡 Enhancement Sources (≤1 GB)

#### 5. ICRISAT Publications (Select docs, ~300 MB)
**📥 Source**: ICRISAT research papers  
**📂 Extract to**: `data/text_qa/icrisat_pubs/`

**Focus**: Dryland agriculture, millets, pulses, oilseeds

---

## 🌐 D. TRANSLATION DATASETS (Indic-First, ≤2 GB)

### 🔴 Must-Have (≤1.5 GB)

#### 1. IndicTrans2 Parallel Corpora (Subset, ~600-800 MB)
**📥 Source**: https://github.com/AI4Bharat/indictrans  
**Research**: IIT Madras AI4Bharat  
**📂 Extract to**: `data/translation/indictrans2/`

**Language Pairs** (download only these):
- English ↔ Hindi
- English ↔ Bengali
- English ↔ Tamil
- English ↔ Telugu
- English ↔ Marathi

**Processing**:
- Sentence-level alignment
- Keep agriculture-related pairs only
- Create eval sets using FLORES-200 benchmark

---

#### 2. Government Bilingual Advisories (~200-300 MB)
**📥 Source**: ICAR/KVK weekly/monthly bulletins  
**📂 Extract to**: `data/translation/govt_bilingual/`

**Content**:
- Parallel Hindi-English agricultural texts
- Crop practices documentation
- Disease control advisories
- Input use guidelines

**Processing**:
- Align sentence-level parallel pairs
- Clean OCR errors from PDFs
- Preserve domain vocabulary (crop names, diseases)

---

#### 3. NLLB-600M Base Model (Weights, ~1.2 GB)
**📥 Source**: facebook/nllb-200-600M (HuggingFace)  
**📂 Store in**: `data/translation/models/nllb_600m/`

**Setup**: Download via HuggingFace transformers

---

### 🟡 Domain-Specific (≤500 MB)

#### 4. SAU Multilingual Bulletins (~300-500 MB)
**📂 Extract to**: `data/translation/sau_multilingual/`

**Content**: Regional bulletins in local languages + English

---

## 📈 E. MARKET FORECASTING DATASETS (India-Only, ≤7 GB)

### 🔴 Must-Have (≤5 GB)

#### 1. Agmarknet Historical Prices (5 years, ~1-1.5 GB)
**📥 Source**: https://agmarknet.ceda.ashoka.edu.in/  
**Enhanced Portal**: CEDA Ashoka University  
**📂 Extract to**: `data/market/agmarknet/`

**Content**:
- Daily mandi prices (last 5 years)
- 3,000+ markets across India
- 500+ agricultural commodities
- Maximum, minimum, modal prices

**Processing**:
- Normalize to ₹/quintal or ₹/kg
- Handle missing data (holidays, strikes)
- Create time-series features (lags, moving averages)
- Add seasonal indicators (Kharif, Rabi, Zaid)

**API Access**: Available for real-time data

---

#### 2. IMD Weather Data (District-level, ~1 GB)
**📥 Source**: https://mausam.imd.gov.in/  
**Government**: India Meteorological Department  
**📂 Extract to**: `data/market/imd_weather/`

**Content**:
- District-level rainfall (daily/monthly)
- Temperature (max/min)
- Monsoon progress
- Drought/flood alerts

**Use Cases**: Weather-yield correlation, climate-aware recommendations

---

#### 3. ICRISAT District Database (Compact, ~500 MB)
**📥 Source**: http://data.icrisat.org/dld/  
**Research**: CGIAR Research Center (HQ: Hyderabad)  
**📂 Extract to**: `data/market/icrisat_district/`

**Content** (download selected crops only):
- Crop production data (area, yield, production)
- Season-wise data (Kharif, Rabi, Zaid)
- Irrigation data
- Fertilizer consumption
- Climate data (rainfall, temperature)

**Download Strategy**: Select 5-10 major crops (rice, wheat, cotton, pulses) and 10-15 states

---

#### 4. eNAM Data (Summaries/Exports, ~300-500 MB)
**📥 Source**: https://enam.gov.in/  
**Government**: National Agriculture Market  
**📂 Extract to**: `data/market/enam/`

**Content**:
- Real-time trade data from 1,000+ mandis
- Quality-based pricing
- Inter-mandi trade flows

---

### 🟡 Enhancement Sources (≤2 GB)

#### 5. State Mandi Reports (OCR to CSV, ~500 MB)
**📥 Sources**: State agriculture marketing boards  
**📂 Extract to**: `data/market/state_mandis/`

**States**: Maharashtra, Gujarat, Karnataka (prioritize)

**Processing**:
- OCR PDFs to text
- Extract tabular data to CSV
- Normalize formats

---

#### 6. NABARD/NITI Reports (Tables only, ~200 MB)
**📂 Extract to**: `data/market/policy_reports/`

**Content**: Demand trends, consumption patterns (extract tables only)

---

## 💾 PRACTICAL STORAGE BUDGET

| Category | Must-Have | Important | Total Target |
|----------|-----------|-----------|--------------|
| Vision | 6 GB | 2 GB | **8 GB** |
| Speech (10 langs) | 18 GB | 4 GB | **22 GB** |
| Text/QA | 2 GB | 1 GB | **3 GB** |
| Translation | 1.5 GB | 0.5 GB | **2 GB** |
| Market | 5 GB | 2 GB | **7 GB** |
| **TOTAL** | **32.5 GB** | **9.5 GB** | **≤42 GB** |

**Expansion to 55-60 GB**: Add Nice-to-Have sources later

---

## 📅 WEEK-BY-WEEK COLLECTION PLAN

### Week 1: Foundation (Days 8-12, ≤25 GB)

**Vision** (Day 8-9):
- [ ] Download PlantDoc → `data/vision/plantdoc/`
- [ ] Download 5 priority Indian crop datasets from Kaggle → `data/vision/indian_crops/`
- [ ] Contact IARI for field image subset (email template below)

**Speech** (Day 10):
- [ ] Download IndicVoices (all 10 languages: hi, bn, mr, te, ta, gu, ur, kn, or, ml) → `data/speech/indicvoices/`
- [ ] Download OpenSLR (hi, ta, te, mr, gu where available) → `data/speech/openslr_compact/`

**Text & Translation** (Day 11):
- [ ] Download 300 ICAR KRISHI PDFs → `data/text_qa/icar_krishi/`
- [ ] Download 100 SAU bulletins → `data/text_qa/sau_bulletins/`
- [ ] Download IndicTrans2 subsets → `data/translation/indictrans2/`
- [ ] Download NLLB weights → `data/translation/models/nllb_600m/`

**Market** (Day 12):
- [ ] Register on Agmarknet CEDA portal
- [ ] Download 5 years Agmarknet data → `data/market/agmarknet/`
- [ ] Download IMD weather (key districts) → `data/market/imd_weather/`
- [ ] Download compact ICRISAT slices → `data/market/icrisat_district/`

---

### Week 2: Enhancement (Days 13-17, ≤+10 GB)

**Vision**:
- [ ] Extract SAU images from PDFs → `data/vision/sau_bulletins/`
- [ ] Receive IARI subset (if approved) → `data/vision/iari_india/`

**Speech**:
- [ ] Download Bhashini sample packs → `data/speech/bhashini_sample/`
- [ ] Request mKisan call data (government approval)

**Text**:
- [ ] Expand ICAR collection to 500 docs
- [ ] Add mKisan SMS samples → `data/text_qa/mkisan_sms/`
- [ ] Add Agmarknet text → `data/text_qa/market_text/`

**Translation**:
- [ ] Add govt bilingual advisories → `data/translation/govt_bilingual/`

**Market**:
- [ ] Add eNAM exports → `data/market/enam/`
- [ ] Add state mandi PDFs (3 states) → `data/market/state_mandis/`

---

### Week 3: Validation (Days 18-21)

- [ ] Data quality checks (all modalities)
- [ ] Create hold-out test sets
- [ ] Metadata consistency validation
- [ ] Documentation complete
- [ ] Storage audit (confirm ≤50-60 GB)

---

## 🔗 INDIAN RESEARCH SOURCES SUMMARY

### IIT/Academic Institutions
- **AI4Bharat (IIT Madras)**: IndicVoices, IndicTrans2, IndicWav2Vec
- **PlantDoc**: ACM India Conference research
- **CEDA (Ashoka University)**: Enhanced Agmarknet portal

### Government Organizations
- **ICAR**: KRISHI repository, IARI field images
- **Bhashini/ULCA**: Ministry of Electronics & IT language datasets
- **Agmarknet**: Ministry of Agriculture mandi prices
- **IMD**: India Meteorological Department weather data
- **eNAM**: National Agriculture Market platform
- **mKisan**: Government SMS advisory system

### Research Institutes
- **ICRISAT**: District-level crop data (Hyderabad HQ)
- **IARI**: Indian Agricultural Research Institute (New Delhi)
- **SAUs**: TNAU, PAU, UAS, ANGRAU (regional expertise)

### Why No NASSCOM Datasets?
NASSCOM publishes policy reports and market analyses, not raw datasets. We use Government of India's IndiaAI/ULCA platform and IIT/AI4Bharat datasets as Indian, production-grade alternatives.

---

## 🛠️ PREPROCESSING SCRIPTS (To Be Created)

### 1. Vision Preprocessing
**Script**: `scripts/preprocess_vision.py`

```python
# Key functions:
- resize_images(224, 224)  # EfficientNet-B0
- normalize_imagenet()
- augment_data(flip=True, rotate=True, brightness=True)
- convert_to_yolo_format()  # For PlantDoc
- create_splits(train=0.7, val=0.15, test=0.15)
```

---

### 2. Text/QA Extraction
**Script**: `scripts/extract_icar_qa.py`

```python
# Pipeline:
- extract_text_from_pdf()
- segment_into_topics()
- generate_qa_pairs()  # Using GPT-4 or manual templates
- add_metadata(crop, region, season, language, source)
- save_as_jsonl()
```

---

### 3. Speech Preprocessing
**Script**: `scripts/prepare_speech_compact.py`

```python
# Key functions:
- resample_audio(16000, mono=True)
- apply_vad()  # Voice Activity Detection
- trim_silence()
- stratified_split_per_language()
- create_metadata_csv()
```

---

### 4. Translation Alignment
**Script**: `scripts/align_translation_pairs.py`

```python
# Key functions:
- sentence_align(source, target)
- clean_ocr_errors()
- preserve_domain_vocab()
- create_eval_sets()
```

---

### 5. Market Data Cleaning
**Script**: `scripts/market_clean.py`

```python
# Key functions:
- normalize_units(rupees_per_quintal=True)
- handle_missing_data(holidays=True, strikes=True)
- generate_features(lags=True, moving_avg=True, seasonal=True)
- validate_outliers()
```

---

## 📧 IARI REQUEST EMAIL TEMPLATE

```
Subject: Research Dataset Request - Smart India Hackathon 2025

Dear ICAR-IARI Research Division,

We are a team participating in Smart India Hackathon 2025 (Problem ID: SIH25076) 
developing "KrishiMitra AI", a multilingual agricultural advisory system for Indian farmers.

Dataset Requested: Field images of India-specific crop diseases
Target Crops: Rice, Wheat, Cotton, Pulses, Sugarcane
Purpose: Academic research, non-commercial, SIH competition

We commit to:
1. Academic use only for SIH 2025
2. Proper citation of ICAR-IARI in all publications
3. Share research outcomes and model results
4. Data security and privacy compliance

Project Details:
- Team: [Your Team Name]
- Institution: [Your College/University]
- Contact: [Your Email/Phone]
- Timeline: Immediate (SIH deadline: [Date])

We would be grateful for even a small curated subset (~2 GB) of field-condition 
disease images to improve our model's accuracy for Indian agricultural context.

Thank you for supporting student innovation in agriculture.

Best regards,
[Your Name]
[Team Lead, KrishiMitra AI]
[Institution]
```

---

## 🎯 SUCCESS METRICS (India-Context)

### Model Performance Targets
- **Vision**: >92% accuracy on IARI/SAU holdout (India-field conditions)
- **Speech**: <10% WER on IndicVoices eval (all 10 languages)
- **Text/QA**: >90% expert approval on ICAR-derived Q&A
- **Translation**: >28 BLEU on Indic pairs (IndicTrans2 benchmark)
- **Market**: <15% MAPE on key commodities (Agmarknet 5-year validation)

### Coverage Targets
- **Crops**: 50+ major Indian crops
- **Languages**: All 10 target languages (hi, bn, mr, te, ta, gu, ur, kn, or, ml) - 100% coverage
- **Districts**: 200+ Indian districts (via IndicVoices + ICRISAT)
- **Mandis**: 1,000+ markets (via Agmarknet + eNAM)
- **Diseases**: 100+ India-specific crop diseases
- **Speech Hours**: 300-400 hours total across all 10 languages

---

## 🗂️ FINAL DIRECTORY STRUCTURE

```
D:\SIH\farmer-ai-system\data\
├── vision/
│   ├── plantdoc/                # PlantDoc (Indian research)
│   ├── iari_india/              # ICAR-IARI field images
│   ├── indian_crops/            # Kaggle Indian crops (10 datasets)
│   ├── sau_bulletins/           # SAU PDF extractions
│   └── transfer_base/           # Optional PlantVillage subset
├── speech/
│   ├── indicvoices/             # AI4Bharat (all 10 langs: hi,bn,mr,te,ta,gu,ur,kn,or,ml)
│   ├── openslr_compact/         # OpenSLR Indic (hi,ta,te,mr,gu where available)
│   ├── bhashini_sample/         # Bhashini/ULCA packs (all 10 langs)
│   └── mkisan_calls/            # mKisan (request-based)
├── text_qa/
│   ├── icar_krishi/             # ICAR KRISHI (500 docs)
│   ├── sau_bulletins/           # SAU bulletins (100-200 docs)
│   ├── mkisan_sms/              # mKisan SMS samples
│   ├── market_text/             # Agmarknet advisories
│   └── icrisat_pubs/            # ICRISAT publications
├── translation/
│   ├── indictrans2/             # AI4Bharat parallel corpora
│   ├── govt_bilingual/          # ICAR/KVK bilingual
│   ├── sau_multilingual/        # SAU multilingual bulletins
│   └── models/nllb_600m/        # NLLB weights
└── market/
    ├── agmarknet/               # Agmarknet (5 years)
    ├── imd_weather/             # IMD weather
    ├── icrisat_district/        # ICRISAT compact
    ├── enam/                    # eNAM exports
    ├── state_mandis/            # State mandi PDFs
    └── policy_reports/          # NABARD/NITI tables
```

---

## ✅ VERIFICATION CHECKLIST

### Before Starting
- [ ] Storage space available (60 GB minimum)
- [ ] Internet bandwidth planned (5-10 Mbps recommended)
- [ ] Kaggle API credentials setup
- [ ] HuggingFace account created
- [ ] IARI/mKisan request emails sent

### During Collection
- [ ] Progress tracking sheet maintained
- [ ] Data quality spot-checks performed
- [ ] Metadata documented per dataset
- [ ] Backup copies created (external drive/cloud)

### After Collection
- [ ] Dataset completeness verified (all must-haves downloaded)
- [ ] Directory structure matches guide
- [ ] Preprocessing scripts tested
- [ ] Hold-out test sets created
- [ ] Storage audit confirms ≤50-60 GB

---

## 🚀 QUICK START COMMANDS

### Download IndicVoices (All 10 Languages)
```python
from datasets import load_dataset

# Download all 10 target languages
languages = ['hi', 'bn', 'mr', 'te', 'ta', 'gu', 'ur', 'kn', 'or', 'ml']

for lang in languages:
    print(f"Downloading {lang}...")
    dataset = load_dataset('ai4bharat/indicvoices_r', lang, split='train')
    # Save to disk
    dataset.save_to_disk(f'data/speech/indicvoices/{lang}/')
```

### Download ICRISAT Data
```bash
# Visit: http://data.icrisat.org/dld/
# Select: Crops (rice, wheat, cotton, pulses)
# Select: States (10-15 major agricultural states)
# Select: Years (2015-2024)
# Download: CSV files
```

### Access Agmarknet API
```bash
# Register at: https://agmarknet.ceda.ashoka.edu.in/
# Get API key
# Documentation: API endpoints for price data
```

### Clone IndicTrans2
```bash
git clone https://github.com/AI4Bharat/indictrans.git
cd indictrans
pip install -r requirements.txt
```

---

## 📚 KEY RESEARCH PAPERS

1. **IndicVoices**: https://arxiv.org/abs/2403.01926 (IIT Madras)
2. **IndicTrans2**: https://arxiv.org/abs/2305.16307 (AI4Bharat)
3. **PlantDoc**: ACM India Conference proceedings
4. **ICRISAT Methods**: Data documentation manual

---

**🇮🇳 100% India-Focused | 🎓 IIT/ICAR-Backed | 💾 Practical ≤60 GB | 🏆 SIH 2025 Ready**


