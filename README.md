# Game Cheating Detection System 🎮🛡️

## Overview
This project detects cheating behavior in online FPS games (e.g., Valorant, CS:GO) using player behavioral data and machine learning. It demonstrates how data science and cybersecurity can be combined to improve game integrity.

## Features
- Behavioral analysis using player stats (accuracy, headshot ratio, etc.)
- Cheat detection with Isolation Forest (unsupervised anomaly detection)
- Comparison with known cheaters (if labeled data is available)
- Visualization of anomalies
- Extendable to real-time data or MMO-style games

## Dataset
The `player_behavior.csv` file includes simulated data with the following fields:
- `accuracy`: Hit accuracy (0 to 1)
- `headshot_ratio`: Proportion of headshots
- `movement_speed`: Player movement speed (units/sec)
- `reaction_time`: Time to react (seconds)
- `kdr`: Kill/Death ratio
- `suspected`: Ground truth label (1 = suspected cheater, 0 = normal)

## How to Use
1. Install dependencies:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn
   ```

2. Run the detection script:
   ```bash
   python scripts/detect_cheaters.py
   ```

3. Output:
   - `data/detected_cheaters.csv`: Result with predictions
   - `data/cheater_detection_plot.png`: Visual anomaly detection
   - Console output: Classification report

## Future Extensions
- Apply to MMO games with economic behavior metrics
- Add supervised learning models (e.g., logistic regression)
- Real-time detection via online data streams
- Integrate into game servers for live moderation

## Authors
Developed as part of a cybersecurity + data science portfolio project.
