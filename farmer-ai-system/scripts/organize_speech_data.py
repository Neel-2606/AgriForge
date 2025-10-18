"""
Speech Dataset Organization Guide
Helps organize Mozilla Common Voice and alternative datasets
"""

from pathlib import Path
import json
import shutil

# ============================================================================
# SPEECH DATA ORGANIZATION
# ============================================================================

BASE_DIR = Path("D:/SIH/farmer-ai-system")
SPEECH_DIR = BASE_DIR / "data" / "speech"

def create_speech_directory_structure():
    """Create proper directory structure for speech datasets"""
    
    # Mozilla Common Voice structure
    mozilla_languages = [
        "hindi", "bengali", "tamil", "telugu", "marathi", 
        "malayalam", "urdu", "odia"
    ]
    
    # Alternative sources for missing languages
    alternatives = {
        "gujarati": ["openslr_compact", "iit_corpus", "bhashini_sample"],
        "kannada": ["openslr_compact", "iisc_corpus", "svarah"]
    }
    
    print("Creating speech dataset directory structure...")
    
    # 1. Mozilla Common Voice directories
    for lang in mozilla_languages:
        for split in ["train", "dev", "test"]:
            clips_dir = SPEECH_DIR / "common_voice" / lang / split / "clips"
            clips_dir.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created: {clips_dir}")
    
    # 2. Alternative source directories
    for lang, sources in alternatives.items():
        for source in sources:
            source_dir = SPEECH_DIR / source / lang
            source_dir.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created: {source_dir}")
    
    # 3. Create organization guide
    guide = {
        "mozilla_common_voice": {
            "languages_available": mozilla_languages,
            "structure": "common_voice/{language}/{train|dev|test}/clips/",
            "file_format": "mp3 + tsv metadata",
            "download_from": "https://commonvoice.mozilla.org/datasets"
        },
        "missing_languages": {
            "gujarati": {
                "sources": [
                    {
                        "name": "OpenSLR-78",
                        "url": "http://openslr.org/78/",
                        "directory": "openslr_compact/gujarati/",
                        "size": "~300 MB"
                    },
                    {
                        "name": "IIT Bombay Corpus",
                        "url": "https://www.cfilt.iitb.ac.in/",
                        "directory": "iit_corpus/gujarati/",
                        "size": "~200 MB"
                    }
                ]
            },
            "kannada": {
                "sources": [
                    {
                        "name": "OpenSLR-79", 
                        "url": "http://openslr.org/79/",
                        "directory": "openslr_compact/kannada/",
                        "size": "~250 MB"
                    },
                    {
                        "name": "IISc Corpus",
                        "url": "Research datasets from IISc Bangalore",
                        "directory": "iisc_corpus/kannada/",
                        "size": "~200 MB"
                    }
                ]
            }
        }
    }
    
    guide_file = SPEECH_DIR / "speech_dataset_organization_guide.json"
    with open(guide_file, "w") as f:
        json.dump(guide, f, indent=2)
    
    print(f"\n📄 Organization guide saved: {guide_file}")
    return guide_file

def create_mozilla_instructions():
    """Create step-by-step Mozilla download instructions"""
    
    instructions = """
# 🎤 Mozilla Common Voice Download Instructions

## Step 1: Download from Mozilla
1. Go to: https://commonvoice.mozilla.org/datasets
2. Create account (free)
3. Download these languages:

### Available Languages:
✅ Hindi (hi) - ~2 GB
✅ Bengali (bn) - ~1.5 GB  
✅ Tamil (ta) - ~1.2 GB
✅ Telugu (te) - ~800 MB
✅ Marathi (mr) - ~600 MB
✅ Malayalam (ml) - ~400 MB
✅ Urdu (ur) - ~300 MB
✅ Odia (or) - ~200 MB

## Step 2: Extract Files
After download, extract each language to:

```
data/speech/common_voice/
├── hindi/
│   ├── train/
│   │   ├── clips/          # Put .mp3 files here
│   │   └── train.tsv       # Metadata file
│   ├── dev/
│   │   ├── clips/
│   │   └── dev.tsv
│   └── test/
│       ├── clips/
│       └── test.tsv
├── bengali/
│   ├── train/clips/
│   ├── dev/clips/
│   └── test/clips/
... (repeat for all languages)
```

## Step 3: Verify Structure
Run this script to verify:
```bash
python scripts/verify_speech_data.py
```

## Missing Languages Solutions:

### Gujarati (Not in Mozilla):
1. **OpenSLR-78**: http://openslr.org/78/
   - Extract to: data/speech/openslr_compact/gujarati/
   
2. **IIT Bombay**: https://www.cfilt.iitb.ac.in/
   - Extract to: data/speech/iit_corpus/gujarati/

### Kannada (Not in Mozilla):
1. **OpenSLR-79**: http://openslr.org/79/
   - Extract to: data/speech/openslr_compact/kannada/
   
2. **IISc Bangalore**: Research datasets
   - Extract to: data/speech/iisc_corpus/kannada/

## Total Expected Size: ~8-10 GB
"""
    
    instructions_file = SPEECH_DIR / "MOZILLA_DOWNLOAD_INSTRUCTIONS.md"
    with open(instructions_file, "w") as f:
        f.write(instructions)
    
    print(f"📋 Download instructions saved: {instructions_file}")
    return instructions_file

if __name__ == "__main__":
    print("Setting up speech dataset organization...")
    
    # Create directory structure
    guide_file = create_speech_directory_structure()
    
    # Create download instructions
    instructions_file = create_mozilla_instructions()
    
    print("\n" + "="*80)
    print("SPEECH DATASET SETUP COMPLETE!")
    print("="*80)
    print(f"\n📂 Speech data directory: {SPEECH_DIR}")
    print(f"📄 Organization guide: {guide_file}")
    print(f"📋 Download instructions: {instructions_file}")
    print("\n🎯 Next steps:")
    print("1. Download Mozilla Common Voice datasets (8 languages)")
    print("2. Download OpenSLR datasets for Gujarati & Kannada")
    print("3. Run verification script to check data integrity")
