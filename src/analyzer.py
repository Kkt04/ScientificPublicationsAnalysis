# src/analyzer.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class PublicationAnalyzer:
    def __init__(self):
        plt.style.use('default')
        sns.set_palette("husl")
        
    def load_sample_data(self):
        """Load the sample data we created"""
        return pd.read_csv('data/sample/sample_data.csv')
    
    def analyze_categories(self, df):
        """Analyze research categories"""
        print("\n🔬 ANALYZING RESEARCH CATEGORIES...")
        
        df['category_list'] = df['categories'].str.split()
        all_categories = df['category_list'].explode()
        
        top_categories = all_categories.value_counts().head(10)
        
        plt.figure(figsize=(12, 6))
        top_categories.plot(kind='bar', color='lightcoral')
        plt.title('Top 10 Research Categories in Sample', fontweight='bold')
        plt.xlabel('Category')
        plt.ylabel('Number of Papers')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('top_categories.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return top_categories
    
    def analyze_timeline(self, df):
        """Analyze publication timeline"""
        print("\n📅 ANALYZING PUBLICATION TIMELINE...")
        df['year'] = pd.to_datetime(df['update_date']).dt.year
        yearly_counts = df['year'].value_counts().sort_index()
        
        plt.figure(figsize=(12, 6))
        yearly_counts.plot(kind='line', marker='o', linewidth=2, markersize=8)
        plt.title('Publication Timeline', fontweight='bold')
        plt.xlabel('Year')
        plt.ylabel('Number of Publications')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('publication_timeline.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return yearly_counts
    
    def analyze_abstracts(self, df):
        """Basic analysis of paper abstracts"""
        print("\n📝 ANALYZING PAPER ABSTRACTS...")
        
        df['abstract_length'] = df['abstract'].str.len()
        
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        df['abstract_length'].hist(bins=20, color='lightgreen', alpha=0.7)
        plt.title('Abstract Length Distribution')
        plt.xlabel('Abstract Length (characters)')
        plt.ylabel('Frequency')
        
        plt.subplot(1, 2, 2)
        df['abstract_length'].plot(kind='box')
        plt.title('Abstract Length Box Plot')
        plt.ylabel('Length (characters)')
        
        plt.tight_layout()
        plt.savefig('abstract_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Average abstract length: {df['abstract_length'].mean():.0f} characters")
        print(f"Longest abstract: {df['abstract_length'].max()} characters")
        print(f"Shortest abstract: {df['abstract_length'].min()} characters")
        
        return df['abstract_length'].describe()

def main_analysis():
    print("🚀 STARTING ARXIV DATASET ANALYSIS - PHASE 1")
    print("="*60)
    
    analyzer = PublicationAnalyzer()
    df = analyzer.load_sample_data()
    
    print(f"📁 Loaded dataset with {len(df)} papers")
    print(f"📊 Columns: {list(df.columns)}")
    
    categories = analyzer.analyze_categories(df)
    timeline = analyzer.analyze_timeline(df)
    abstracts = analyzer.analyze_abstracts(df)
    
    print("\n" + "="*60)
    print("✅ PHASE 1 ANALYSIS COMPLETE!")
    print("="*60)
    print("📈 Generated Charts:")
    print("   - top_categories.png (Top 10 research categories)")
    print("   - publication_timeline.png (Publication growth)")
    print("   - abstract_analysis.png (Abstract length analysis)")
    print(f"📚 Papers analyzed: {len(df):,}")
    print(f"🔬 Categories found: {df['category_list'].explode().nunique()}")

if __name__ == "__main__":
    main_analysis()