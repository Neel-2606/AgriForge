# 🇮🇳 AGRIFORGE AI - Complete Dataset Links Guide
**Smart India Hackathon 2025 - India-Focused, Training-Ready**

---

## 📋 EXECUTIVE SUMMARY

**Core Principle**: 100% India-first, IIT/AI4Bharat-anchored, government-aligned, practical for SIH timeline.

**Target Models**: Whisper (STT), TinyLlama (Q&A), NLLB (Translation), EfficientNet (Vision), Prophet/XGB/LSTM (Market)

**Languages**: Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Urdu, Kannada, Odia, Malayalam

**Total Storage**: ≤42 GB (Must-Have + Important)

---

## 📁 DIRECTORY STRUCTURE WITH DOWNLOAD LINKS

```
D:\SIH\farmer-ai-system\data\
├── vision/
│   ├── plantdoc/
│   ├── iari_india/
│   ├── indian_crops/
│   ├── sau_bulletins/
│   └── transfer_base/
├── speech/
│   ├── indicvoices/
│   ├── openslr_compact/
│   ├── bhashini_sample/
│   └── mkisan_calls/
├── text_qa/
│   ├── icar_krishi/
│   ├── sau_bulletins/
│   ├── mkisan_sms/
│   ├── market_text/
│   └── icrisat_pubs/
├── translation/
│   ├── indictrans2/
│   ├── govt_bilingual/
│   ├── sau_multilingual/
│   └── models/nllb_600m/
└── market/
    ├── agmarknet/
    ├── imd_weather/
    ├── icrisat_district/
    ├── enam/
    ├── state_mandis/
    └── policy_reports/
```

---

## 🔍 A. VISION MODEL DATASETS (≤8 GB)

### 📂 `data/vision/plantdoc/`
**Dataset**: PlantDoc Dataset (Indian Research)  
**📥 Download**: https://github.com/pratikkayal/PlantDoc-Dataset  
**Size**: ~500 MB  
**Content**: 2,598 images across 13 plant species, 27 disease classes with bounding boxes  
**Why This**: Real Indian field conditions, includes bounding boxes for YOLO object detection  
**Processing**: Convert annotations to YOLO format, filter for Indian-relevant crops, split 70/15/15  

---

### 📂 `data/vision/iari_india/`
**Dataset**: ICAR-IARI Field Disease Images  
**📥 Source**: Request-based from ICAR-IARI  
**Contact**: http://www.icar.org.in/  
**Size**: ~2 GB  
**Content**: Authentic Indian field images for Rice, Wheat, Cotton, Pulses, Sugarcane  

---

### 📂 `data/vision/indian_crops/`
**Dataset**: Indian Crop Disease Datasets (Kaggle)  
**Size**: ~3 GB total  
**Content**: Individual disease datasets for major Indian crops  

**Priority Downloads** (India-relevant only):
- **Rice**: https://www.kaggle.com/datasets/vbookshelf/rice-leaf-diseases (~500 MB)
- **Wheat**: https://www.kaggle.com/datasets/olyadanylenko/wheat-leaf-disease-detection (~300 MB)
- **Millets**: https://www.kaggle.com/datasets/aman2000jaiswal/millet-crop-disease-detection (~200 MB)
- **Chickpea**: https://www.kaggle.com/datasets/nirmalsankalana/chickpea-leaf-disease-dataset (~150 MB)
- **Groundnut**: https://www.kaggle.com/datasets/rishikeshkonapure/groundnut-disease-dataset (~200 MB)
- **Turmeric**: https://www.kaggle.com/datasets/aryashah2k/turmeric-leaf-disease-dataset (~150 MB)
- **Chili**: https://www.kaggle.com/datasets/arshid/chilli-leaf-disease-detection (~200 MB)
- **Mango**: https://www.kaggle.com/datasets/aryashah2k/mango-leaf-disease-dataset (~150 MB)
- **Tea**: https://www.kaggle.com/datasets/shashwatwork/tea-leaf-disease-dataset (~200 MB)
- **Tomato**: https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf (~300 MB)
- **Potato**: https://www.kaggle.com/datasets/arjuntejaswi/plant-village (~200 MB)
- **Cotton**: Search "cotton disease India" on Kaggle (~300 MB)

**Action**: Download only these Indian crops; skip global crops (apple, grape, etc.)  

---

### 📂 `data/vision/sau_bulletins/`
**Dataset**: SAU Image Bulletins (PDF Extraction)  
**📥 Sources**:
- TNAU (Tamil Nadu): https://tnau.ac.in/
- PAU (Punjab): https://www.pau.edu/
- UAS (Bangalore): https://uasbangalore.edu.in/
- ANGRAU (Andhra Pradesh): https://angrau.ac.in/

**Size**: ~500 MB  

---

### 📂 `data/vision/transfer_base/`
**Dataset**: PlantVillage Dataset (Transfer Learning Base)  
**📥 Download**: https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset  
**Size**: ~1.2 GB (use subset: tomato, potato, rice, wheat only)  
**Content**: 54,000+ images, 38 disease classes across multiple crops  
**Use**: Pre-trained feature extraction bootstrap, transfer learning base  
**Why This**: Clean, well-labeled dataset for initial model training before fine-tuning on Indian field data  

---

## 🎤 B. SPEECH MODEL DATASETS (≤22 GB)

### 📂 `data/speech/indicvoices/`
**Dataset**: AI4Bharat IndicVoices (PRIMARY SOURCE)  
**📥 Download**: https://huggingface.co/datasets/ai4bharat/indicvoices_r  
**Research**: IIT Madras AI4Bharat Initiative  
**Size**: ~15-18 GB (all 10 languages)  

**Language Coverage**:
- Hindi (hi): ~2.0 GB
- Bengali (bn): ~1.5 GB
- Marathi (mr): ~1.5 GB
- Telugu (te): ~1.5 GB
- Tamil (ta): ~1.5 GB
- Gujarati (gu): ~1.5 GB
- Urdu (ur): ~1.5 GB
- Kannada (kn): ~1.5 GB
- Odia (or): ~1.2 GB
- Malayalam (ml): ~1.2 GB
---

### 📂 `data/speech/openslr_compact/`
**Dataset**: OpenSLR Indic Speech Corpora  
**Size**: ~3-4 GB  

**Download Links by Language**:
- SLR63 (Hindi): http://openslr.org/63/
- SLR64 (Tamil): http://openslr.org/64/
- SLR65 (Telugu): http://openslr.org/65/
- SLR78 (Marathi): http://openslr.org/78/
- Additional Languages: http://openslr.org/

---

### 📂 `data/speech/bhashini_sample/`
**Dataset**: Bhashini/ULCA Sample Packs  
**📥 Source**: https://bhashini.gov.in/  
**Government**: Ministry of Electronics & IT  
**Size**: ~1-2 GB  

---

### 📂 `data/speech/mkisan_calls/`
**Dataset**: mKisan/Kisan Call Center Recordings  
**📥 Source**: https://mkisan.gov.in/  
**Size**: ~1-2 GB  
**Contact**: Kisan Call Center: 1800-180-1551

---

## 💬 C. TEXT/QA MODEL DATASETS (≤3 GB)

### 📂 `data/text_qa/icar_krishi/`
**Dataset**: ICAR KRISHI Repository  
**📥 Source**: https://krishi.icar.gov.in/  
**Government**: Indian Council of Agricultural Research  
**Size**: ~300-500 MB  

---

### 📂 `data/text_qa/sau_bulletins/`
**Dataset**: SAU Regional Bulletins  
**Size**: ~200-400 MB  

**📥 Sources**:
- TNAU: https://tnau.ac.in/
- PAU: https://www.pau.edu/
- UAS: https://uasbangalore.edu.in/
- ANGRAU: https://angrau.ac.in/

---

### 📂 `data/text_qa/mkisan_sms/`
**Dataset**: mKisan SMS Archive  
**📥 Source**: https://mkisan.gov.in/  
**Size**: ~100-200 MB  

---

### 📂 `data/text_qa/market_text/`
**Dataset**: Agmarknet Advisory Text  
**📥 Source**: https://agmarknet.gov.in/  
**Enhanced Portal**: https://agmarknet.ceda.ashoka.edu.in/  
**Size**: ~100 MB  

---

### 📂 `data/text_qa/icrisat_pubs/`
**Dataset**: ICRISAT Publications (Optional)  
**📥 Source**: https://www.icrisat.org/publications/  
**Data Portal**: http://data.icrisat.org/  
**Size**: ~300 MB  

---

## 🌐 D. TRANSLATION DATASETS (≤2 GB)

### 📂 `data/translation/indictrans2/`
**Dataset**: IndicTrans2 Parallel Corpora  
**📥 Source**: https://github.com/AI4Bharat/indictrans  
**Research**: IIT Madras AI4Bharat  
**Size**: ~600-800 MB  

---

### 📂 `data/translation/govt_bilingual/`
**Dataset**: Government Bilingual Advisories  
**📥 Source**: https://krishi.icar.gov.in/  
**Size**: ~200-300 MB  

---

### 📂 `data/translation/sau_multilingual/`
**Dataset**: SAU Multilingual Bulletins (Optional)  
**Size**: ~300-500 MB  
**📥 Sources**: Same as SAU bulletins (TNAU, PAU, UAS, ANGRAU)  

---

### 📂 `data/translation/models/nllb_600m/`
**Dataset**: NLLB-600M Base Model (Weights)  
**📥 Source**: https://huggingface.co/facebook/nllb-200-distilled-600M  
**Size**: ~1.2 GB  

---

## 📈 E. MARKET FORECASTING DATASETS (≤7 GB)

### 📂 `data/market/agmarknet/`
**Dataset**: Agmarknet Historical Prices (5 years)  
**📥 Source**: https://agmarknet.gov.in/  
**Enhanced Portal**: https://agmarknet.ceda.ashoka.edu.in/  
**Size**: ~1-1.5 GB  

---

### 📂 `data/market/imd_weather/`
**Dataset**: IMD Weather Data (District-level)  
**📥 Source**: https://mausam.imd.gov.in/  
**Government**: India Meteorological Department  
**Size**: ~1 GB  

**Data Portal**: https://www.imdpune.gov.in/cmpg/Griddata/Rainfall_25_Bin.html  
**Alternative**: https://data.gov.in/

---

### 📂 `data/market/icrisat_district/`
**Dataset**: ICRISAT District Database  
**📥 Source**: http://data.icrisat.org/dld/  
**Research**: CGIAR Research Center  
**Size**: ~500 MB  

---

### 📂 `data/market/enam/`
**Dataset**: eNAM Real-time Trade Data  
**📥 Source**: https://enam.gov.in/  
**Government**: National Agriculture Market  
**Size**: ~300-500 MB  

---

### 📂 `data/market/state_mandis/`
**Dataset**: State Mandi Reports (Optional)  
**Size**: ~500 MB  

**📥 Sources**:
- Maharashtra APMC: https://www.mahaapmc.gov.in/
- Gujarat: https://agmarknet.gov.in/
- Karnataka: http://www.raitamitra.kar.nic.in/

---

### 📂 `data/market/policy_reports/`
**Dataset**: NABARD/NITI Reports (Optional)  
**Size**: ~200 MB  

**📥 Sources**:
- NABARD: https://www.nabard.org/
- NITI Aayog: https://www.niti.gov.in/
- Ministry of Agriculture: https://agricoop.nic.in/

---

## 🔗 QUICK ACCESS SUMMARY

### Government of India Sources
| Source | Link |
|--------|------|
| ICAR | http://www.icar.org.in/ |
| KRISHI Portal | https://krishi.icar.gov.in/ |
| Agmarknet | https://agmarknet.gov.in/ |
| Agmarknet Enhanced | https://agmarknet.ceda.ashoka.edu.in/ |
| eNAM | https://enam.gov.in/ |
| Bhashini | https://bhashini.gov.in/ |
| IMD | https://mausam.imd.gov.in/ |
| mKisan | https://mkisan.gov.in/ |
| Ministry of Agriculture | https://agricoop.nic.in/ |

### IIT/Academic Research
| Source | Link |
|--------|------|
| AI4Bharat | https://github.com/AI4Bharat |
| IndicVoices | https://huggingface.co/datasets/ai4bharat/indicvoices_r |
| IndicTrans2 | https://github.com/AI4Bharat/indictrans |
| CEDA Ashoka | https://agmarknet.ceda.ashoka.edu.in/ |

### State Agricultural Universities
| University | Link |
|------------|------|
| TNAU | https://tnau.ac.in/ |
| PAU | https://www.pau.edu/ |
| UAS Bangalore | https://uasbangalore.edu.in/ |
| ANGRAU | https://angrau.ac.in/ |

### International Research
| Source | Link |
|--------|------|
| ICRISAT | http://data.icrisat.org/dld/ |
| FAO | https://www.fao.org/faostat/ |

### Open Source Platforms
| Platform | Link |
|----------|------|
| OpenSLR | http://openslr.org/ |
| HuggingFace | https://huggingface.co/ |
| Kaggle | https://www.kaggle.com/datasets |

---

**🇮🇳 100% India-Focused | 🎓 IIT/ICAR-Backed | 💾 ≤42 GB | 🏆 SIH 2025 Ready**
