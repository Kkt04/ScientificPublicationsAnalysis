import os
import sys

sys.path.append('./src')

from data_loader import DataLoader
from analyzer import PublicationAnalyzer

def main():
    print("🚀 SCIENTIFIC PUBLICATIONS ANALYSIS - PHASE 1")
    print("=" * 50)
    loader = DataLoader()
    analyzer = PublicationAnalyzer()
    print("\n📥 Step 1: Loading data...")
    data = loader.create_sample_from_real_data(sample_size=1000)
    
    print("\n📊 Step 2: Data statistics...")
    stats = loader.get_data_stats(data)
    
    print("\n🔍 Step 3: Running analysis...")
    
    # Category analysis
    categories = analyzer.analyze_categories(data)
    
    # Timeline analysis  
    timeline = analyzer.analyze_timeline(data)
    
    # Abstract analysis
    abstracts = analyzer.analyze_abstracts(data)
    

    print("\n" + "=" * 50)
    print("✅ PHASE 1 COMPLETED SUCCESSFULLY!")
    print("=" * 50)
    print("📁 Generated Files:")
    print("   - data/sample/sample_data.csv")
    print("   - top_categories.png")
    print("   - publication_timeline.png") 
    print("   - abstract_analysis.png")
    print(f"📊 Papers analyzed: {len(data):,}")
    print(f"🔬 Unique categories: {data['categories'].str.split().explode().nunique()}")
    print("\n🎯 Next: Run 'jupyter notebook' to explore in notebooks/exploration.ipynb")

if __name__ == "__main__":
    main()