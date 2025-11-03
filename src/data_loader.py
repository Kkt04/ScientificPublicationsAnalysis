# src/data_loader.py
import pandas as pd
import json
import os
from tqdm import tqdm

class DataLoader:
    def __init__(self):
        self.raw_data_path = "data/raw/arxiv-metadata-oai-snapshot.json"
        self.sample_data_path = "data/sample/sample_data.csv"
        
    def create_sample_from_real_data(self, sample_size=1000):
        """Create a manageable sample from the real ArXiv dataset"""
        print(" Creating sample from real ArXiv data...")
        
        # Check if raw data exists
        if not os.path.exists(self.raw_data_path):
            print(" Real dataset not found! Creating demo data instead.")
            return self.create_demo_data()
        
        sample_data = []
        try:
            with open(self.raw_data_path, 'r') as f:
                for i, line in tqdm(enumerate(f), total=sample_size, desc="Reading lines"):
                    if i >= sample_size:
                        break
                    data = json.loads(line)
                    sample_data.append({
                        'id': data.get('id', ''),
                        'title': data.get('title', ''),
                        'authors': data.get('authors', ''),
                        'categories': data.get('categories', ''),
                        'abstract': data.get('abstract', '')[:200] + '...',
                        'update_date': data.get('update_date', ''),
                        'versions': len(data.get('versions', []))
                    })
            
            df = pd.DataFrame(sample_data)
            
            os.makedirs('data/sample', exist_ok=True)
            
            df.to_csv(self.sample_data_path, index=False)
            print(f" Sample created with {len(df)} records from real data!")
            return df
            
        except Exception as e:
            print(f" Error reading real data: {e}")
            print(" Creating demo data instead...")
            return self.create_demo_data()
    
    def create_demo_data(self):
        """Create demo data if real dataset is not available"""
        print(" Creating demo data for testing...")
        
        demo_data = {
            'id': [f'2001.0000{i}' for i in range(1, 101)],
            'title': [f'Research Paper on AI Topic {i}' for i in range(1, 101)],
            'authors': [f'Author {i}, Co-author {i}' for i in range(1, 101)],
            'categories': ['cs.AI']*30 + ['cs.LG']*25 + ['cs.CV']*20 + ['stat.ML']*15 + ['math.OC']*10,
            'abstract': [f'This is abstract for paper {i} discussing machine learning topics.' for i in range(1, 101)],
            'update_date': [f'202{i%3}-{str((i%12)+1).zfill(2)}-{str((i%28)+1).zfill(2)}' for i in range(1, 101)],
            'versions': [1] * 100
        }
        
        df = pd.DataFrame(demo_data)
        os.makedirs('data/sample', exist_ok=True)
        df.to_csv(self.sample_data_path, index=False)
        print(" Demo data created with 100 records!")
        return df
    
    def get_data_stats(self, df):
        """Get statistics about the dataset"""
        print("\n" + "="*60)
        print(" DATASET STATISTICS")
        print("="*60)
        print(f"Total papers: {len(df):,}")
        print(f"Columns: {list(df.columns)}")
        print(f"Date range: {df['update_date'].min()} to {df['update_date'].max()}")
        
        categories = df['categories'].str.split().explode()
        print(f"Unique categories: {categories.nunique()}")
        print("\nTop 10 categories:")
        print(categories.value_counts().head(10))
        
        return {
            'total_papers': len(df),
            'unique_categories': categories.nunique(),
            'date_range': (df['update_date'].min(), df['update_date'].max())
        }

if __name__ == "__main__":
    loader = DataLoader()
    data = loader.create_sample_from_real_data(sample_size=1000)
    stats = loader.get_data_stats(data)
