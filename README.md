# Trader Behavior Insights - Junior Data Scientist Assignment

**Goal:** Explore relationship between Bitcoin market sentiment (Fear/Greed) and trader performance (Hyperliquid historical data).

## Included files
- `trader_behavior_analysis.ipynb` - Jupyter notebook with step-by-step data loading, cleaning, EDA, merging with sentiment, visualizations, and example statistical tests.
- `analysis_script.py` - Script version of the main notebook (can be run as a script).
- `requirements.txt` - Python dependencies.
- `sample_paths.txt` - Guidance for placing/downloading dataset files.

## How to use
1. Download your datasets from the links provided in the assignment and place them inside a `data/` folder (same level as the notebook) as:
   - `data/hyperliquid_historical.csv`  (Historical trader data)
   - `data/fear_greed_index.csv`       (Fear/Greed daily sentiment)
2. Open and run `trader_behavior_analysis.ipynb` in Jupyter or Visual Studio Code.
3. Alternatively, run `python analysis_script.py --trader data/hyperliquid_historical.csv --sentiment data/fear_greed_index.csv`

## Notes
- The notebook contains robust data-cleaning steps, helpful visualizations, and suggested extensions.
- If your data files are large, consider testing on a subset first (e.g., `head -n 100000` for CSVs).
