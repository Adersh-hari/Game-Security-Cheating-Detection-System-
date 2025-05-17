# Game Security & Cheating Detection System

This project develops a behavioral analysis and cheat detection system for multiplayer FPS games (e.g., Valorant, PUBG). It leverages unsupervised machine learning to identify cheating patterns and improve game fairness.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Files](#key-files)
- [Data Flow & Analysis](#data-flow--analysis)
- [Detection Methodology](#detection-methodology)
- [Technologies Used](#technologies-used)
- [Project Status](#project-status)

## Project Overview

This system simulates player behavioral data and uses Isolation Forest to detect anomalous patterns consistent with cheating or unfair play. It aims to support game security by providing actionable cheat flags and analytics.

## Key Files

- [data/player_behavior.csv](data/player_behavior.csv) — Simulated player stats with suspected cheater labels.
- [scripts/detect_cheaters.py](scripts/detect_cheaters.py) — Runs anomaly detection and outputs flagged players.
- [report/cheat_detection_report.txt](report/cheat_detection_report.txt) — Explains methodology, results, and next steps.
- [requirements.txt](requirements.txt) — Lists Python dependencies for easy setup.

## Data Flow & Analysis

Player behavioral features (accuracy, reaction time, movement speed, etc.) are processed through an Isolation Forest model to identify outliers. The results are saved with prediction labels and visualized to aid interpretation.

## Detection Methodology

- Uses **Isolation Forest** for unsupervised anomaly detection.
- Features analyzed include accuracy, headshot ratio, movement speed, reaction time, and kill/death ratio.
- Model flags players whose behavior significantly deviates from typical patterns as suspected cheaters.

## Technologies Used

- Python (data processing and machine learning)
- pandas (data manipulation)
- scikit-learn (machine learning)
- matplotlib & seaborn (visualization)
- Git/GitHub (version control)

## Project Status

*Completed*  
This project serves as a cybersecurity portfolio piece demonstrating practical cheat detection techniques using data science.

## Project Structure

- [data/](data/)
- [scripts/](scripts/)
- [report/](report/)

---

*Feel free to explore, adapt, or extend this system for game security research or applications!*
